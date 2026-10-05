# Plano para o quadro em GitHub Projects

A aba **Projects** ainda não está configurada. Como Projects (v2) é
configurado pela interface do GitHub (não por arquivo), siga este roteiro
para montar um quadro útil para quem for contribuir.

## 1. Criar o Project

1. Vá em `Projects` (no topo do repositório) → **New project**.
2. Escolha o template **Board** (Kanban).
3. Nomeie: `React-Phaser — Trilha de Conteúdo`.

## 2. Colunas sugeridas

| Coluna | Descrição |
|---|---|
| 📥 Backlog | Ideias e issues ainda não priorizadas |
| 🧭 Planejado | Próximo ciclo — já priorizado pelos mantenedores |
| 🚧 Em andamento | Alguém já está trabalhando (issue/PR atribuído) |
| 👀 Em revisão | PR aberto, aguardando review |
| ✅ Concluído | Mesclado/fechado |

## 3. Automação (Workflows do Project)

No menu do Project → **Workflows**, habilite:

- *Item added to project* → status `Backlog`
- *Pull request merged* → status `Concluído`
- *Issue closed* → status `Concluído`
- *Pull request opened* (linked a issue) → status `Em revisão`

## 4. Campos personalizados sugeridos

- `Área`: Documentação / Scripts / Jogos / Sprites-VFX-Sounds / Infraestrutura
- `Dificuldade`: Iniciante / Intermediário / Avançado (bom para sinalizar
  `good first issue` para quem está aprendendo)
- `Categoria numerada`: referência à pasta (00 a 09), para visualizar a
  cobertura da trilha por módulo

## 5. Views recomendadas

- **Por área** (agrupado pelo campo `Área`) — ajuda colaboradores a
  encontrar o que combina com seu interesse (física, sprites, UI/UX...).
- **Por dificuldade** — destaca boas primeiras contribuições.
- **Roadmap (timeline)** — usando milestones abaixo, para enxergar o plano
  de médio prazo.

## 6. Milestones sugeridos (Issues → Milestones)

1. **Fundação da comunidade** — templates, CI, CONTRIBUTING, licença
   (este pacote de melhorias).
2. **Cobertura de exemplos** — completar lacunas em `02-Scripts` (ex.
   tilemaps, áudio espacial, save/load, mobile/touch input).
3. **Jogos de referência** — expandir `03-Jogos` com 2-3 jogos completos
   "showcase" bem documentados (com GIF/demo publicada).
4. **Deploy e demos ao vivo** — publicar builds de exemplo via GitHub
   Pages/Vercel para que qualquer pessoa jogue sem clonar o repositório.
5. **Internacionalização** — versão em inglês do README principal e dos
   READMEs de cada módulo.

## 7. Dica de divulgação

Depois de montado, adicione o link do Project ao `README.md` principal
(seção "Comunidade") para que colaboradores encontrem onde ver o que está
sendo feito.
