# ✅ Relatório de testes — trilha "Meu Primeiro Jogo"

Todas as aulas foram **executadas em navegador real** (Chrome headless, via
Puppeteer) antes de serem publicadas. Este arquivo registra o que foi
verificado e o resultado.

**Data da verificação:** outubro de 2026
**Ambiente:** Node.js 20 · Chrome for Testing 154 · Phaser 3.90 (standalone) · Phaser 4.x (React/Vite)

---

## 1. Carregamento e execução — 24/24 ✅

Cada aula foi testada nos **dois formatos** (sem instalação e React + Vite),
verificando: erros de console, recursos que não carregaram, cena ativa e
estado do jogo.

| Aula | Sem instalação | React + Vite |
|---|---|---|
| 01 — Plano de Fundo | ✅ | ✅ |
| 02 — Chão | ✅ | ✅ |
| 03 — Cenário Completo | ✅ | ✅ |
| 04 — Personagem | ✅ | ✅ |
| 05 — Inimigo | ✅ | ✅ |
| 06 — Movimento do Personagem | ✅ | ✅ |
| 07 — Movimento do Inimigo | ✅ | ✅ |
| 08 — Colisão do Personagem | ✅ | ✅ |
| 09 — Colisão do Inimigo | ✅ | ✅ |
| 10 — Objetos em Tela | ✅ | ✅ |
| 11 — Novas Plataformas | ✅ | ✅ |
| 12 — HUD / UI-UX | ✅ | ✅ |

**Resultado:** 24/24 verificações sem erros de console ou recursos faltando.

## 2. Build de produção (React + Vite) — 12/12 ✅

`npm install && npm run build` executado em cada aula `*/react`.
Todas as 12 builds concluíram com sucesso (é o mesmo que o CI do
repositório — `.github/workflows/ci-exemplos.yml` — faz).

## 3. Comportamento do jogo (testes com teclado simulado) ✅

Aulas com lógica foram testadas "jogando" de verdade, com teclas simuladas:

| Aula | O que foi verificado | Resultado |
|---|---|---|
| 03 | as 4 camadas do cenário se movem em velocidades diferentes (parallax) | ✅ |
| 04 | o herói aparece com os pés no chão; animação de 2 quadros alternando | ✅ |
| 05 | 3 gosmas criadas pelo método `criarInimigo(x)`, cada uma na sua posição | ✅ |
| 06 | aterrissagem, andar para os dois lados, virar o desenho (`flip`), pular, `blocked.down` voltando a verdadeiro, animação correta em cada estado, teclas A/D | ✅ |
| 07 | velocidades diferentes por gosma (88, 96, 84 px/s), todas virando nas bordas do mundo | ✅ |
| 08 | colisão com a gosma → invencibilidade ativa → empurrão → retorno ao início | ✅ |
| 09 | pisão em cima da gosma → inimigo derrotado (contador subiu) sem levar dano | ✅ |
| 10 | coleta de moeda (+100), texto no HUD atualizando, "+100" subindo e sumindo | ✅ |
| 11 | subir em plataforma (colisão), coletar moeda no ar | ✅ |
| 12 | HUD com 3 corações; cada dano remove 1 coração; 0 vidas → GAME OVER; tecla R → reinício com 3 vidas e 0 pontos | ✅ |

## 4. Capturas de tela

As 12 imagens `screenshot.png` (uma por aula, usadas nos READMEs) foram
capturadas automaticamente **do jogo rodando** — não são montagens.

---

## Como repetir estes testes

```bash
node testar-aula.js standalone ../06-Movimento-do-Personagem/index.html sondagem.js saida.png cenario.json
node testar-aula.js react      ../12-HUD-UI-UX/react sondagem.js saida.png
```

Detalhes de uso (e exemplos de "cenário" e "sondagem") em
[README.md](README.md) desta pasta.
