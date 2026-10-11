# Avaliação: morluto/rea (REA: Reverse Engineer Anything)
Data: 2026-10-11
Fonte: https://github.com/morluto/rea (branch main)
Skill original: https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md
Router oficial: ARSENAL INDEX.md
Stack: evaluate-and-import-skill

## Classificação e decisão
- Classe: **A/D**. Metodologia robusta de investigação orientada por evidências, mas capacidade principal depende de runtime MCP/CLI e analisadores externos.
- Ação: **KEEP_EXTERNAL_REFERENCE + ABSORB_METHOD_ONLY**. Não criar uma skill textual que prometa decompilação sem infraestrutura.
- Owners existentes: `code-understanding-audit`, `behavior-contract-validation`, `computer-use-agent-engineering`, `design-system-extraction`, `software-engineering-cycle`.
- Gatilho de reavaliação: disponibilidade comprovada de REA MCP/CLI e target autorizado, com teste real no host suportado.

## O que faz
REA unifica CLI e MCP para investigação de binários nativos (Hopper/Ghidra/IDA), JavaScript/Electron, .NET, APKs Android (JADX/JDK), websites e capturas HAR, além de casos especializados de firmware, ELF, EVM e crashes. Retorna evidências, referências e incertezas para que um agente investigue e eventualmente reconstrua funcionalidades. Uma skill acompanha o runtime; instalar só o SKILL.md não registra o servidor MCP.

## Método aproveitável
1. Identificar o artefato/versão alvo e autorização.
2. Roteamento por tipo de arquivo, evidência estática versus runtime.
3. Começar por um inventário/resumo e aprofundar somente hipóteses relevantes.
4. Conectar afirmações a proveniência e evidências; diferenciar observação, derivação, inferência e desconhecido.
5. Não confundir reconstrução proposta com comportamento comprovado; testar com casos relevantes.
6. Registrar lacunas/limitações e não alegar cobertura completa sem prova.

## Incrementalidade e overlap
- Revisão comum de source repository continua com `code-understanding-audit`; o próprio REA recomenda não ativar suas ferramentas nesse cenário.
- Observação e contrato de comportamento têm owner em `behavior-contract-validation`.
- Browser/desktop grounding tem owner em `computer-use-agent-engineering` e extração visual em `design-system-extraction`.
- O diferencial novo é de **infraestrutura**: decompiladores e conectores de análise de artefatos fechados. Sem esse runtime disponível, uma nova skill seria uma promessa falsa.
- Não alterar `ARSENAL INDEX.md` porque nenhum trigger ou recurso novo foi publicado.

## Segurança e portabilidade
Veredito: **CAUTION**, avaliação documental limitada, não homologação.
- Setup por `npx rea-agents setup` altera configuração de agentes e registra MCP, com potencial de instalar Hopper após aprovação. Não executar instalador automaticamente.
- CLI e runtime podem ler artefatos locais, processos, navegador, redes/capturas e executar targets sob permissões do usuário. Acesso depende de autorização, isolamento e menor privilégio.
- Node.js/npm e, conforme modalidade, Ghidra/Hopper/IDA, JADX/JDK, browser, adb, pwntools, GDB ou ferramentas firmware podem ser necessários; não são inerentes ao ChatGPT.
- Inspecionar a versão instalada, scripts de instalação, origem, dependências e políticas de armazenamento antes de implantação. Preferir versões pinadas e ambiente isolado.
- Não inferir segurança apenas da licença MIT ou de sinais de popularidade.
- O projeto declara processamento local, mas a política do provedor do modelo utilizado pelo agente permanece separada.
- Respeitar autorização de análise e propriedade intelectual, e não executar aplicações desconhecidas fora de sandbox.

## Limites da validação
Foram lidos README.md, AGENTS.md, .agents/skills/reverse-engineer-anything/SKILL.md e metadados no GitHub em 2026-10-11. Nenhum pacote, script, analisador ou binário do REA foi instalado/executado; não houve auditoria exaustiva das dependências nem teste de segurança em runtime. Nenhum benchmark de precisão de decompilação foi reproduzido.

## Relação com avaliação anterior
`evaluations/2026-10-10-paperclip-rea-iris-eneas-floria.md` tratava do guia externo `47thtechcorner/RayCodes_Rea-AI-Agent-Setup`, particularmente inspeção de UI via CDP. Esta avaliação examina o repositório original `morluto/rea` e sua amplitude nativa, sem duplicar skill.

## Aplicação aprovada em 2026-10-11
Após solicitação explícita de aplicar, a metodologia portável foi incorporada aos owners existentes `code-understanding-audit` e `behavior-contract-validation`: seleção por artefato, investigação resumida/progressiva, ledger com níveis de evidência e testes de reconstrução. Não foi instalado REA nem foi criada uma skill redundante. A classificação A/D e o CAUTION continuam válidos. Ativação de decompilação depende de ferramentas MCP/CLI efetivamente acessíveis e alvo autorizado.

## Fontes
- https://github.com/morluto/rea
- https://github.com/morluto/rea/blob/main/README.md
- https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md
- https://github.com/morluto/rea/blob/main/AGENTS.md
