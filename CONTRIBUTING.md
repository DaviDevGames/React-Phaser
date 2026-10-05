# Guia de Contribuição

Primeiro, obrigado por querer contribuir com o **React-Phaser**! 🎮 Este
repositório é uma trilha de estudos aberta, então toda ajuda — desde corrigir
um typo até enviar um jogo completo novo — é bem-vinda.

## Índice

- [Código de Conduta](#código-de-conduta)
- [Como posso ajudar?](#como-posso-ajudar)
- [Antes de começar](#antes-de-começar)
- [Fluxo de contribuição](#fluxo-de-contribuição)
- [Padrão de pastas para novos exemplos](#padrão-de-pastas-para-novos-exemplos)
- [Convenção de commits](#convenção-de-commits)
- [Checklist do Pull Request](#checklist-do-pull-request)
- [Dúvidas](#dúvidas)

## Código de Conduta

Ao participar, você concorda em seguir o nosso [Código de Conduta](CODE_OF_CONDUCT.md).

## Como posso ajudar?

| Tipo de contribuição | Onde começar |
|---|---|
| 🐛 Reportar um bug | Abra uma [issue de bug](../../issues/new?template=bug_report.yml) |
| ✨ Sugerir melhoria | Abra uma [issue de melhoria](../../issues/new?template=feature_request.yml) |
| 🎮 Propor novo exemplo/jogo | Abra uma [issue de novo exemplo](../../issues/new?template=novo_exemplo.yml) |
| 📝 Melhorar a documentação | Corrija READMEs, explique conceitos, adicione imagens |
| 🌍 Traduzir conteúdo | Veja a seção [Tradução](#tradução-opcional) |
| 💻 Enviar código | Siga o fluxo abaixo e abra um Pull Request |
| 📌 Ajudar a organizar o backlog | Veja o quadro em [Projects](https://github.com/davidcreator/React-Phaser/projects) |

Issues marcadas com [`good first issue`](../../labels/good%20first%20issue)
são ótimas para quem está começando a contribuir em open source.

## Antes de começar

1. Verifique se já não existe uma issue ou PR aberto sobre o mesmo assunto.
2. Para mudanças grandes (novo jogo, nova categoria de pasta, mudança de
   estrutura), abra uma issue **antes** de começar a codar, para alinhar a
   ideia com os mantenedores.
3. Confirme que tem instalado:
   - Node.js 18+ (recomendado: versão LTS mais recente)
   - npm (vem com o Node.js)
   - Git

## Fluxo de contribuição

```bash
# 1. Faça um fork do repositório e clone o seu fork
git clone https://github.com/SEU-USUARIO/React-Phaser.git
cd React-Phaser

# 2. Crie uma branch descritiva a partir da main
git checkout -b feat/novo-exemplo-plataforma-2d

# 3. Entre na pasta do exemplo que você vai alterar/criar
cd "02-Scripts/.../sua-pasta"
npm install
npm run dev

# 4. Faça suas alterações, teste no navegador (http://localhost:5173)

# 5. Rode o lint antes de commitar
npm run lint

# 6. Volte à raiz, adicione e faça commit das mudanças
cd ../../../..
git add .
git commit -m "feat: adiciona exemplo de plataforma 2D com pulo duplo"

# 7. Envie para o seu fork e abra o Pull Request
git push origin feat/novo-exemplo-plataforma-2d
```

Abra o Pull Request contra a branch `main` deste repositório. O template de
PR vai guiar você pelo checklist necessário.

## Padrão de pastas para novos exemplos

Cada exemplo novo deve seguir a convenção já usada no repositório:

```
NN-nome-descritivo/
├── README.md          # O que o exemplo ensina, como rodar, prints/gifs
├── package.json
├── vite.config.js
├── index.html
├── src/
│   ├── main.jsx
│   ├── App.jsx
│   ├── PhaserGame.jsx
│   └── scenes/ (ou objects/, conforme o padrão da categoria)
└── .gitignore
```

- Use prefixo numérico (`01-`, `02-`...) para manter a ordem didática.
- Nomes de pasta em `kebab-case`, sem acentos.
- O `README.md` do exemplo deve explicar: objetivo, conceitos de
  Phaser/React envolvidos, como rodar (`npm install && npm run dev`) e,
  se possível, um screenshot ou GIF.
- **Nunca** faça commit de `node_modules/`, `dist/` ou outros artefatos de
  build — confira o `.gitignore`.

## Convenção de commits

Usamos mensagens no estilo [Conventional Commits](https://www.conventionalcommits.org/pt-br/):

- `feat:` novo exemplo, jogo ou funcionalidade
- `fix:` correção de bug
- `docs:` mudanças apenas de documentação
- `chore:` manutenção, dependências, configs
- `refactor:` mudança de código que não altera comportamento
- `ci:` mudanças em workflows/automações

Exemplo: `fix: corrige colisão do jogador em 02-Scripts/04-Fisica/09-bouncing-com-colisao`

## Checklist do Pull Request

Antes de marcar o PR como pronto para revisão, confirme que:

- [ ] O exemplo roda sem erros (`npm install && npm run dev`)
- [ ] O lint passa (`npm run lint`)
- [ ] Há um `README.md` explicando o exemplo (para conteúdo novo)
- [ ] Não há arquivos grandes/binários desnecessários (compacte imagens/sprites)
- [ ] A descrição do PR referencia a issue relacionada (`Closes #123`)

## Tradução (opcional)

O conteúdo principal é em português (PT-BR). Se você quiser ajudar a tornar
o repositório acessível a um público internacional, abra uma issue de
melhoria propondo traduzir um README específico para inglês — assim
evitamos duplicar esforço traduzindo tudo de uma vez.

## Dúvidas

Use a aba [Discussions](https://github.com/davidcreator/React-Phaser/discussions)
para perguntas gerais, ou abra uma [issue de dúvida](../../issues/new?template=duvida.yml)
se achar que algo na documentação precisa ser esclarecido.

Obrigado novamente por contribuir! 💙
