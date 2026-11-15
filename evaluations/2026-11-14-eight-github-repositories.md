# Avaliação de oito repositórios externos — 2026-11-14

## Escopo e método

Fontes consultadas diretamente no GitHub (branch padrão na data): repositórios e READMEs; arquivos `SKILL.md` de Modern Web Guidance, Line Art Animation e Cracked; índice canônico `ARSENAL INDEX.md` e stacks `arsenal-autopilot` / `evaluate-and-import-skill`; owners existentes de web design, motion, realtime voice e computer use. Revisão de segurança proporcional por leitura estática e análise de dependências. **Nenhum installer, binário ou treino executado; nenhum benchmark externo reproduzido.**

Decisões A (skill com ganho), B (método), C (prompt com pouco ganho), D (runtime/técnica externa). Para candidatos D, referência não equivale a instalação ou capacidade nativa.

| Fonte | Capacidade real | Classe | Decisão | Owner/ação | Dependências e riscos |
|---|---|---|---|---|---|
| [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) | Guias especializados e dados de compatibilidade da plataforma web; busca/recuperação pontual e análise de padrões legados | A/B | **UPDATE_EXISTING** | `skills/web-design-engineer/SKILL.md`: consulta dirigida, Baseline, fallbacks, teste real | CLI `npx` / npm não assumido; evitar `@latest` não pinado e disparos amplos sobre backend. Revisar código/fonte antes de instalar. |
| [ersinkoc/phonebox](https://github.com/ersinkoc/phonebox) | Painel Android local para PC com widgets, telemetria e ações, agent .NET e ADB | D | **KEEP_EXTERNAL_REFERENCE** | Não criar skill: é produto operacional, não novo método de atuação do ChatGPT | USB debugging, APK, agente com privilégios locais, comandos/controle de mídia e acesso a sessões AI. Requer revisão de threat model, pareamento, bind de rede, permissões e supply chain antes de uso. |
| [nishant-Tiwari24/cracked](https://github.com/nishant-Tiwari24/cracked) | Catálogo de preparação para entrevistas técnicas com contraexemplos, pistas graduais, rubricas e testes | A/D | **CREATE_NEW** (núcleo portátil) | `skills/technical-interview-simulation/SKILL.md`; não importar 19 skills nem banco/runner | Dependências de CLI, perfis e arquivos; execução de código de candidato exige isolamento, consentimento e verificação. Dados de perguntas por empresa precisam fonte atual. |
| [JDhruv14/line-art-animation](https://github.com/JDhruv14/line-art-animation) | SVG/TypeScript procedural, marcha com pé plantado, springs, cenas temporais, frame stepping determinístico | A/D | **UPDATE_EXISTING** | `skills/motion-asset-engineering/SKILL.md` | JS/Node 22+, Chrome, ffmpeg para demos/export; não presumir bibliotecas e scripts disponíveis. Distinguir metodologia de código reutilizável e respeitar licença MIT. |
| [HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic) | Rastreamento corporal de humanoides e treino de world model/policy em simulação | D | **KEEP_EXTERNAL_REFERENCE** | `embodied-agent-evaluation` / `game-animation-engineering` já são owners conceituais | Requer GPU/CUDA, `uv`, `mjlab` e repositório auxiliar; treinamento não é capacidade do chat. Não importar modelos/scripts sem reprodução e licença/dependency review. |
| [adventists-ai/sophon-realtime](https://github.com/adventists-ai/sophon-realtime) | Modelos de áudio full-duplex, interrupções, tags expressivas e voice cloning | B/D | **UPDATE_EXISTING** (método) | `skills/realtime-voice-agent-engineering/SKILL.md` | GPU de alta VRAM ou API hospedada/credenciais; áudio/voz sensíveis, consentimento para clonagem, logs. Benchmarks auto-relatados não validados. |
| [OmniJev/Flide](https://github.com/OmniJev/Flide) | Engine para inferência de modelos decision/Jev com state forking e API dedicada | D | **KEEP_EXTERNAL_REFERENCE** | `local-llm-inference-engineering` cobre análise; sem atualizar owner sem benchmark independente | NVIDIA GPU, PyTorch/CUDA e modelos compatíveis. Acelerações de até 9,5× e demais métricas vêm do projeto, não foram reproduzidas; adaptar só sob caso de uso real. |
| [tobi/wrapvm](https://github.com/tobi/wrapvm) | VM/contêiner desktop para agentes com XFCE, Chrome compartilhado, CDP, agent-browser e agent-desktop | D | **KEEP_EXTERNAL_REFERENCE** | `computer-use-agent-engineering` já cobre isolamento e verificação | Container image, smolvm/podman/docker, perfil Chrome, cookies e credenciais expostas via controle remoto/CDP. Autorização por ação e isolamento de rede obrigatórios em contexto sensível. |

## Ledger de ganho incremental

- **Browser native-first**: ganho sobre `web-design-engineer` foi tornar obrigatória a verificação dirigida de maturidade Baseline/compatibilidade quando APIs novas são propostas, sem forçar uso de CLI ou tokenizar indiscriminadamente 250 guias. Should-trigger: popover com Safari; near-miss: migração de banco de dados. Prova esperada: browser matrix e fallback testados.
- **Ilustração SVG animada**: ganho sobre `motion-asset-engineering` foi modelagem de passada/apoio, validação com tempo fixo e tratamento do ciclo dia-noite. Should-trigger: cena vetorial viva; near-miss: simples animação de assinatura/stroke. Prova esperada: frames e integração acessível.
- **Interview candidate practice**: novo contrato que não estava coberto por `hiring-process`, focado em candidato e não recrutador. Should-trigger: simulação de entrevista de código; near-miss: entrevista de descoberta. Prova esperada: contraprova, rubrica evidenciada e testes executados ou ressalva.
- **Duplex voice**: não criar owner novo; detalhar cancellation, segmentação de áudio e marca expressiva em owner já existente. Should-trigger: agente full-duplex; near-miss: transcrição offline. Prova esperada: interrupções e métricas end-to-end.

## Segurança/portabilidade

**Veredito para incorporações metodológicas: CAUTION / static_only.** Não foram encontrados motivos para executar instaladores; os trechos incorporados são instruções adaptadas, não scripts ou permissões importadas. Isso **não** certifica os projetos originais como seguros. Para cada fonte com runtime local ou remoto, exigir auditoria de versão, cadeia de instalação/dependências, tratamento de credenciais, acesso de rede, writes locais, permissões e autenticação antes de produção. Não rodar `curl | sh`, `npx @latest`, imagens de contêiner ou APKs para simples avaliação.

Projetos com voz clonada: consentimento e anti-personificação. Projetos que executam código: sandboxing. VM/browser com CDP: cookies, credenciais, bind, isolamento e acesso remoto. Hardware/modelos: requisitos não equivalem a capacidades da sessão.

## Publicação

- `skills/web-design-engineer/SKILL.md` — UPDATE_EXISTING, guidance web.
- `skills/motion-asset-engineering/SKILL.md` — UPDATE_EXISTING, SVG procedural.
- `skills/realtime-voice-agent-engineering/SKILL.md` — UPDATE_EXISTING, voice duplex.
- `skills/technical-interview-simulation/SKILL.md` — CREATE_NEW.
- `ARSENAL INDEX.md` — novo owner roteado.
- Este registro `evaluations/2026-11-14-eight-github-repositories.md`.

Aprovação é de **metodologia portátil** em modo `static_only`; não há `behavior_verified` nem testes completos de runtime. Nenhum pacote externo foi instalado ou utilizado como serviço. Verificar no GitHub branch `master` os arquivos finais após commit.
