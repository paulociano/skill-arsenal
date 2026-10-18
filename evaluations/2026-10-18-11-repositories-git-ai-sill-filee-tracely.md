# Avaliação em lote: onze repositórios GitHub (2026-10-18)

## Escopo e método
Fontes: READMEs e metadados das branches default indicadas abaixo, consultados em 2026-10-18. Router: `ARSENAL INDEX.md`; stack: `stacks/arsenal-autopilot/STACK.md`. Comparação com owners canônicos já existentes. Revisão de risco estática e proporcional: **não** houve clone, instalação, execução, teste de runtime, auditoria integral de código nem certificação de segurança.

## Matriz de decisão

| Fonte | Classe | Capacidades e dependências | Ownership, decisão e estado |
| --- | --- | --- | --- |
| [feder-cr/git-ai](https://github.com/feder-cr/git-ai) | A/D | Git para muitos agentes, CAS de referências, logs de changesets, resolução de conflitos; Go, servidor gRPC, banco e object storage | UPDATE_EXISTING: `skills/coding-agent-engineering/SKILL.md`. Incorporados critérios de concorrência, segurança, revisão e testes do commit publicado. Sem executar Graft. |
| [Saffsanity/sill](https://github.com/Saffsanity/sill) | D | Captura/controle remoto Mac→iPhone/iPad; macOS, iOS, ScreenCaptureKit, TLS, permissões de tela/acessibilidade | KEEP_EXTERNAL_REFERENCE: aplicativo independente, não capacidade nativa do ChatGPT; requer hardware e consentimento. |
| [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | D | Conversor offline por interface/CLI para muitos formatos; .NET e motores opcionais externos (FFmpeg, Pandoc, LibreOffice etc.) | KEEP_EXTERNAL_REFERENCE: utilitário não justifica skill duplicada de conversão; verificações de binários, instalação e licença são necessárias antes de uso. |
| [jwuthri-cloud/Tracely-ai](https://github.com/jwuthri-cloud/Tracely-ai) | A/D | Traces→clusters→fixtures→replay→CI gate→alertas; OTLP, API, bases e infraestrutura próprias | UPDATE_EXISTING: `skills/llm-observability-evaluation/SKILL.md`, com fail-to-pass, replay hermético, calibração de judge e privacidade. |
| [aixisstudio/Snitch](https://github.com/aixisstudio/Snitch) | D | Monitoramento local de tráfego; captura libpcap/Npcap, Python, FastAPI, Electron, permissões elevadas | KEEP_EXTERNAL_REFERENCE: investigação pontual de rede, não ferramenta disponível nativamente; requer validação antes de coleta sensível. |
| [nekohasekai/open-screen-sharing](https://github.com/nekohasekai/open-screen-sharing) | D | Cliente/servidor de compartilhamento Apple VNC, RDP; iOS/macOS, APIs privadas e recurso de sideload/exploit indicado | KEEP_EXTERNAL_REFERENCE: alto acoplamento à plataforma e riscos de permissões; não importar rotinas de exploit. |
| [Noniv/web-ocean](https://github.com/Noniv/web-ocean) | A/D | FFT multiescala, oceano WGSL/WebGPU, nuvens, sky shading, otimização de GPU; hardware e navegador compatíveis | UPDATE_EXISTING: `skills/shader-graphics-engineering/SKILL.md` com pipeline gradual e QA. |
| [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | A/D | Descrição, medidas e comparação perceptual, geração de SFX por código; Python, modelos CPU, bancos de referência, MCP opcional | UPDATE_EXISTING: `skills/game-audio-engineering/SKILL.md`. Sem instalar modelos nem alegar escuta. |
| [rohit267/net-merge](https://github.com/rohit267/net-merge) | D | Balanceamento por conexão em múltiplos adaptadores; TUN/Wintun e privilégios de rede | KEEP_EXTERNAL_REFERENCE: efeito de sistema e potencial interferência na conectividade; não usar install scripts não auditados. |
| [aicodeking/leanrea](https://github.com/aicodeking/leanrea) | A | Skill leve para investigar executáveis com ferramentas CLI locais; vários decompiladores/CLIs dependem de instalação | UPDATE_EXISTING: `skills/code-understanding-audit/SKILL.md`, incluindo roteamento por magic bytes, consultas seletivas, proveniência e limites da análise estática. Os benchmarks do autor não são evidência de ganho neste ambiente. |
| [Gathin23/tv-vibehack](https://github.com/Gathin23/tv-vibehack) | D | Debloat e launcher Android TV, ADB e scripts de disable/restore, build Android | KEEP_EXTERNAL_REFERENCE: potencial perda de recursos e alterações em dispositivo, exigindo hardware, aprovação e restauração testada. |

## Segurança, portabilidade e limites

- Apps de rede/tela/dispositivo podem exigir permissões privilegiadas, alterar configurações, acessar dados sensíveis ou abrir superfícies de administração; nenhum installer ou binário foi executado.
- `Tracely-ai` pode armazenar dados de produção, prompts e tool outputs: somente traces autorizados, redigidos e com política de retenção podem alimentar evals.
- `git-ai` traz infraestrutura própria. A skill atualizada usa somente critérios portáveis; GitHub connector não fornece servidor Graft.
- `earshot` requer modelos/toolchain ausentes por padrão; avaliações de áudio não foram realizadas.
- `leanrea` contém comandos com ferramentas de análise potencialmente perigosas. Somente alvos autorizados e inspeção estática prioritária; nada foi executado.
- `web-ocean` fornece referência técnica, não benchmark transferível ou shaders já verificados para outro app.
- Nenhuma fonte foi classificada como malware. CAUTION para adoção operacional de todas as ferramentas D até revisão completa de código/instalador e avaliação das permissões.

## Alterações publicadas

- `skills/code-understanding-audit/SKILL.md` — https://github.com/paulociano/skill-arsenal/commit/fe83a6d1e507f274c8ace888cc1cb393332997cf
- `skills/llm-observability-evaluation/SKILL.md` — https://github.com/paulociano/skill-arsenal/commit/6c4e12222a4dd10358079016dcd407a6750fb46b
- `skills/game-audio-engineering/SKILL.md` — https://github.com/paulociano/skill-arsenal/commit/235aa6990d86c5868c3d89de6ca0fc0d386fac86
- `skills/shader-graphics-engineering/SKILL.md` — https://github.com/paulociano/skill-arsenal/commit/ec66457afb8685f71bdc6abc189c2fe1c9abe5e8
- `skills/coding-agent-engineering/SKILL.md` — https://github.com/paulociano/skill-arsenal/commit/a2a94e8f3a207b750dc348d3d4e7d32c03fdabad

Não foram criados novos owners nem alterado o router, já que as cinco melhorias são absorções em skills canônicas previamente indexadas. Referências externas não foram instaladas.
