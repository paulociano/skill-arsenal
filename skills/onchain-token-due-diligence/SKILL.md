---
name: onchain-token-due-diligence
description: Avaliar riscos de tokens e contratos cripto por evidências on-chain, liquidez, permissões, concentração e possibilidade de saída, sem confundir auditoria automatizada com segurança garantida ou executar trades.
---

# On-chain Token Due Diligence

## Quando usar
Quando o usuário pede auditoria de risco de token, suspeita de honeypot ou rug pull, análise de contrato, concentração de carteiras, tributação de compra/venda embutida no token, liquidez ou sinais on-chain de fraude. Não acionar para preço isolado de BTC/ETH, educação cripto geral ou recomendação de compra.

## Fontes e capacidade
- Confirmar **rede + endereço do contrato**, não confiar apenas no ticker. Se faltar informação essencial, pedir somente a necessária; não escolher automaticamente tokens homônimos.
- Consultar fontes atuais verificáveis (exploradores, documentação do projeto, dados de pools, auditorias publicadas, ferramentas de análise quando realmente acessíveis). A Binance Web3 Token Security Audit é uma fonte possível, **não uma integração garantida**.
- Quando houver conector/API efetivamente disponível, usar seu contrato documentado e citar a origem e instante; nunca dizer que executou scanner ou auditoria de bytecode se apenas leu uma página.
- Contratos proxy, permissões administrativas, cadeia de upgrades, owner, mint/burn/blacklist/pause, honeypot, restrições de venda, buy/sell taxes, lockers, liquidez, volume verificável, concentração e fluxos entre carteiras são dimensões candidatas, não campos presumidamente disponíveis.

## Procedimento
1. **Identificação:** rede, contrato exato, decimal e metadados, links oficiais com confirmação cruzada e risco de spoofing.
2. **Contrato:** código verificado? proxy/upgrade? owner/multisig? funções que podem bloquear vendas, alterar taxas, emitir tokens ou retirar ativos? Registre apenas o que pode comprovar.
3. **Negociabilidade:** pools/DEX, liquidez e profundidade, spread, slippage estimado, concentração de LP, taxas efetivas e evidência de venda realizável. Sem teste observável, classificar possibilidade de saída como desconhecida.
4. **Distribuição e comportamento:** holders, concentração, carteiras relacionadas, sinais de manipulação, liquidez adicionada/removida e transações relevantes, com janela temporal e limitações da atribuição de endereços.
5. **Triangulação:** distinguir dados diretamente observados, classificações de scanners de terceiros, alegações do projeto e inferências. Registrar divergências entre fontes.
6. **Síntese:** risco por dimensão, achados críticos, fontes, hora do snapshot, campos não verificados e ações de verificação humana. **Não emitir selo de segurança.**

## Interpretação de auditorias Binance
A fonte `query-token-audit` documenta `hasResult`, `isSupported`, `riskLevel`, `riskLevelEnum`, `riskItems`, `extraInfo.buyTax/sellTax/isVerified`. Interpretar risco **somente** quando `hasResult=true` e `isSupported=true`; caso contrário informar ausência de resultado válido. `LOW` não significa seguro. Taxas e níveis são sinais de triagem da fonte, não laudo independente. A API e formatos podem mudar: validar versão/documentação vigente antes de implementar qualquer cliente.

## Riscos e limites
- Nenhum dado de chave privada, seed ou assinatura deve ser solicitado para análise.
- Não instalar CLI, executar transações, conectar carteiras, conceder allowance ou assinar mensagens como requisito de due diligence.
- Não transformar atividades de smart money/copy trading em recomendação automática; backtests podem ter viés de seleção e custos omitidos.
- Se fonte/chain/token não tiver suporte, marque `não verificado` em vez de extrapolar.
- Alto risco no contrato ou saída bloqueada requer destaque explícito; ausência de alertas não elimina risco.
- Análise é informativa, não garantia de segurança nem aconselhamento financeiro personalizado.

## Output
Resumo de identificação e data; tabela das dimensões (evidência, fonte, estado: confirmado / alerta / não verificado); red flags relevantes; limitações; próximos passos seguros. Uma conclusão pode indicar **evidência insuficiente**, jamais segurança absoluta.

## Provenance
Metodologia adaptada da `query-token-audit` e da triagem do Binance Skills Hub (acesso em 2026-10-10):
- https://www.binance.com/en/skills
- https://www.binance.com/en/skills/detail/binance-web3/query-token-audit
- https://github.com/binance/binance-skills-hub
Dependências `baw`/`binance-cli` e endpoints de execução não foram importados.
