# 🧑‍🏫 Material do Professor(a) — trilha "Meu Primeiro Jogo"

> Este documento é **complementar** aos 12 `README.md` das aulas.
> Ele traz: objetivos pedagógicos, plano de curso, respostas dos desafios,
> os erros mais comuns da turma (e como destravá-los), proposta de avaliação
> e ideias de culminância.

---

## 1. Para quem é esta trilha

| Público | Como usar |
|---|---|
| **8 a 11 anos** | Faça as aulas 01–06 em ritmo de 1 por encontro. As tarefas "mude o número" são as favoritas. O professor digita junto, projetando a tela. |
| **12 a 14 anos** | Trilha completa em 8–10 encontros. Estimule a lerem o `Jogo.js` antes de rodar e a preverem o resultado. |
| **15 e 16 anos** | Trilha completa + desafios "⭐ DESAFIO" e, na sequência, os módulos `03-Cenarios`, `04-Fisica` e `06-VFX` do repositório. Podem ser convidados a criar uma aula nova para os mais novos (aprender ensinando!). |

**Pré-requisitos:** nenhum. Computador com navegador e editor de texto.
Nenhuma instalação é obrigatória (Jeito 1 do README da trilha).

---

## 2. Objetivos por bloco

| Bloco | Aulas | Conceitos de programação | Conceitos de jogos |
|---|---|---|---|
| **A. A tela é minha** | 01–02 | sequência de execução, coordenadas, constantes, repetição de imagem | pixel, camada, tile |
| **B. O mundo ganha vida** | 03–05 | variáveis, métodos com parâmetros, listas, `push`, dados | parallax, animação, spritesheet, level design inicial |
| **C. O jogo responde** | 06–08 | condicionais (`if/else`), operadores (`&&`, `||`), estado, callbacks | física, controle, colisão, *game feel*, invencibilidade |
| **D. O jogo tem regras** | 09–12 | flags, eventos, remoção de objetos, contadores | pisão, recompensa, risco × recompensa, HUD, UX |

Observe que a trilha segue uma progressão clássica de computação criativa:
**imitar → modificar → combinar → criar**.
Cada aula entrega código funcionando e pede modificações; ao final, o aluno
tem tudo para criar o seu próprio jogo.

---

## 3. Plano de curso sugerido (6 encontros de 90 min)

### Encontro 1 — "Eu mudo a tela do jogo!"
* Jogar o exemplo da aula 12 por 3 minutos (motivação: "vocês vão construir ISTO").
* Aulas 01 e 02. Fechamento: cada aluno troca a cor de fundo e o texto
  com o nome próprio.

### Encontro 2 — "A arte do cenário"
* Aulas 03 e 04. Quadro: desenhe na lousa as 5 camadas e peça que a turma
  escreva as velocidades (longe/rápido? perto/rápido?).
* Verificação: aluno coloca o herói em outra posição e explica por que ele
  continua "no chão".

### Encontro 3 — "O grande salto: física"
* Aula 05 (inimigos com lista) e **aula 06** (a mais importante).
* Sugestão: dividir em duas atividades — (a) teclado e velocidade,
  (b) pulo e animações.
* Erros esperados: esquecer o `else { setVelocityX(0) }` (personagem
  desliza) e testar o pulo sem `estaNoChao` (voo infinito). Ambos estão na
  tabela de problemas comuns do README.

### Encontro 4 — "O jogo morde de volta"
* Aulas 07 e 08. Comparar `collider` x `overlap` no quadro.
* Dinâmica de "playtest justo": um aluno joga, outro cronometra quantas
  vezes perde vida em 30 s. Depois ajustam numericamente e repetem.

### Encontro 5 — "O momento mais gostoso"
* Aulas 09 e 10. O pisão e as moedas.
* Conversa sobre *game feel*: o que deixa o acerto "satisfatório"?
  (tremor? som? partículas? número voando?).

### Encontro 6 — "Nível completo e apresentação"
* Aulas 11 e 12. Cada aluno/jogo personalizado é apresentado em 2 minutos:
  *"o que eu mudei e por quê"* (a explicação vale tanto quanto o jogo!).

> **Se você tem pouco tempo (4 encontros):** junte (01+02), (03+04+05),
> (06+07+08) e (09+10+11+12). A aula 06 nunca deve ser cortada ou apressada.

---

## 4. Respostas e direções dos desafios

Os desafios foram escritos para **várias respostas válidas**. Abaixo, a
intenção pedagógica e uma direção esperada:

### Aula 01 (Plano de Fundo)
1. Trocar a imagem → `'assets/chao.png'`: aparece o ladrilho esticado;
   ótimo momento para falar sobre **coordenadas e repetição**.
2. `setOrigin(0.5, 0.5)` centraliza o céu em (640, 360) → efeito idêntico
   aqui (mesmo tamanho da tela!); `setOrigin(1, 1)` empurra o desenho para
   fora da tela. Respostas boas descrevem **o que muda na posição do canto**.
3. Assinar a obra: personalização — aumenta o vínculo com o projeto.
4. Cor de fundo: perceber que `main.js` é configuração, não "o jogo".
5. Desafio: `this.add.image(900, 500, 'ceu').setScale(0.5);`

### Aula 02 (Chão)
1. Múltiplos de 128 (o tamanho do tile): `256` fica perfeito; `200` gera a
   faixa de grama "no lugar errado" → **estratégia de ensino de matemática**
   (múltiplos, divisão com resto).
2. O chão flutua porque o centro do retângulo mudou, mas a altura do
   desenho não é a mesma da constante.
3. `tilePositionX = 200` desloca o padrão → antecipa o parallax da aula 03.
4. `setTileScale(2, 2)` deixa o ladrilho maior ("zoom"); `(0.5, 0.5)` menor.
5. Desafio: o segundo chão desenhado **depois** fica na frente (camadas).

### Aula 03 (Cenário Completo)
1–2. Velocidades: aceitar qualquer justificativa ligada a *profundidade*.
3. Sem o update do chão, só ele fica parado (contraste entre "mundo" e fundo).
4. As montanhas claras "sobem" na tela quando aumentamos o Y.
5. `Math.sin` → movimento de vai-e-vem (aceitar como "acelera e freia").

### Aula 04 (Personagem)
1. `frameRate` maior = respiração mais rápida (é a "velocidade do tempo").
2. `start: 1, end: 1` = animação de 1 quadro = boneco congelado.
3. y fixo em `TOPO_CHAO` mantém os pés no chão → causa: o `origin`.
4. `setScale` **não** tira os pés do chão justamente por causa do `origin`
   (0.5, 1). Essa pergunta reforça o conceito central da aula.
5. `repeat: 0` = toca uma vez e para (útil para dano/vitória).

### Aula 05 (Inimigo)
1. Contagem no console (incentiva ler o console!).
2. `frameRate: 12` = gosma "nervosa" (sensação de velocidade).
3. `setScale` + `origin` → pés continuam no chão.
4. Desafio: `criarInimigo(x, y)` com valor padrão
   `criarInimigo(x, y = TOPO_CHAO)` é a resposta mais elegante.
5. Lista: permite N inimigos com o mesmo código (e é o que o Phaser espera
   para `overlap` com vários objetos).

### Aula 06 (Movimento) ⭐
1. `debug: true` → ver as caixas; `setSize(128,128)` faz o Milo colidir
   "no ar" com o chão (caixa maior que o desenho).
2. `FORCA_PULO` -350 = pulinho; -900 = superpulo (pode "furar" plataformas
   se a velocidade for muito alta — excelente gancho para a aula 11).
3. `VEL_ANDAR`: 80 = tartaruga, 500 = corrida insana.
4. Gravidade baixa = pulo flutuante (lua); alta = pulo seco (pedra).
5. "Sempre correndo" = jogo de corrida infinita (lembra o `pong-v2`/jogos do repo).
6. Extra 1 (pulo variável) e Extra 2 (pulo duplo): código pronto no arquivo,
   explicado linha a linha nos comentários.

### Aula 07 (Movimento do Inimigo)
1. `setScale` + velocidade sorteadas por gosma.
2. `VEL_GOSMA_MAX = 300` → injusto/frustrante: falar de **curva de dificuldade**.
3. `setBounce` + gravidade = gosmas quicando (caos divertido).
4. Patrulha por posição: `if (gosma.x > 1000) { velocidade negativa }`.
5. Provar a velocidade: observar duas gosmas se distanciando na tela.

### Aula 08 (Colisão do Personagem)
1. Empurrão forte = mais punitivo; conversar sobre "punição x aprendizado".
2. Sem invencibilidade: levar dano várias vezes por segundo = **injusto**.
   Esse experimento ensina o conceito melhor que qualquer explicação.
3. Tremor: `shake` é *game feel* — pergunte qual valor parece "pesado".
4. Cores do `setTint`.
5. Contador de vidas com `console.log` (prepara a aula 12).

### Aula 09 (Colisão do Inimigo)
1. `+ 50` = pisão generoso (mais fácil); `+ 0` = exigente (mais difícil).
2. `shake` no lugar de `flash`.
3. `frameRate 20` = a poça desaparece rápido.
4. `FORCA_QUIQUE = -600` = comemoração mais alta.
5. Desafio 2: `this.pontos += 100` no `derrotarInimigo`.
6. Pergunta-chave: sem `peAbaixoDoTopo`, qualquer queda ao lado da gosma
   contaria como vitória (pisão "injusto").

### Aula 10 (Objetos em Tela)
1. Item impossível: falar de **acessibilidade** e respeito ao tempo do
   jogador ("itens impossíveis frustram, segredos recompensam").
2. `PONTOS_MOEDA = 1000` → economia do jogo (números "redondos" são lidos melhor).
3. `duration: 250` = flutuação rápida/ansiogênica.
4. Sem tween: a moeda fica parada (e o corpo acompanha — repare!).
5. `criarMoeda(x, y, valor)` = primeiro passo para generalizar código.
6. Corpo dinâmico sem gravidade: porque o corpo **deve acompanhar** o tween.

### Aula 11 (Novas Plataformas)
1. Pulo mais alto "quebra" o level design: excelente discussão sobre **intenção
   do designer** x liberdade do jogador.
2. Plataforma extra: verificar se é alcançável (90 px de altura por degrau).
3. Moeda sobre a estrela: o `overlap` dispara os dois no mesmo quadro;
   ordem definida pela ordem dos `overlap` registrados.
4. Trocar item e mensagem = personalização.
5. Plataforma fantasma: conflito entre **desenho** e **corpo** — grande
   ensinamento sobre "o que o jogador vê x o que o jogo faz".

### Aula 12 (HUD/UI-UX)
1. `VIDAS_INICIAIS = 5` e `TEMPO_INVENCIVEL = 1500` = mais amigável.
2. Recorde com `localStorage`:
   ```js
   const recorde = Number(localStorage.getItem('recorde-milo') || 0);
   if (this.pontos > recorde) localStorage.setItem('recorde-milo', this.pontos);
   ```
3. Vitória: `if (this.estrelaPega && this.inimigosDerrotados === 3) this.vitoria();`
4. Cronômetro: `this.time.addEvent({ delay: 1000, loop: true, callback: () => this.segundos++ })`
5. Botão:
   ```js
   const botao = this.add.rectangle(CENTRO_X, 540, 420, 76, 0x2d6cdf).setDepth(2001)
       .setInteractive({ useHandCursor: true });
   botao.on('pointerdown', () => this.scene.restart());
   ```
6. Personalização livre — é o encerramento da trilha.

---

## 5. Erros mais comuns da turma (e como destravar rápido)

| Sintoma | Causa provável | Como conduzir |
|---|---|---|
| Tela preta | Erro de digitação (falta `;`, vírgula, parêntese) | **F12 → Console**, leia a primeira linha vermelha; mostre que o erro aponta a linha |
| Nada aparece | Abriu o arquivo errado (`src/main.js` em vez de `index.html`) | Ensinar a diferença entre "arquivo que abre" e "arquivo que se edita" |
| Imagem/textura não carrega | Caminho errado no `preload` | `assets/` + nome exato, minúsculas/maiúsculas contam |
| Personagem enterrado/flutuando | `origin` e/ou o Y de referência | Relembrar o truque `setOrigin(0.5, 1)` |
| Não pula | Faltou `estaNoChao`... ou o teclado não está com foco | Clicar uma vez na página do jogo antes de testar |
| Cai para sempre | Faltou `collider` ou o chão físico não é estático | Ler a "Problemas comuns" da aula 06 |
| Animações "tremendo" | Faltou o `true` no `play('x', true)` | Mostrar a diferença com/sem |
| Dano repetido várias vezes | Faltou a trava de invencibilidade | Pergunte: "60 quadros por segundo... quantos danos isso dá?" |
| Pisão não funciona | Faltou a condição dos pés acima, ou a margem é 0 | Ativar `debug: true` e ver as caixas |
| Moeda não é coletada | Corpo estático em objeto com tween | O "segredo importante" da aula 10 |
| Avisos no console repetidos | Recriar animações após `restart` | O `anims.exists()` da aula 12 |

> **Postura recomendada:** nunca entregar a correção pronta. Peça que
> descrevam **o que esperavam** e **o que aconteceu**; quase sempre o próprio
> aluno localiza a linha ao verbalizar.

---

## 6. Avaliação sugerida (rubrica simples)

| Critério | Insuficiente | Bom | Excelente |
|---|---|---|---|
| **Funciona** | o jogo não roda | roda com pequenos erros | roda estável em qualquer navegador |
| **Entende** | copiou sem saber explicar | explica o que cada bloco faz | explica por que escolheu cada número |
| **Modifica** | repetiu o exemplo | mudou valores e testou | criou variações próprias (item, cenário, regra) |
| **Testa e depura** | para no primeiro erro | lê o console e tenta | descreve hipóteses e isola o problema |
| **Colabora** | não participa | ajuda e pede ajuda | ensina colegas / documenta o que aprendeu |

**Evidências para o portfólio:** o jogo personalizado + uma explicação
curta em vídeo (1 min, "tela + voz") explicando **uma** decisão de código.

---

## 7. Culminância e projetos finais (ideias)

1. **Feira de jogos:** cada aluno/jogo num computador, com fichinha "controles"
   e "o que eu mudei". Colegas jogam e deixam bilhetes ("amei o pulo").
2. **Speedrun de personalização:** em 20 minutos, cada dupla deve deixar o
   jogo "irreconhecível" (cores, velocidades, quantidade de inimigos).
3. **Nível novo:** usando a aula 11, criar um nível com 3 caminhos (fácil,
   médio, secreto) e justificar a escolha.
4. **Porta para o reposiório maior:** estudar um jogo de `03-Jogos`
   (ex.: campo minado) e comparar com o que construímos.
5. **Ensinar é aprender:** gravar um mini-tutorial (2 min) de uma tarefa e
   doar para a turma do ano seguinte.

---

## 8. Recursos para continuar

* Documentação oficial do Phaser 3: <https://docs.phaser.io/phaser/getting-started/what-is-phaser>
* Exemplos oficiais (centenas de trechos curtos): <https://labs.phaser.io/>
* Guia de JavaScript para iniciantes (MDN): <https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript>
* Projeto **React + Phaser** (este repositório): pastas `02-Scripts`,
  `03-Jogos`, `04-Sprites`, `06-VFX`, `07-Sounds` e `09-gdd`.
* Glossário rápido para a turma: [GLOSSARIO.md](GLOSSARIO.md)

---

## 9. Sobre a arte e a manutenção do material

* Toda a arte (Milo, gosma, moedas, chão, cenário) foi desenhada
  especificamente para esta trilha, em pixel art, e é livre (licença MIT
  do repositório). Os tamanhos de cada quadro estão documentados no
  `assets/README.md` de cada aula.
* A pasta [ferramentas/](ferramentas/README.md) explica como a arte e os
  testes automáticos das 12 aulas foram feitos — útil se você quiser criar
  aulas novas ou mudar o visual sem quebrar o código.
* Todas as 12 aulas foram **executadas em navegador real** (Chrome headless)
  antes de serem publicadas: carregamento de assets, movimento, colisões,
  coleta, vidas e game over foram verificados automaticamente.
