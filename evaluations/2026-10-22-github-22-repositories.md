# Lote de 22 repositórios GitHub — triagem do Arsenal (2026-10-22)

## Escopo e método
Fontes: repositórios originais fornecidos pelo usuário. Fonte de decisão: `ARSENAL INDEX.md` e `stacks/arsenal-autopilot/STACK.md` do branch master. Triagem por metadados e READMEs principais; nenhuma instalação, benchmark independente, auditoria completa do código ou inspeção de binários foi realizada. Classes: A processo comportamental, B metodologia, C baixo valor incremental, D runtime/software externo. As classes descrevem adequação ao Arsenal, não qualidade geral do software.

## Ledger e decisão por projeto

| Fonte | Capacidade observada | Classe | Decisão | Owner / motivo |
|---|---|---|---|---|
| [justrach/nanoui](https://github.com/justrach/nanoui) | GUI desktop em Zig; UI GPU/webview | D | KEEP_EXTERNAL_REFERENCE | engenharia desktop dependente de runtime Zig, sem projeto consumidor |
| [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv) | launcher sem anúncios para smart TV | D | KEEP_EXTERNAL_REFERENCE | aplicativo/dispositivo, não skill ChatGPT; operações ADB exigem consentimento e reversão |
| [obsidianmd/pele](https://github.com/obsidianmd/pele) | Mermaid → SVG via TS e layout responsivo | B/D | UPDATE_EXISTING | `skills/architecture-visualization/SKILL.md` com seleção opcional de renderer |
| [perplexityai/SPACE](https://github.com/perplexityai/SPACE) | execução isolada de agentes em microVMs Firecracker | D | KEEP_EXTERNAL_REFERENCE | infraestrutura Kubernetes/VM; isolamento já previsto em generative-ui-engineering, sem runtime disponível |
| [stackedlol/ascii-sharks](https://github.com/stackedlol/ascii-sharks) | animação ASCII em Canvas | D | KEEP_EXTERNAL_REFERENCE | asset visual específico; sem método generalizável adicional |
| [dominikmartn/harp](https://github.com/dominikmartn/harp) | sidebar de sessões Claude/Codex | B/D | KEEP_EXTERNAL_REFERENCE | UX de agentes, mas ferramenta Mac nativa não portátil |
| [eagle-hq/EAGLE-4](https://github.com/eagle-hq/EAGLE-4) | speculative decoding de LLM | D | KEEP_EXTERNAL_REFERENCE | pesquisa/runtime de inferência, não disponível neste ChatGPT |
| [ELY-Open-Source/ElyOffice](https://github.com/ELY-Open-Source/ElyOffice) | suíte local Rust/GPUI para documentos | D | KEEP_EXTERNAL_REFERENCE | aplicação desktop; sem ganho incremental à produção de artefatos do Arsenal |
| [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | inferência distribuída de modelos DeepSeek | D | KEEP_EXTERNAL_REFERENCE | kernels/hardware/serving específicos; comparação somente em projeto real |
| [interplains/zero-breach](https://github.com/interplains/zero-breach) | scanner local read-only de IOCs de spyware | B/D | KEEP_EXTERNAL_REFERENCE | ferramenta forense especializada; resultado negativo não prova ausência de infecção; não instalar nem varrer sistema |
| [soumatheusgomes/editonny](https://github.com/soumatheusgomes/editonny) | edição de vídeo local por linguagem natural | A/D | UPDATE_EXISTING | `skills/video-editing-pipeline/SKILL.md`: contrato editorial, operações e QA sem dependência de Codex/Claude |
| [Ansub/tv-detox](https://github.com/Ansub/tv-detox) | ADB para TV/launcher simplificado | D | KEEP_EXTERNAL_REFERENCE | potencial alteração de dispositivo; não inferir reversibilidade universal |
| [vercel-labs/fx0](https://github.com/vercel-labs/fx0) | geração de página HTML por agente durável | B/D | KEEP_EXTERNAL_REFERENCE | modelo de sessões/checkpoints já roteado; operação exige Vercel/libfx/serviços reais |
| [wevm/ondine](https://github.com/wevm/ondine) | Mermaid → SVG compilado por Rust/build | B/D | UPDATE_EXISTING | `skills/architecture-visualization/SKILL.md`; contraste build-time vs client-side |
| [InukaAsith/TwinDesk](https://github.com/InukaAsith/TwinDesk) | integração de dispositivos, tela, input, arquivos | D | KEEP_EXTERNAL_REFERENCE | aplicativo com acesso elevado a desktop/clipboard; auditar permissões antes do uso |
| [zilvestro/grammai](https://github.com/zilvestro/grammai) | revisão gramatical offline + IA opcional | B/D | KEEP_EXTERNAL_REFERENCE | extensão externa, tarefa de escrita já coberta, requer CLI para IA |
| [salihcantekin/ruvio](https://github.com/salihcantekin/ruvio) | servidor RESP/Redis em Rust | D | KEEP_EXTERNAL_REFERENCE | decisão de infraestrutura dependente de compatibilidade e benchmarks |
| [MemTensor/MemT-1.0](https://github.com/MemTensor/MemT-1.0) | modelo com memória nativa treinável | D | KEEP_EXTERNAL_REFERENCE | arquitetura/treinamento de modelo; não confundir com memória de agente do ChatGPT |
| [humblemuzzu/dumbtv](https://github.com/humblemuzzu/dumbtv) | ajustes ADB de smart TV | D | KEEP_EXTERNAL_REFERENCE | produto de nicho; ações sobre dispositivos exigem backup e aprovação |
| [solidsf-inc/solidcv](https://github.com/solidsf-inc/solidcv) | CV/visão 3D e otimizações Rust declaradas | D | KEEP_EXTERNAL_REFERENCE | claims de desempenho não reproduzidos; dependência de hardware/projeto |
| [llamaboi55/DragShift](https://github.com/llamaboi55/DragShift) | menu radial de conversão de arquivos | B/D | KEEP_EXTERNAL_REFERENCE | inspiração UX, já coberta; não executar instalador remoto por pipe sem revisão |
| [longbridge/nsh](https://github.com/longbridge/nsh) | UI nativa Rust/TSX multiplataforma com módulos | D | KEEP_EXTERNAL_REFERENCE | framework de app, depende de toolchain e host real |

## Revisão de segurança e portabilidade
- Nenhum shell installer, executável, extensão de navegador, modelo de terceiros ou dependência externa foi executado.
- Zero-breach: evidência negativa tem baixa sensibilidade; manter a distinção entre IOC e comprovação de segurança.
- TV tools: ADB, desativação de apps e alteração de launcher podem causar efeitos de dispositivo; não executar sem confirmação por dispositivo.
- TwinDesk/grammai: clipboard, telas, conteúdo editado e integração de CLI envolvem acesso potencial a dados sensíveis.
- SPACE: sandbox real requer boundary de credenciais, rede e lifecycle, não apenas iframe.
- fx0: custo de inferência, persistência, autenticação e autorização dependem da implantação; um exemplo não prova disponibilidade no ChatGPT.
- DeepInfer/EAGLE/MemT/solidcv: claims de desempenho, compatibilidade e qualidade são dos autores; requerem testes independentes antes de recomendação de produção.

## Mudanças publicadas
- `skills/architecture-visualization/SKILL.md`: adicionada seleção técnica de Pele/Ondine, validação de semântica, compatibilidade e restrições de SVG.
- `skills/video-editing-pipeline/SKILL.md`: absorvida metodologia de edição conversacional inspirada em editonny, sem assumir engine instalada.
- Índice não alterado: nenhum owner novo ou description materialmente diferente.

## Limites
Leitura em nível de README/root, não auditoria de supply chain, threat model detalhado, testes em dispositivos nem benchmarking. Fontes técnicas externas são referências condicionais, não recursos instalados ou garantidos.