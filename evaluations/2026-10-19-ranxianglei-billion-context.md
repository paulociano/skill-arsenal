# Avaliação: billion-context (2026-10-19)

- Fonte: https://github.com/ranxianglei/billion-context
- Referência lida: README master, SHA blob `a55026a118f723df1f2f192164f6edd46533ba01`; LICENSE `eba0939b44fcea224b18b508937a133c51a47d21`.
- **Classe D (skill técnica dependente de runtime externo); adoção metodológica parcial B.**
- Decisão: **ADAPT_EXISTING_OWNER**, sem instalar o proxy. Owner: `skills/agent-memory-engineering/SKILL.md`.
- Evidência de implementação: commit https://github.com/paulociano/skill-arsenal/commit/a3bb05a8adff0ca87521a8ec87de4554b45b7dbe
- Mecânica: proxy TypeScript entre agente e API do modelo, compressão incremental/hierárquica com quatro operações: compress, decompress, search_context e acp_status. Suporta múltiplos clientes CLI, mas a implementação não pode interceptar a sessão gerenciada do ChatGPT.
- Valor incremental: distinção entre resumo reversível e memória durável, conservação de provenance do intervalo comprimido, recuperação exata sob demanda, estabilidade de prefix-cache e diagnóstico do orçamento contextual.
- Sobreposição: `agent-memory-engineering` já cobre captura, distilação, retrieval seletivo, histórico/provenance e source of truth; novas skills duplicariam ownership.
- Dependências: Node/npm, pacote externo, proxy HTTP(S), configuração do cliente e API/modelo conforme integração; não são pré-requisitos para a metodologia adaptada.
- Segurança: **CAUTION** no runtime, revisão estática parcial da documentação, sem installer executado nem auditoria integral de código/dependências. Proxy vê prompts e potencialmente credenciais/tráfego; modos MITM, certificados e persistência exigem revisão específica e consentimento. Cache e compressão não garantem fidelidade; medir.
- Claims de desempenho: 5× economia e bilhões de tokens cumulativos por sessão são claims do autor, não testados independentemente nesta avaliação. A licença tem termo adicional de atribuição de produto, portanto não presumir licença MIT pura do conjunto nem copiar kernel sem revisão.
- Resultado: metodologia documentada em owner existente; nenhum runtime instalado; sem benchmark próprio.
