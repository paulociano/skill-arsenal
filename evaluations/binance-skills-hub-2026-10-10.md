# Avaliação: Binance Skills Hub (2026-10-10)

## Escopo e provenance
- Catálogo oficial: https://www.binance.com/en/skills (20 entradas visíveis em 2026-10-10)
- Origem técnica indicada pelo catálogo: https://github.com/binance/binance-skills-hub
- Amostras de SKILL.md lidas no Hub: `query-token-audit`, `binance-wallet-tracker`, `binance-trading-signal` e `academy-skill`.
- Roteamento canônico consultado: `ARSENAL INDEX.md`; método: `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/skill-security-review/SKILL.md`.
- Profundidade: triagem **das 20 entradas** por descrições oficiais; inspeção técnica **amostral** das 4 acima. Não afirmar auditoria completa de cada script, dependência ou repositório. Não houve execução de CLI, instalação ou testes autenticados.

## Decisão
Adotar **uma** competência portátil: `skills/onchain-token-due-diligence/SKILL.md`, inspirada especialmente em `query-token-audit`. Esta é uma metodologia investigativa para dados públicos e evidências verificáveis, **não** implementação da API Binance nem integração instalada. Absorver princípios de monitoramento e sinais apenas como contexto nessa due diligence e em análises financeiras quando apropriado. Não importar carteiras, trading, pagamentos nem copy trading.

## Ledger de 20 candidatas

| Origem | Classe | Ação | Justificativa |
| --- | --- | --- | --- |
| `academy-skill` | B | ABSORB_METHOD_ONLY | Educacao e trilhas; sobrepoe ensino e pesquisa; referencia externa sem nova skill. |
| `binance` | D | KEEP_EXTERNAL_REFERENCE | CLI spot/futuros e auth; ordens e derivativos nao portados. |
| `binance-agentic-wallet` | D | REJECT | Carteira, signing, swaps, permissoes, DeFi e pagamentos; alto impacto e runtime ausente. |
| `binance-leaderboard` | D | KEEP_EXTERNAL_REFERENCE | Score de carteiras e rankings dependem de dados e metodologia Binance; dados observaveis nao implicam habilidade de prever retornos. |
| `binance-onchain-copy-trader` | D | REJECT | Automacao de trades, seguimento de sinais e estrategia autoexecutada sem guardrails auditados. |
| `binance-sports-ai-analyzer` | D | REJECT | Previsoes e mercados de predicao fora do escopo e sem valor incremental demonstrado. |
| `binance-tokenized-securities-info` | D | KEEP_EXTERNAL_REFERENCE | Dados Ondo de ativos tokenizados dependem de API e disponibilidade; pode apoiar analises pontuais. |
| `binance-trading-signal` | D | ABSORB_METHOD_ONLY | Backtest e revisao de sinais com vieses, custo, drawdown e limites; sem API no runtime. |
| `binance-wallet-tracker` | A/D | ABSORB_METHOD_ONLY | Padroes de acumulacao/distribuicao e trilha on-chain uteis, mas monitoramento WebSocket/CLI nao disponivel. |
| `crypto-market-rank` | D | KEEP_EXTERNAL_REFERENCE | Rankings sociais e fluxos dependem de feed mutavel; hype nao equivale a qualidade. |
| `fiat` | D | KEEP_EXTERNAL_REFERENCE | Meios de pagamento/limites dependem de pais e conta; verificar ao vivo quando solicitado. |
| `meme-rush` | D | REJECT | Feeds de lancamentos de alto risco; pouco valor reutilizavel sem infraestrutura e forte viés de promocao. |
| `onchain-pay-open-api` | D | REJECT | Criacao de ordens, pagamentos e envio on-chain exigem integracao, autorizacao e teste. |
| `p2p` | D | KEEP_EXTERNAL_REFERENCE | Anuncios e recursos de conta autenticada; nao importados. |
| `payment-assistant` | D | REJECT | Transferencias e QR para pagamentos, efeitos externos e risco financeiro. |
| `query-address-info` | D | KEEP_EXTERNAL_REFERENCE | Snapshot publico de carteira: util quando fontes atuais estiverem realmente acessiveis. |
| `query-token-audit` | A/D | CREATE_NEW | Checklist especializado de seguranca de token; adaptado sem dependencia de endpoint ou execucao. |
| `query-token-info` | D | KEEP_EXTERNAL_REFERENCE | Metadados e OHLCV exigem API; usar fontes atuais com verificacao de contrato. |
| `square-post` | D | REJECT | Publicacao externa com autenticacao e efeitos de conta; sem ganho para Arsenal. |
| `trading-signal` | D | ABSORB_METHOD_ONLY | Eventos de compra/venda observaveis servem para estudo, nao comprovam alpha nem backtest robusto. |

## Prova de valor incremental
- Owner novo `onchain-token-due-diligence`: avaliação verificável de token/contrato, permissões, honeypot, impostos transacionais, liquidez, saída, distribuição e proveniência; não havia skill especializada no índice.
- Should-trigger: "Audite este token na BSC, contrato 0x..., antes de um swap, apontando red flags e o que ficou sem verificação".
- Near-miss: "Qual o preço do Bitcoin?" (consulta de preço), "Explique staking" (educação) ou "Execute uma ordem" (não é due diligence).
- Aceitação: validar chain + contrato, separar evidência de inferência, apontar campos desconhecidos, citar data e origem, evitar falso selo de segurança e qualquer execução financeira.

## Revisão de segurança (estática e proporcional)
- `query-token-audit`: **CAUTION** na fonte externa; API remota recebe endereço/chain e classificação é snapshot mutável. No método adaptado: **APPROVE** para análise de leitura, sem envio compulsório a endpoints ou execução de código.
- `binance-wallet-tracker` e `binance-trading-signal`: **CAUTION**; `baw` CLI, dependência npm, dados e autenticação; estratégias, WebSocket e possíveis efeitos externos. Nenhuma instalação.
- Carteira, copy-trading, trading, P2P, pagamentos, Square: **CAUTION / não adotadas**, por credenciais, assinatura, permissões, envio de ativos e automação com efeitos irreversíveis. Não se afirma presença de malware: não foi feita inspeção exaustiva do código.
- Sem scanner automatizado nem installer-chain review, pois nenhuma instalação foi realizada. Nenhuma chave, seed, API key ou conta conectada.
- Não replicar regras normativas da Binance como prova universal de segurança. `LOW` não significa seguro e resultado só é válido quando `hasResult` e `isSupported` forem verdadeiros.

## Publicação e limites
Criada a skill `onchain-token-due-diligence` e roteada em `ARSENAL INDEX.md`. Não há promessa de consultar Binance de forma autenticada, monitorar WebSocket, disparar alertas automáticos ou efetuar operações. Nova revisão deve checar diffs e fontes originais se surgir necessidade concreta de APIs.
