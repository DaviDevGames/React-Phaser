# Checklist de Saúde da Comunidade (Community Standards / Insights)

O GitHub calcula um "Community Profile" (visível em **Insights > Community
Standards**) com base na presença de alguns arquivos e configurações. Este
checklist mapeia cada item às entregas deste pacote de melhorias e ao que
ainda precisa ser configurado manualmente nas **Settings** do repositório
(isso não pode ser feito por arquivo — precisa de acesso de administrador).

## ✅ Resolvido por arquivos (já incluídos neste pacote)

| Item exigido pelo GitHub | Arquivo |
|---|---|
| Descrição do repositório | Configurar em Settings > About (texto curto) |
| README | `README.md` (atualizado) |
| Código de Conduta | `CODE_OF_CONDUCT.md` |
| Diretrizes de Contribuição | `CONTRIBUTING.md` |
| Licença | `LICENSE` (MIT) |
| Template de Issue | `.github/ISSUE_TEMPLATE/*.yml` |
| Template de Pull Request | `.github/PULL_REQUEST_TEMPLATE.md` |
| Política de Segurança | `SECURITY.md` |
| CODEOWNERS (revisão automática) | `.github/CODEOWNERS` |

## 🛠️ Requer ação manual em Settings (não é arquivo)

Marque ao concluir:

- [ ] **About / Descrição**: adicionar uma frase curta + topics (tags)
  como `phaser`, `react`, `vite`, `gamedev`, `javascript`,
  `game-development`, `educacional`, `portuguese`. Isso melhora muito a
  descoberta do repositório em buscas do GitHub.
- [ ] **Social preview image**: Settings > General > Social preview — uma
  imagem (1280×640px) ajuda o link a ficar atrativo quando compartilhado.
- [ ] **Issues**: confirmar que está habilitado (Settings > General >
  Features).
- [ ] **Discussions**: habilitar (Settings > General > Features) — ótimo
  para dúvidas e perguntas abertas, tira pressão das Issues.
- [ ] **Wiki**: habilitar (Settings > General > Features) e publicar o
  conteúdo de `wiki-drafts/` (veja `GUIA_DE_APLICACAO.md`).
- [ ] **Projects**: criar o quadro conforme `PROJECTS.md`.
- [ ] **Actions**: confirmar que Actions estão habilitadas (Settings >
  Actions > General) para os workflows em `.github/workflows/` rodarem.
- [ ] **Branch protection** na `main` (Settings > Branches):
  - Exigir Pull Request antes de merge
  - Exigir que os checks de CI passem
  - (Opcional) Exigir revisão de pelo menos 1 pessoa
- [ ] **Security**:
  - Settings > Code security > Dependabot alerts: **habilitar**
  - Settings > Code security > Dependabot security updates: **habilitar**
  - Settings > Code security > Secret scanning: **habilitar**
  - Settings > Code security > Push protection: **habilitar**
  - (Opcional) Habilitar "Private vulnerability reporting" para permitir
    reportes via Security > Report a vulnerability
- [ ] **Labels**: rodar `scripts/setup-labels.sh` (ou aplicar
  `.github/labels.yml` manualmente) para padronizar labels.
- [ ] **Sincronizar labels usadas nos templates** (`bug`, `enhancement`,
  `novo-conteudo`, `duvida`, `triagem`, `good first issue`, etc.) — já
  cobertas por `.github/labels.yml`.

## 📊 Como acompanhar o progresso

- `Insights > Community Standards`: mostra uma checklist visual com ✅/❌
  para os itens de arquivo listados acima.
- `Insights > Pulse`: mostra atividade recente (commits, PRs, issues) —
  fica mais interessante conforme a comunidade engaja com os novos
  templates e automações.
- `Insights > Traffic`: visitas e clones — bom indicador de alcance depois
  de melhorar a descrição/topics.
