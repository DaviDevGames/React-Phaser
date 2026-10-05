# React + Phaser — Trilha de Desenvolvimento de Jogos Web

[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](LICENSE)
[![PRs bem-vindos](https://img.shields.io/badge/PRs-bem--vindos-brightgreen.svg)](CONTRIBUTING.md)
[![CI - Build dos exemplos](https://github.com/davidcreator/React-Phaser/actions/workflows/ci-exemplos.yml/badge.svg)](https://github.com/davidcreator/React-Phaser/actions/workflows/ci-exemplos.yml)
[![Issues abertas](https://img.shields.io/github/issues/davidcreator/React-Phaser.svg)](https://github.com/davidcreator/React-Phaser/issues)
[![Code of Conduct](https://img.shields.io/badge/Código%20de%20Conduta-Contributor%20Covenant-ff69b4.svg)](CODE_OF_CONDUCT.md)

Este repositório organiza uma trilha didática, em português, para criação
de jogos web com **React + Phaser** — do primeiro "hello world" até jogos
completos, passando por física, HUD, sprites, VFX e áudio.

## O que é React + Phaser?

- **React** cuida da estrutura da interface (menus, HUD, organização do projeto).
- **Phaser** cuida do loop do jogo (cenas, física, colisões, animações e input).

Juntos, eles permitem criar jogos web modernos, organizados e fáceis de evoluir.

## 📚 Estrutura de estudo

| Pasta | Descrição | Link |
|---|---|---|
| `00-Ebooks` | Livros essenciais para introdução de lógica e algoritmos. | [Abrir](./00-Ebooks/README.md) |
| `01-Ambiente` | Configuração de ambiente e documentação para iniciar projetos. | [Abrir](./01-Ambiente/README.md) |
| `02-Scripts` | Modelos de scripts para usos comuns dentro de jogos. | [Abrir](./02-Scripts/README.md) |
| `03-Jogos` | Jogos-modelo para prática de desenvolvimento pelos alunos. | [Abrir](./03-Jogos/README.md) |
| `04-Sprites` | Jogos e exemplos usando sprites e animações 2D. | [Abrir](./04-Sprites/README.md) |
| `06-VFX` | Jogos e exemplos com efeitos visuais (VFX). | [Abrir](./06-VFX/README.md) |
| `07-Sounds` | Jogos com efeitos sonoros e músicas (trilha de áudio). | [Abrir](./07-Sounds/README.md) |
| `08-Complementar` | Material extra: cenas, objetos, partículas e ferramentas de sprite. | [Abrir](./08-Complementar/README.md) |
| `09-gdd` | Modelo de Game Design Document (com apoio de IA). | [Abrir](./09-gdd/README.md) |
| `base/`, `pong-v2/` | Projetos Vite "modelo" prontos para começar um jogo do zero. | [base](./base) · [pong-v2](./pong-v2) |

## 🧭 Ordem recomendada

1. Comece por `00-Ebooks`.
2. Configure tudo em `01-Ambiente`.
3. Estude padrões em `02-Scripts`.
4. Pratique com os projetos de `03-Jogos`.
5. Evolua para arte em `04-Sprites`, VFX em `06-VFX` e áudio em `07-Sounds`.
6. Explore material avançado em `08-Complementar` e planeje seu próprio
   jogo com `09-gdd`.

Veja mais detalhes na [Wiki do projeto](https://github.com/davidcreator/React-Phaser/wiki)
(guia de instalação completo, FAQ, solução de problemas e roadmap).

## 🚀 Começando rápido

```bash
git clone https://github.com/davidcreator/React-Phaser.git
cd React-Phaser/base      # ou qualquer outra pasta de exemplo
npm install
npm run dev
```

> Cada pasta de exemplo é um projeto Vite independente, com seu próprio
> `package.json`. Entre na pasta desejada antes de instalar as dependências.

## 🤝 Comunidade e como contribuir

Este projeto cresce com a ajuda da comunidade de quem estuda jogos web!

- 🐛 **Bugs**: abra uma [issue de bug](../../issues/new?template=bug_report.yml)
- ✨ **Sugestões**: abra uma [issue de melhoria](../../issues/new?template=feature_request.yml)
- 🎮 **Novo exemplo/jogo**: abra uma [issue de novo exemplo](../../issues/new?template=novo_exemplo.yml)
- ❓ **Dúvidas**: use as [Discussions](../../discussions) ou uma [issue de dúvida](../../issues/new?template=duvida.yml)
- 📋 **Acompanhe o planejamento**: veja o [quadro de Projects](../../projects) e o [Roadmap](https://github.com/davidcreator/React-Phaser/wiki/Roadmap-do-Projeto)
- 💻 **Pull Requests** são bem-vindos — leia o [guia de contribuição](CONTRIBUTING.md) antes de começar

Leia também nosso [Código de Conduta](CODE_OF_CONDUCT.md) e a
[Política de Segurança](SECURITY.md).

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
