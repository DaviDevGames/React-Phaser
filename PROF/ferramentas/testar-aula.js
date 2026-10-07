/**
 * Harness de teste da trilha "Meu Primeiro Jogo".
 *
 * Abre a aula num Chrome headless de verdade, espera a cena do Phaser
 * carregar, executa um CENÁRIO (teclas reais + esperas + fotos) e coleta
 * o estado do jogo com uma SONDAGEM em cada ponto de checagem.
 *
 * Uso:
 *   node testar.js <standalone|react> <alvo> <probe.js> <shot.png> [cenario.json]
 */
const fs = require('fs')
const path = require('path')
const http = require('http')
const puppeteer = require('puppeteer')

const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json',
  '.svg': 'image/svg+xml', '.woff2': 'font/woff2',
}

function servir(dir) {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let p = decodeURIComponent(req.url.split('?')[0])
      if (p === '/') p = '/index.html'
      const file = path.join(dir, p)
      if (!file.startsWith(dir) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
        res.writeHead(404); res.end('nao encontrado: ' + p); return
      }
      res.writeHead(200, { 'Content-Type': MIME[path.extname(file)] || 'application/octet-stream' })
      fs.createReadStream(file).pipe(res)
    })
    server.listen(0, '127.0.0.1', () => resolve({ server, port: server.address().port }))
  })
}

const dormir = (ms) => new Promise((r) => setTimeout(r, ms))

async function esperarCena(page, timeoutMs = 30000) {
  const t0 = Date.now()
  while (Date.now() - t0 < timeoutMs) {
    const ok = await page.evaluate(() => {
      try {
        const j = window.jogo
        if (!j || !j.isBooted) return false
        const s = j.scene.getScene('Jogo')
        if (!s || !s.scene.isActive()) return false
        return !(s.load && s.load.isLoading && s.load.isLoading())
      } catch (e) { return false }
    })
    if (ok) return true
    await dormir(250)
  }
  return false
}

async function main() {
  const [modo, alvo, probeFile, shotFile, cenarioFile] = process.argv.slice(2)
  const erros = []
  const avisos = []
  const snapshots = {}

  let url, server = null
  if (modo === 'standalone') {
    url = 'file://' + path.resolve(alvo)
  } else {
    const distDir = path.join(alvo, 'dist')
    if (!fs.existsSync(path.join(distDir, 'index.html'))) {
      console.log(JSON.stringify({ erro: 'build do React nao encontrado em ' + distDir }))
      process.exit(2)
    }
    const s = await servir(distDir)
    server = s.server
    url = `http://127.0.0.1:${s.port}/`
  }

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files',
           '--disable-dev-shm-usage', '--force-device-scale-factor=1',
           '--autoplay-policy=no-user-gesture-required'],
  })
  const page = await browser.newPage()
  await page.setViewport({ width: 1400, height: 820 })

  page.on('console', (msg) => {
    if (msg.type() === 'error') erros.push('console: ' + msg.text())
  })
  page.on('pageerror', (err) => erros.push('pageerror: ' + (err && err.message)))
  page.on('requestfailed', (req) => erros.push('falhou ao carregar: ' + req.url().split('/').slice(-2).join('/')))

  await page.goto(url, { waitUntil: 'load', timeout: 40000 })
  const carregou = await esperarCena(page)
  if (!carregou) erros.push('a cena "Jogo" nao ficou ativa em 30s')

  const fonteProbe = probeFile && fs.existsSync(probeFile) ? fs.readFileSync(probeFile, 'utf8') : null
  async function sondar() {
    if (!fonteProbe) return null
    try {
      return await page.evaluate(`(${fonteProbe})()`)
    } catch (e) {
      erros.push('probe falhou: ' + e.message)
      return null
    }
  }

  // clica no canvas para o jogo "ganhar" o teclado
  try { await page.click('canvas') } catch (e) { /* ok */ }
  await dormir(300)

  if (carregou) {
    const cenario = cenarioFile && fs.existsSync(cenarioFile)
      ? JSON.parse(fs.readFileSync(cenarioFile, 'utf8'))
      : []

    if (!cenario.length) {
      await dormir(1200)
      snapshots['estado'] = await sondar()
    }

    for (const passo of cenario) {
      if (passo.tipo === 'tecla') {
        await page.keyboard.down(passo.tecla)
        await dormir(passo.ms || 300)
      } else if (passo.tipo === 'soltar') {
        await page.keyboard.up(passo.tecla)
        await dormir(passo.ms || 120)
      } else if (passo.tipo === 'esperar') {
        await dormir(passo.ms || 500)
      } else if (passo.tipo === 'foto') {
        await page.screenshot({ path: passo.arquivo })
        continue
      } else if (passo.tipo === 'sondar') {
        // só coleta o estado, sem esperar
      } else if (passo.tipo === 'esperarAte') {
        const limite = Date.now() + (passo.timeout || 15000)
        let ok = false
        while (Date.now() < limite) {
          ok = await page.evaluate(passo.condicao)
          if (ok) break
          await dormir(150)
        }
        if (!ok) erros.push('esperarAte estourou o tempo: ' + passo.condicao.slice(0, 60))
      }
      if (passo.rotulo) snapshots[passo.rotulo] = await sondar()
    }

    // solta todas as teclas no final
    for (const t of ['ArrowRight', 'ArrowLeft', 'ArrowUp', 'ArrowDown', 'Space', 'KeyA', 'KeyD']) {
      try { await page.keyboard.up(t) } catch (e) { /* ok */ }
    }
  }

  if (shotFile) {
    await dormir(400)
    await page.screenshot({ path: shotFile })
  }

  await browser.close()
  if (server) server.close()

  console.log(JSON.stringify({ modo, alvo: path.basename(alvo), carregou, erros, avisos, snapshots }, null, 2))
  process.exit(erros.length ? 1 : 0)
}

main().catch((e) => { console.error('FALHA GERAL:', e); process.exit(3) })
