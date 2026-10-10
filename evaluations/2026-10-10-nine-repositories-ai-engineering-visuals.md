# Avaliação de lote — nove repositórios externos

Data: 2026-10-10
Método: `arsenal-autopilot`, índice canônico, README/root das nove fontes, comparação seletiva com owners existentes. Revisão estática parcial; nenhum installer, script ou binário externo executado.

## Fontes e decisões

| Fonte | Classe | Capability real | Owner/decisão |
|---|---|---|---|
| [ThariqS/ai-newtab](https://github.com/ThariqS/ai-newtab) | D | Extensão Chromium que transforma histórico de navegação e até oito páginas autenticadas em homepage personalizada gerada via Anthropic | KEEP_EXTERNAL_REFERENCE; `ai-workspace-operating-cycle` e `dashboard-design` cobrem metodologia; não incorporar leitura de histórico sem consentimento específico |
| [morluto/rea](https://github.com/morluto/rea) | A/D | Engenharia reversa multimodal de apps, sites, JavaScript/Electron e binários com MCP/CLI e ferramentas especializadas | KEEP_EXTERNAL_REFERENCE; `code-understanding-audit` e `computer-use-agent-engineering` cobrem análise disponível, mas não substituem Ghidra/Hopper/IDA |
| [mattpocock/skills](https://github.com/mattpocock/skills) | A/B/D | Catálogo modular de engenharia, debugging, descoberta, review e produtividade | ALREADY_ADOPTED; avaliação canônica `evaluations/2026-09-26-mattpocock-skills.md`; owner `decision-questionnaire` e outros |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | A/D | Diagramas editoriais HTML/SVG, seleção semântica, estilo por tokens e amplo catálogo visual | ALREADY_ADOPTED; `evaluations/2026-10-02-diagram-design-zazencodes-season-3.md`, owner `architecture-visualization` |
| [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) | A | Review SwiftUI com referências seletivas sobre APIs, data flow, acessibilidade, localização, responsividade e performance | KEEP_EXTERNAL_REFERENCE neste lote; avaliar atualização de owner específico SwiftUI apenas com comparação das referências e versão real do SDK; não adotar alegações de plataforma sem confirmação |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | A/D | Ferramenta CLI de review por diff e escopo com LLM, regras e comentários por linha | ALREADY_ADOPTED metodologicamente em `skills/code-review/SKILL.md`; não importar CLI nem assumir resultados de benchmark externos |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | D | Gateway e SDK multi-modelo com autenticação, roteamento, gastos, guardrails e balanceamento | KEEP_EXTERNAL_REFERENCE; infraestrutura de execução, não skill disponível no ChatGPT |
| [storytold/artcraft](https://github.com/storytold/artcraft) | D | Aplicação de produção visual com composição 2D/3D, controle de cena, poses e assets | KEEP_EXTERNAL_REFERENCE; `concept-to-3d-asset` e produção visual cobrem partes metodológicas, sem runtime ArtCraft |
| [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | D | Reconstrução 3D streaming baseada em modelo geométrico, GPU/CUDA/PyTorch | KEEP_EXTERNAL_REFERENCE; técnica interessante, mas requer modelo e hardware, não é skill ChatGPT |

## Valor incremental e ownership

Nenhuma nova capability suficientemente portátil e ainda sem owner foi demonstrada nesta triagem. O trabalho mais promissor para um futuro aprofundamento é SwiftUI (leitura seletiva de referências e regras por deployment target), porém apenas se a capacidade não estiver coberta pelo owner nativo já existente.

As fontes já adotadas não devem ser importadas novamente. `mattpocock/skills`, `diagram-design` e `open-code-review` já têm evidências no Arsenal.

## Segurança e portabilidade

- **CAUTION: ai-newtab.** O README declara envio de resumo do histórico de navegação e HTML de páginas autenticadas à API Anthropic. Acesso a dados pessoais e API key requer consentimento informado e avaliação de privacidade.
- **CAUTION: rea.** Instala CLI/MCP, pode integrar Hopper, Ghidra, IDA e inspecionar apps/binários; uso somente com autorização sobre os alvos.
- **CAUTION: mattpocock, diagram-design, open-code-review.** Plugins, scripts, ferramentas e integrações externas não foram executados nem incorporados como dependência obrigatória.
- **CAUTION: LiteLLM.** Gateway operacional gerencia chaves, logs e tráfego de modelos. Exige revisão própria antes de deploy; nenhuma implantação efetuada.
- **CAUTION: ArtCraft e LingBot-Map.** Runtimes, downloads de modelos, dependências de GPU e execução local não foram validados.
- **APPROVE apenas para referência/metodologia textual de fontes selecionadas**, sujeito a fonte, versão e evidência em cada uso.

Revisão estática limitada aos README/root, duas skills representativas e aos owners selecionados; não é auditoria de segurança integral dos códigos e cadeias de instalação.

## Prova incremental e critério de parada

Should-trigger futuro para SwiftUI: projeto iOS com deployment target conhecido, solicitação explícita de revisão de APIs, fluxo de estado, acessibilidade ou performance.
Near-miss: projeto React Native/Flutter ou pedido genérico de interface web.
Evidência de ganho: achados corretos, localizados, sem sugestões de API indisponível no SDK real.

## Publicação

Este registro é o único acréscimo justificado neste lote. Não criar novas skills/stacks e não modificar o índice, pois nenhum nome nem description canônico foi alterado.
