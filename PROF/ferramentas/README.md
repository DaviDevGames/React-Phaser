# 🛠️ ferramentas — como esta trilha foi feita (e como mantê-la)

Esta pasta é **opcional para quem estuda** (o aluno não precisa dela!) e
serve para quem quer **manter ou ampliar** a trilha: regenerar a arte,
testar as aulas automaticamente e tirar os prints usados nos READMEs.

> Se você só quer estudar, volte para o [README da trilha](../README.md). 🙂

---

## O que tem aqui

| Arquivo | Para que serve |
|---|---|
| `gerar-arte.py` | Desenha **toda a arte** (Milo, gosma, moedas, chão, cenário) e salva os PNGs. Pixel art gerada por código, em estilo "desenhe e amplie". |
| `testar-aula.js` | Abre uma aula num **Chrome de verdade** (headless), simula teclado e lê o estado do jogo (posição, animação, pontos, vidas) para checar se tudo funciona. |
| `capturar-telas.js` | Roda as 12 aulas e tira o print do *canvas* de cada uma → `capturas/*.png` (é de onde vêm os `screenshot.png` das aulas). |

---

## Requisitos

```bash
node -v            # Node.js 18+ (ideal 20)
python3 -V         # Python 3.10+
pip install pillow numpy            # para gerar a arte
npm install puppeteer               # para os testes e as capturas
```

---

## 1) Regerar a arte

```bash
python3 gerar-arte.py
```

Ele cria uma pasta `art_out/` com todos os PNGs. Os tamanhos principais:

| Arquivo | Quadro | Observação |
|---|---|---|
| `heroi-parado.png` | 128x128 (2 quadros) | os pés terminam na **última linha** do quadro (é o que faz o `setOrigin(0.5, 1)` encaixar perfeito) |
| `heroi-correndo.png` | 128x128 (4 quadros) | |
| `heroi-pulando.png` / `heroi-dano.png` | 128x128 (1 quadro) | |
| `gosma-andando.png` | 104x80 (4 quadros) | |
| `gosma-derrotada.png` | 104x80 (2 quadros) | |
| `moeda.png` | 64x64 (4 quadros) | |
| `estrela.png` / `coracao.png` | 64x64 | |
| `chao.png` | 128x128 | **repete sem emenda**; a grama fica na borda de cima |
| `plataforma.png` | 192x64 | repete na horizontal |
| `nuvens.png`, `montanhas.png`, `montanhas-claras.png`, `ceu.png` | 1280 de largura | repetem sem emenda (perfeitos para `tileSprite`/parallax) |

> ⚠️ **Regra de ouro:** o chão tem 128 de altura. Se você mudar o tamanho do
> tile, lembre-se de usar **múltiplos** dele na constante `ALTURA_CHAO` das
> cenas — senão o `tileSprite` repete a grama no meio da terra (foi
> exatamente esse detalhe que ajustamos na aula 02).

Para distribuir a arte às aulas, o script de montagem do material copia os
arquivos para `assets/` (versão sem instalação) e `react/public/assets/`
(versão React) de cada aula.

## 2) Testar uma aula automaticamente

```bash
node testar-aula.js standalone ../06-Movimento-do-Personagem/index.html probes/estado.js saida.png cenario.json
node testar-aula.js react      ../06-Movimento-do-Personagem/react probes/estado.js saida.png
```

* `standalone` abre o `index.html` por `file://`; `react` serve a pasta `dist/`
  (rode `npm run build` antes).
* O **cenário** (JSON) descreve o teste: `tecla`, `soltar`, `esperar`,
  `esperarAte` (com uma condição em JavaScript), `foto` e `sondar`.
* A **sondagem** é um arquivo `.js` com uma função que devolve o estado do
  jogo (posição do jogador, animação, pontos, vidas...). O resultado sai em
  JSON no terminal.

Exemplo de condição usada nos testes deste repositório:

```js
"(() => { const c = window.jogo.scene.getScene('Jogo'); return c.jogador.body.blocked.down })()"
```

> 💡 **Por que existe `window.jogo`?** No `main.js` (e no `PhaserGame.jsx`)
> guardamos o jogo numa variável global para você poder explorar no console
> (F12). É esse mesmo gancho que permite os testes automáticos. 🙂

## 3) Tirar os prints das aulas

```bash
node capturar-telas.js      # usa o bloco ROTEIRO para saber o que fazer em cada aula
```

As imagens saem em `capturas/`. Copie a que quiser para
`<Aula>/screenshot.png`.

---

## Como a trilha foi verificada

Antes de publicar, **todas as 12 aulas** foram executadas em navegador real:

* as **12 versões sem instalação** e as **12 versões React** carregaram sem
  erro de console;
* verificamos movimento (andar, virar, pular), troca de animação, colisão
  com o chão, dano com invencibilidade, **pisão** com derrota do inimigo,
  coleta de moedas com pontuação, plataformas e a sequência completa de
  **vidas → game over → reinício** da aula 12;
* as 12 versões React também passaram no `npm run build` (é o que o CI do
  repositório faz, veja `.github/workflows/ci-exemplos.yml`).

Se você mudar o código de uma aula, rode o teste dela de novo — leva
menos de 1 minuto e evita publicar aulas quebradas. 💚
