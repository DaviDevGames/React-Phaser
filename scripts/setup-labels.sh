#!/usr/bin/env bash
# Cria/atualiza as labels do repositório a partir de .github/labels.yml
# Requisitos: GitHub CLI (`gh`) autenticado (`gh auth login`) e `yq` instalado.
#
# Uso:
#   chmod +x scripts/setup-labels.sh
#   ./scripts/setup-labels.sh davidcreator/React-Phaser

set -euo pipefail

REPO="${1:-davidcreator/React-Phaser}"
LABELS_FILE="$(dirname "$0")/../.github/labels.yml"

if ! command -v gh >/dev/null 2>&1; then
  echo "Erro: GitHub CLI (gh) não encontrado. Instale em https://cli.github.com/" >&2
  exit 1
fi

if ! command -v yq >/dev/null 2>&1; then
  echo "Erro: 'yq' não encontrado. Instale com 'pip install yq' ou 'brew install yq'." >&2
  exit 1
fi

echo "Sincronizando labels em $REPO a partir de $LABELS_FILE ..."

COUNT=$(yq '. | length' "$LABELS_FILE")

for i in $(seq 0 $((COUNT - 1))); do
  NAME=$(yq -r ".[$i].name" "$LABELS_FILE")
  COLOR=$(yq -r ".[$i].color" "$LABELS_FILE")
  DESCRIPTION=$(yq -r ".[$i].description" "$LABELS_FILE")

  if gh label list --repo "$REPO" --limit 200 | grep -qF "$NAME"; then
    echo "Atualizando label: $NAME"
    gh label edit "$NAME" --repo "$REPO" --color "$COLOR" --description "$DESCRIPTION"
  else
    echo "Criando label: $NAME"
    gh label create "$NAME" --repo "$REPO" --color "$COLOR" --description "$DESCRIPTION"
  fi
done

echo "Labels sincronizadas com sucesso!"
