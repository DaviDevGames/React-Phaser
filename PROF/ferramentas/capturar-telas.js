/**
 * Tira uma foto do canvas de cada aula (elemento canvas, sem a moldura do navegador).
 * Uso: node capturar.js
 */
const fs = require('fs'); const path = require('path'); const http = require('http'); const puppeteer = require('puppeteer');
const MIME = {'.html':'text/html','.js':'text/javascript','.css':'text/css','.png':'image/png','.json':'application/json'};
const TRILHA = './';
const dormir = ms => new Promise(r => setTimeout(r, ms));

// aula -> [({teclas}), espera, foto...]
const ROTEIRO = {
  '01-Plano-de-Fundo': { teclas: [], espera: 900 },
  '02-Chao': { teclas: [], espera: 900 },
  '03-Cenario-Completo': { teclas: [], espera: 2500 },
  '04-Personagem': { teclas: [], espera: 900 },
  '05-Inimigo': { teclas: [], espera: 900 },
  '06-Movimento-do-Personagem': { teclas: ['ArrowRight'], teclaMs: 900, espera: 200 },
  '07-Movimento-do-Inimigo': { teclas: [], espera: 4000 },
  '08-Colisao-do-Personagem': {
    passos: [
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.jogador.body.blocked.down })()" },
      { tipo: 'down', tecla: 'ArrowRight' },
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.invencivel === true })()", msMax: 40000 },
      { tipo: 'up', tecla: 'ArrowRight' },
      { tipo: 'dormir', ms: 250 },
    ],
  },
  '09-Colisao-do-Inimigo': {
    passos: [
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.jogador.body.blocked.down })()" },
      { tipo: 'down', tecla: 'ArrowRight' },
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.inimigosDerrotados > 0 })()", msMax: 60000 },
      { tipo: 'up', tecla: 'ArrowRight' },
      { tipo: 'dormir', ms: 200 },
    ],
  },
  '10-Objetos-em-Tela': {
    passos: [
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.jogador.body.blocked.down })()" },
      { tipo: 'down', tecla: 'ArrowRight' },
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.pontos > 0 })()", msMax: 40000 },
      { tipo: 'dormir', ms: 120 },
    ],
  },
  '11-Novas-Plataformas': {
    passos: [
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.jogador.body.blocked.down })()" },
      { tipo: 'down', tecla: 'ArrowRight' },
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.pontos >= 200 })()", msMax: 70000 },
      { tipo: 'down', tecla: 'Space' },
      { tipo: 'dormir', ms: 250 },
      { tipo: 'up', tecla: 'Space' },
      { tipo: 'dormir', ms: 600 },
    ],
  },
  '12-HUD-UI-UX': {
    passos: [
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.jogador.body.blocked.down })()" },
      { tipo: 'down', tecla: 'ArrowRight' },
      { tipo: 'ate', cond: "(() => { const c = window.jogo.scene.getScene('Jogo'); return c.pontos > 0 })()", msMax: 40000 },
      { tipo: 'up', tecla: 'ArrowRight' },
      { tipo: 'dormir', ms: 300 },
    ],
  },
};

(async () => {
  const browser = await puppeteer.launch({ headless: 'new',
    args: ['--no-sandbox','--disable-setuid-sandbox','--allow-file-access-from-files','--disable-dev-shm-usage'] });
  for (const [aula, cfg] of Object.entries(ROTEIRO)) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 820, deviceScaleFactor: 1 });
    const erros = [];
    page.on('pageerror', e => erros.push(e.message));
    page.on('console', m => { if (m.type() === 'error') erros.push(m.text()); });
    const arquivo = path.join(TRILHA, aula, 'index.html');
    await page.goto('file://' + arquivo, { waitUntil: 'load', timeout: 40000 });
    // espera a cena
    for (let i = 0; i < 100; i++) {
      const ok = await page.evaluate(() => { try { const s = window.jogo.scene.getScene('Jogo'); return s && s.scene.isActive(); } catch (e) { return false; } });
      if (ok) break;
      await dormir(250);
    }
    await page.click('canvas');
    await dormir(250);

    if (cfg.passos) {
      for (const p of cfg.passos) {
        if (p.tipo === 'ate') {
          const lim = Date.now() + (p.msMax || 20000);
          let ok = false;
          while (Date.now() < lim) { ok = await page.evaluate(p.cond); if (ok) break; await dormir(150); }
          if (!ok) erros.push('timeout espera');
        } else if (p.tipo === 'down') await page.keyboard.down(p.tecla);
        else if (p.tipo === 'up') await page.keyboard.up(p.tecla);
        else if (p.tipo === 'dormir') await dormir(p.ms);
      }
    } else {
      for (const t of (cfg.teclas || [])) await page.keyboard.down(t);
      await dormir(cfg.teclaMs || 100);
      await dormir(cfg.espera || 500);
      for (const t of (cfg.teclas || [])) await page.keyboard.up(t);
    }
    const canvas = await page.$('canvas');
    const destino = path.join(__dirname, 'capturas', aula + '.png');
    fs.mkdirSync(path.dirname(destino), { recursive: true });
    await canvas.screenshot({ path: destino });
    console.log(`${aula}: foto ok ${erros.length ? '| ERROS: ' + erros.slice(0,2).join(' ; ') : ''}`);
    await page.close();
  }
  await browser.close();
})();
