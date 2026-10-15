# Avaliação — PromtEngineer/software-factory

Data: 2026-10-15

Fonte: https://github.com/PromtEngineer/software-factory

## Resultado
**Classe A/D**: metodologia efetiva e runtime técnico específico.
**Decisão UPDATE_EXISTING**: `skills/software-factory-operations/SKILL.md`.
**Owner existente**: skill no Arsenal já cobre charter, fila, triagem, claims atômicos, writer/verifier, checks, revisão humana e back-pressure. Não criar outra skill ou stack.

## O que a fonte faz
Orquestra GitHub issues em etapas isoladas em Upstash Box com agentes Claude Code: claim, triage, implementação, testes de verifier, review e PR para merge humano. Passagem de estado por JSON com schemas Zod. O integrador usa branch separada para conflitos; hidden tests procuram falhas não expostas ao writer. O projeto dispõe de backend local para demonstração.

## Valor incremental adotado
- Isolamento e snapshot por lane com base commit explícito;
- contrato tipado por unidade, transições verificáveis, falha de schema bloqueante;
- verifier em checkout limpo e holdout não visto pelo writer;
- integração sequencial de PRs como gate separado, testes após cada merge;
- custo e desempenho incluindo conflitos, retrabalho e review debt;
- credenciais mínimas, egress restrito e limites de orçamento.

## Dados e evidências
README declara experimento em 2026-10-05 de 10 issues, 9 PRs, 9/9 testes ocultos e 7/9 branches inicialmente conflitantes ao integrar. Tais números são **declarações do autor**; não reproduzidos independentemente.

## Segurança e portabilidade
**CAUTION** para executar: exige Node, Claude Code, Upstash Box, GitHub CLI/token, Context7 opcional e custos de infraestrutura. Superfícies: credenciais, agentes com execução de shell, rede externa, dependências npm, escrita no GitHub, resolução de conflitos e testes executáveis. Não executar código de terceiros para avaliar. Apenas README, package.json e estrutura descrita foram examinados; não houve auditoria exaustiva de `src/`, dependency tree nem scanner. Não assumir Upstash/Claude Code/Context7 disponíveis no ChatGPT.

**Should-trigger:** operar fila contínua de issues com writers paralelos, verifier isolado e merge humano.
**Near-miss:** corrigir um único bug simples num projeto pequeno.
**Acceptance:** documentos de charter e handoff, checks observados, integração com suite completa e declaração transparente dos componentes realmente executados.

## Alterações
Atualizada a skill existente. Índice permanece igual porque nome e description continuam apropriados. Sem nova stack. Verificar arquivos publicados após a escrita.
