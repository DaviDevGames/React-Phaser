# Política de Segurança

## Sobre este projeto

O **React-Phaser** é um repositório educacional com exemplos e jogos
front-end (React + Phaser + Vite). Ele não processa dados de usuários nem
expõe um backend em produção, mas, como qualquer projeto com dependências
npm, pode ser afetado por vulnerabilidades em pacotes de terceiros ou por
código de exemplo que demonstre más práticas sem querer.

## Versões suportadas

Por ser uma trilha de estudos (sem versionamento semântico formal),
oferecemos suporte apenas à branch `main`, que é mantida com as versões
mais recentes das dependências.

| Branch | Suportada |
|---|---|
| `main` | ✅ |
| outras branches/forks | ❌ |

## Como reportar uma vulnerabilidade

**Não abra uma issue pública para vulnerabilidades de segurança.**

Em vez disso:

1. Use a aba **Security > Report a vulnerability** deste repositório
   (GitHub Security Advisories), caso esteja habilitada; ou
2. Envie um e-mail descrevendo o problema para o mantenedor responsável
   (ver perfil [@davidcreator](https://github.com/davidcreator)), incluindo:
   - Descrição da vulnerabilidade e impacto potencial
   - Passos para reproduzir (PoC, se possível)
   - Versão/commit afetado
   - Sugestão de correção, se tiver

### O que esperar

- **Confirmação de recebimento:** em até 5 dias úteis.
- **Avaliação inicial:** em até 10 dias úteis, informando se o reporte foi
  aceito, precisa de mais informação, ou não se aplica.
- **Correção e divulgação:** vulnerabilidades confirmadas serão corrigidas
  prioritariamente; daremos crédito ao reportante (salvo pedido de
  anonimato) quando a correção for publicada.

## Boas práticas já adotadas no repositório

- **Dependabot** habilitado (`.github/dependabot.yml`) para alertas e
  atualizações automáticas de dependências vulneráveis.
- `.gitignore` configurado para nunca versionar `.env`/segredos.
- Recomendamos habilitar, nas configurações do repositório
  (`Settings > Code security`):
  - Dependabot alerts
  - Dependabot security updates
  - Secret scanning
  - Push protection para segredos

## Escopo

Como o conteúdo é majoritariamente didático, pedimos que relatórios de
segurança foquem em:

- Dependências com CVEs conhecidos (`npm audit`)
- Código de exemplo que ensine práticas inseguras de forma explícita
- Scripts de CI/CD (`.github/workflows`) com permissões excessivas ou
  exposição de segredos

Obrigado por ajudar a manter este projeto seguro para quem está aprendendo! 🔐
