# Guia de Aplicação das Melhorias

Este documento explica **passo a passo** como levar tudo o que foi
preparado neste pacote para o repositório real
`github.com/davidcreator/React-Phaser`. Nada aqui foi enviado
automaticamente para o GitHub — você (como dono/colaborador) precisa
aplicar, revisar e fazer commit/push.

## 📦 O que foi criado

```
LICENSE                              # Licença MIT
README.md                            # Atualizado: links corrigidos + seções novas
CONTRIBUTING.md                      # Guia de contribuição
CODE_OF_CONDUCT.md                   # Código de conduta (Contributor Covenant PT-BR)
SECURITY.md                          # Política de segurança
PROJECTS.md                          # Plano para o quadro em GitHub Projects
HEALTH_CHECKLIST.md                  # Checklist de "Community Standards" / Insights
GUIA_DE_APLICACAO.md                 # Este arquivo

.github/
├── CODEOWNERS
├── PULL_REQUEST_TEMPLATE.md
├── dependabot.yml
├── labels.yml                       # Definição de labels
├── labeler-paths.yml                # Regras do actions/labeler
├── mlc_config.json                  # Config do markdown-link-check
├── ISSUE_TEMPLATE/
│   ├── config.yml
│   ├── bug_report.yml
│   ├── feature_request.yml
│   ├── novo_exemplo.yml
│   └── duvida.yml
└── workflows/
    ├── ci-exemplos.yml              # Builda só os exemplos alterados no PR
    ├── markdown-link-check.yml      # Checa links quebrados nos .md
    ├── stale.yml                    # Fecha issues/PRs inativos
    └── labeler.yml                  # Rotula PRs automaticamente

scripts/
└── setup-labels.sh                  # Cria/sincroniza labels via GitHub CLI

wiki-drafts/                         # Conteúdo pronto para a Wiki (ver seção 4)
├── Home.md
├── Guia-de-Instalacao.md
├── Estrutura-do-Repositorio.md
├── FAQ.md
├── Solucao-de-Problemas.md
├── Recursos-Externos.md
└── Roadmap.md

08-Complementar/README.md            # Faltava — criado
09-gdd/README.md                     # Faltava — criado
```

**Correção importante**: a tabela de pastas no `README.md` original tinha
links quebrados (usava `00 - Ebooks` com espaços e numeração desatualizada,
mas as pastas reais são `00-Ebooks`, `04-Sprites`, etc.). Isso já foi
corrigido.

## 1. Aplicar os arquivos no seu repositório

### Opção A — copiar manualmente

1. Baixe/zipe esta pasta de trabalho.
2. Copie cada arquivo/pasta acima para a raiz do seu clone local de
   `React-Phaser` (mantendo os caminhos, ex. `.github/workflows/...`).
3. Rode `git status` para conferir o que mudou.
4. `git add -A && git commit -m "chore: adiciona templates, CI, docs de comunidade e corrige links do README"`
5. `git push`

### Opção B — usando o diff desta sessão

Se preferir, posso gerar um `.zip` com exatamente os arquivos novos/alterados
para facilitar o download — é só pedir.

> Recomendação: aplique essas mudanças em uma branch (ex.
> `chore/community-health`) e abra um Pull Request para `main`, já testando
> na prática o fluxo descrito em `CONTRIBUTING.md` e o novo template de PR.

## 2. Issues e Pull Requests

Depois do push, confira:

- Abra `Issues > New issue` — os 4 formulários (bug, melhoria, novo
  exemplo, dúvida) devem aparecer como opções, e "issue em branco" deve
  estar desabilitado (`blank_issues_enabled: false`).
- Abra um PR de teste — o checklist do `PULL_REQUEST_TEMPLATE.md` deve
  aparecer automaticamente na descrição.
- Rode `scripts/setup-labels.sh davidcreator/React-Phaser` (requer
  [GitHub CLI](https://cli.github.com/) autenticado e `yq`) para criar as
  labels usadas pelos templates (`bug`, `enhancement`, `novo-conteudo`,
  `duvida`, `triagem`, etc.). Sem isso, o GitHub ainda cria a issue, só não
  aplica a label automaticamente até ela existir.

## 3. Actions

1. Em **Settings > Actions > General**, confirme que "Allow all actions and
   reusable workflows" está habilitado (ou ao menos as actions usadas:
   `actions/checkout`, `actions/setup-node`, `actions/stale`,
   `actions/labeler`, `gaurav-nelson/github-action-markdown-link-check`).
2. Os workflows rodam automaticamente a partir do próximo push/PR:
   - `ci-exemplos.yml`: builda apenas os exemplos cujas pastas mudaram.
   - `markdown-link-check.yml`: roda em PRs que tocam `.md` e semanalmente.
   - `stale.yml`: roda diariamente, marca inatividade após 45 dias.
   - `labeler.yml`: rotula PRs conforme os caminhos alterados.
3. Opcional: adicione `ci-exemplos` como **check obrigatório** em Branch
   Protection (ver seção 6).

## 4. Publicando a Wiki

A Wiki do GitHub é, na verdade, **outro repositório git**
(`React-Phaser.wiki.git`). Para publicar o conteúdo de `wiki-drafts/`:

1. No GitHub, vá em **Settings > General > Features** e habilite **Wikis**.
2. Acesse a aba **Wiki** do repositório e clique em "Create the first page"
   (isso inicializa o repositório da wiki).
3. Clone o repositório da wiki localmente:
   ```bash
   git clone https://github.com/davidcreator/React-Phaser.wiki.git
   cd React-Phaser.wiki
   ```
4. Copie os arquivos de `wiki-drafts/` renomeando conforme o título da
   página (o nome do arquivo vira o título, trocando `-` por espaço):
   ```bash
   cp ../React-Phaser/wiki-drafts/Home.md ./Home.md
   cp ../React-Phaser/wiki-drafts/Guia-de-Instalacao.md "./Guia de Instalação e Primeiros Passos.md"
   cp ../React-Phaser/wiki-drafts/Estrutura-do-Repositorio.md "./Estrutura do Repositório.md"
   cp ../React-Phaser/wiki-drafts/FAQ.md "./Perguntas Frequentes (FAQ).md"
   cp ../React-Phaser/wiki-drafts/Solucao-de-Problemas.md "./Solução de Problemas Comuns.md"
   cp ../React-Phaser/wiki-drafts/Recursos-Externos.md "./Recursos Externos.md"
   cp ../React-Phaser/wiki-drafts/Roadmap.md "./Roadmap do Projeto.md"
   ```
5. Ajuste os links internos `[[Nome da Página]]` em `Home.md` se os títulos
   finais forem diferentes dos sugeridos.
6. `git add -A && git commit -m "docs: publica conteúdo inicial da wiki" && git push`

## 5. Projects

Siga o roteiro detalhado em [`PROJECTS.md`](PROJECTS.md) — criação do
quadro, colunas, automações e milestones sugeridos. Isso é feito pela
interface do GitHub (Projects v2 não é configurado por arquivo).

## 6. Security

1. **Settings > Code security**:
   - Habilite *Dependabot alerts*
   - Habilite *Dependabot security updates*
   - Habilite *Secret scanning* (+ *Push protection*)
   - Opcional: habilite *Private vulnerability reporting* (ativa o botão
     "Report a vulnerability" referenciado no `SECURITY.md`)
2. O `.github/dependabot.yml` já cobre as dezenas de subprojetos via
   `directories` com glob — o Dependabot deve começar a abrir PRs de
   atualização conforme o cronograma mensal definido.

## 7. Branch protection (recomendado)

Em **Settings > Branches > Add branch protection rule** para `main`:

- Exigir Pull Request antes de merge
- Exigir que os checks `ci-exemplos` / `markdown-link-check` passem
- (Opcional) Exigir 1 aprovação de revisão

## 8. Insights / Community Standards

Depois de aplicar os passos 1–7, confira **Insights > Community Standards**
— a lista de requisitos deve ficar toda marcada com ✅. Veja o detalhamento
completo em [`HEALTH_CHECKLIST.md`](HEALTH_CHECKLIST.md), incluindo os
itens de **About** (descrição + topics) e **Social preview** que também
ajudam na descoberta do repositório mas não aparecem nesse checklist
automático.

## 9. Topics sugeridos para o About

`phaser` `react` `vite` `javascript` `gamedev` `game-development`
`html5-games` `educacional` `portuguese-br` `tutorial`

---

Qualquer dúvida sobre algum desses passos, é só perguntar — posso detalhar
ainda mais qualquer seção ou gerar variações dos arquivos (ex. versão em
inglês dos templates).
