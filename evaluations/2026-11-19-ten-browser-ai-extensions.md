# Avaliação de dez projetos de navegador e IA (2026-11-19)

## Escopo e método
Fontes: READMEs da branch padrão de dez repositórios externos, lidos por GitHub connector em 2026-11-19. Router canônico: `ARSENAL INDEX.md`. Workflow: `stacks/arsenal-autopilot/STACK.md`, `stacks/evaluate-and-import-skill/STACK.md`, `skills/skill-security-review/SKILL.md`. Comparados os owners `secure-code-privacy-review`, `computer-use-agent-engineering`, `design-system-extraction` e `web-extraction-pipeline`. O escopo foi **triagem estática de README**, não inspeção exaustiva de código, dependências, builds ou tráfego. Nenhum instalador foi executado. Portanto, **todos os vereditos de segurança são CAUTION / static_only**, isto não é evidência de comportamento seguro ou ausência de vulnerabilidades.

## Capability ledger e decisões

| Repositório | Capacidade confirmada no README | Classe | Decisão e owner | Dependências/risco |
|---|---|---|---|---|
| [sgasser/pasteguard](https://github.com/sgasser/pasteguard) | Proxy local pré-provedor com mascaramento PII/secrets, placeholders, restauração e opção de roteamento a modelo local | A/D | **UPDATE_EXISTING**: `skills/secure-code-privacy-review/SKILL.md`, método de boundary, testes e logs | Bun/Hono, GLiNER, Docker, proxy, storage, extensão; falso negativo, reversão de placeholders, logs, Docker :latest |
| [urzeye/ophel](https://github.com/urzeye/ophel) | Navegação por outline, pastas/tags de chats, exportação e biblioteca de prompts | D | **KEEP_EXTERNAL_REFERENCE**; interface de organização, sem novo owner incremental | Extensão, permissões de leitura de conversas, sync e adaptadores atualizáveis; licença GPLv3 declarada |
| [AI-Prompt-Genius/AI-Prompt-Genius](https://github.com/AI-Prompt-Genius/AI-Prompt-Genius) | Biblioteca e curadoria de prompts com extensão Chrome | D | **KEEP_EXTERNAL_REFERENCE**; recursos já cobertos por gestão de conhecimento/prompting | Extensão e sincronização via Google; README declara CC BY-NC-SA 4.0, evitar cópia de código/conteúdo |
| [kizuna-ai-lab/sokuji](https://github.com/kizuna-ai-lab/sokuji) | Tradução bidirecional de fala em tempo real, local (WASM/WebGPU) ou por nuvem | D | **KEEP_EXTERNAL_REFERENCE**; aplicativo especializado, não skill portátil | Captura de microfone/áudio, APIs, modelos locais, PostHog mesmo em modo local segundo README; AGPL-3.0 |
| [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | Agente browser com modos Ask/Act/Dev, modelos locais/nuvem, workflows, aprovações e watches | A/D | **UPDATE_EXISTING**: `skills/computer-use-agent-engineering/SKILL.md`, replay e gates | Permissões de abas e credenciais, ações com efeitos, provedores externos, agendamento dependente do runtime; GPL-3.0-or-later |
| [A9T9/RPA](https://github.com/A9T9/RPA) | Macros de navegador/desktop, OCR/visão e ponte MCP para criar/reproduzir macros | A/D | **UPDATE_EXISTING**: `skills/computer-use-agent-engineering/SKILL.md`, captura→macro→replay | Extensão, XModules nativos opcionais, instalador npx da ponte MCP não executado, controle da máquina |
| [Player-YN/BrowserKitten](https://github.com/Player-YN/BrowserKitten) | Agente no side panel, sessão local, workspace, execução por modelo separado, follow-up local | D | **UPDATE_EXISTING**: `skills/computer-use-agent-engineering/SKILL.md` para limites/estado de follow-up; sem importar app | Chrome em execução, provedores configurados, permissões de página, tarefas locais, chave e custo BYOK; MIT |
| [AhmadHassan-BTed/ScrollToPrompt](https://github.com/AhmadHassan-BTed/ScrollToPrompt) | Marcadores/minimapa de prompts em chats com adapters e Shadow DOM | D | **KEEP_EXTERNAL_REFERENCE**; conveniência de UI, não nova skill | Extensão Chrome, mutações DOM, mudanças do site; MIT |
| [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | Extração visual e geração de DESIGN.md/SKILL.md de site ativo | B/D | **KEEP_EXTERNAL_REFERENCE**; `design-system-extraction` já cobre observado vs. derivado e contrato DESIGN.md | Leitura de DOM/styles, extensão e documentação gerada não verificada; MIT |
| [AhmadHassan-BTed/JinaClip](https://github.com/AhmadHassan-BTed/JinaClip) | Extração local de página para Markdown, limpeza heurística, Shadow DOM/iframes, screenshots | B/D | **KEEP_EXTERNAL_REFERENCE**; `web-extraction-pipeline` já cobre extração seletiva, higienização e validação | Acesso às páginas, clipboard, injeção de script, captura de tela, dados sensíveis; MIT |

**A** = processo que altera comportamento; **B** = método útil sem necessidade de skill nova; **C** = prompt sem ganho relevante; **D** = software técnico dependente de runtime externo. Uma fonte pode receber A/D ou B/D.

## Evidência incremental e QA proposto

1. **PasteGuard**: cenário positivo, app enviando prompt com segredo e nome a API de modelo; deve conferir payload upstream sem valores originais, placeholder correto e logs seguros. Near-miss: revisão de código sem fluxo LLM externo não ativa este checklist.
2. **Ui.Vision/WebBrain/BrowserKitten**: cenário positivo, rotina repetida em site autorizado com resultados verificáveis; produzir macro parametrizada e replay com postconditions e aprovação. Near-miss: pergunta pontual sobre uma página não exige macro nem agenda.
3. **design-md-chrome / JinaClip**: já cobertos por owners existentes; nenhuma duplicata criada.

Não foram executados testes comportamentais; QA acima é plano de aceitação, não resultado medido.

## Segurança e portabilidade

- Resultado: **CAUTION (static_only)** para os dez projetos, por ausência de auditoria de manifest/permissões, dependency lockfiles, scripts, egress de rede e execução de versões pinadas.
- Não instalar extensões ou bridge MCP automaticamente. Preferir perfil isolado, grants de site mínimos, revisão de dados enviados aos provedores, bloqueio de ações consequenciais sem aprovação e logs sem PII.
- Claims de privacidade/performance nos READMEs são declarações de projeto, não foram verificados independentemente.
- Nenhum aplicativo externo, recurso de OCR, proxy ou controle local foi instalado no ChatGPT.

## Publicação de melhoria
- Atualizado: `skills/secure-code-privacy-review/SKILL.md` no commit `5a5ea5603851bf2ed4ef06922a25a83ffdfa99bd`.
- Atualizado: `skills/computer-use-agent-engineering/SKILL.md` no commit `bec947ea9f61587fbbcc5bc872a58f16db25a510`.
- Índice preservado: owners e descriptions continuam os mesmos.
- Registro de avaliação: este arquivo. Conferir publicação via leitura na branch canônica. 
