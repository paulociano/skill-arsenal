# Avaliação: mods de interface, progresso, cache e revisão — 2026-10-21

## Escopo
Aplicada a stack arsenal-autopilot após consulta ao ARSENAL INDEX.md atual. Revisão manual estática de nove fontes e aprofundamento seletivo; nenhuma instalação ou execução externa. A autorização permanente de avaliações em AGENTS.md cobre os commits. Não constitui auditoria integral de código, dependências ou instaladores.

## Decisões
| Fonte | Classe | Ação e owner | Resultado |
| --- | --- | --- | --- |
| hellosverre/claude-skins | D / B metodológica | UPDATE_EXISTING: coding-agent-engineering | Folding recuperável, fallback nativo, reduced motion e distinção apresentação/contexto. Temas e renderer ficam externos. |
| JohnnyVizz/claude-kit — savvy-progress | D / B metodológica | UPDATE_EXISTING: coding-agent-engineering | Progresso por tarefas aceitas, controle global pelo coordenador e relato local dos workers; estimativa de custo não é fatura. |
| Claude Code Docs — You should know | D / B | ABSORB_METHOD_ONLY efetivado em codex-cost-efficiency; KEEP_EXTERNAL_REFERENCE para feature | Custo dos revisores laterais contabilizado. Auditoria de escolhas já tem owner agent-choice-audit, lido e comparado; não criar nova skill de dicas ou prometer side agent ativo no ChatGPT. |
| data-goblin/claude-code-filetree | D / B metodológica | UPDATE_EXISTING: coding-agent-engineering | Distinguir seleção, leitura e escrita; seleção não autoriza ação. Navegação, cores e integração de editor ficam externas. |
| karanb192/cache-tax | D / B metodológica | UPDATE_EXISTING: codex-cost-efficiency | Medição read/write/output, warm estimado versus observado e comparação de custo total. Não adotar keepwarm automático, recusa de prompt ou preços do README como defaults. |
| anthropics/claude-code-playground — blast-radius | D / B metodológica | UPDATE_EXISTING: agent-action-governance | Fonte já estava incorporada; aprofundadas limitações do parser, freshness, probes com efeitos e conflitos de UI. Não duplicar preflight existente. |
| BayramAnnakov/claude-reflect — mod | D / B metodológica | UPDATE_EXISTING: session-learn | Revisão contextual de candidatos, dedupe, owner correto e proteção contra escrita concorrente. Pipeline de promoção e escopo já existia; complemento restrito a essas lacunas. |
| zenbu-labs/terminal-browser | D | KEEP_EXTERNAL_REFERENCE | Chromium/Electron em terminal, Kitty graphics, plugin e SSH dependem de runtime real. Sem ganho metodológico incremental suficiente diante das regras existentes de browser e perfis autenticados em agent-action-governance. |
| anthropics/claude-code-playground — replay-theater | D / B metodológica | UPDATE_EXISTING: coding-agent-engineering | Timeline deve separar chamada tentada, operação autorizada, falha e diff observado; replay em memória não prova persistência nem sucesso. |

Não há nova skill/stack ou mudança de name/description: o índice continua apontando para os mesmos owners, sem alterar índice/README ou contagens.

## Arquivos alterados
- skills/coding-agent-engineering/SKILL.md
- skills/codex-cost-efficiency/SKILL.md
- skills/agent-action-governance/SKILL.md
- skills/session-learn/SKILL.md
- este registro em evaluations/2026-10-21-claude-mods-observability-cache.md

## Segurança, privacidade e portabilidade
CAUTION para instalação dos produtos completos; aceitas apenas adaptações metodológicas independentes. Não declarar os repositórios seguros: scripts, manifests e cadeia completa de instalação não foram auditados.
- Skins documenta version check diário, leitura de uso/tema, armazenamento e hints ao modelo. Ocultar saída visual não economiza input do modelo. Configurar tema, compactar sessão e instalar marketplace não foram autorizados por esta avaliação nem executados.
- Savvy-progress fornece APIs específicas do Claude Code e estimativas via tabela embutida; inspecionado trecho inicial de hooks/register.tsx, sem validação integral do enforcement. A metodologia adotada é contrato normativo, não claim de proteção comprovada no produto.
- Filetree pode abrir editores, executar integrações e inserir seleção no prompt. Contexto contextual não é autorização e comandos de editor requerem tratamento seguro de paths.
- Cache-tax realiza forks sobre transcript, consome tokens, mantém estado e pode descartar envio uma vez. README distingue custo equivalente de API de cobrança de assinatura e teste de relógio de evidência de cache servidor. Não ativar pings, loops ou alterar TTL; preços e particularidades de provedor exigem nova consulta oficial para uso concreto.
- Blast Radius reconhece somente algumas formas de Bash e primeira parte arriscada; não é sandbox. Status de migração pode executar código. Refs remotas podem estar stale. Colisões na região acima do prompt podem ocultar botões. Essas limitações foram incorporadas ao owner já existente.
- Reflect-mod faz chamada de modelo para prompts elegíveis e grava regra após Save; README documenta perda possível em saves de sessões simultâneas. A adaptação não transforma releitura isolada em atomicidade e não instala captura de históricos.
- Terminal-browser documenta instalador curl-pipe-shell, Chromium/Electron, auxiliar nativo de input, rede via SSH e telemetria/crash reports. Lidos README raiz e plugin: versão/suporte/flag experimental devem ser reconciliados com documentação oficial antes de qualquer instalação. Não abrir sessão, porta local ou extrair cookies.
- Replay Theater registra no tool.call: operação negada ou falha também pode aparecer. Histórico é volátil e preview limitado; não tratá-lo como trilha auditável completa.
- You should know é feature do Claude Code, não uma skill portátil. A página oficial descreve revisor sem tools e custo de checks adicionais. Não ativado nem reproduzido como agente persistente.

## Validação
Revisão documental de contratos e casos abaixo; não foram executados mods, testes dos autores, cenários em aplicação consumidora, benchmarks de custo ou retenção de cache.
- Worker encerra mas testes falham → atividade concluída, tarefa ainda não aceita.
- Edição recusada → timeline marca recusa; diff final não presume alteração.
- Folding visual → nenhuma alegação de redução de tokens.
- Ping com cache read → prova somente a chamada, não economia líquida.
- Preview da primeira operação em comando composto → cobertura parcial; não autorização do restante.
- Correção pontual → não vira regra global; proposta duplicada é consolidada.
- Conflito de SHA/ETag → releitura/reconciliação, não sobrescrita cega.
- Pedido comum de código, concisão ou navegação → não instala mods, painel ou keepwarm.

Publicação pela API de contents com SHA dos owners lidos, preservando conflito em vez de force-push. Releitura pós-escrita deve coincidir integralmente com o conteúdo esperado; frontmatter/name/description e rotas existentes preservados.

## Snapshots de origem
SHAs abaixo são de blobs de arquivo, não commits. Fontes lidas na default branch em 2026-10-21:
- https://github.com/hellosverre/claude-skins — README.md; blob dd99197b3bc4ff45977ed133c904daf617d5c916; URL lida https://github.com/hellosverre/claude-skins/blob/main/README.md.
- https://github.com/JohnnyVizz/claude-kit — plugins/savvy-progress/README.md; blob 5b47f6e57c93fd965c4748bb2e6da3794dd59987; URL lida https://github.com/JohnnyVizz/claude-kit/blob/main/plugins/savvy-progress/README.md.
- https://github.com/data-goblin/claude-code-filetree — README.md; blob e72cb44dddd22a07c29dc913b421d3a3a2f34052; URL lida https://github.com/data-goblin/claude-code-filetree/blob/main/README.md.
- https://github.com/karanb192/cache-tax — README.md; blob 8b5c7d5bc876b500499bf1104a78b9957d91ecb2; URL lida https://github.com/karanb192/cache-tax/blob/main/README.md.
- https://github.com/anthropics/claude-code-playground — claude-code/mods/blast-radius/README.md; blob 0d59e5df4bba535addaa67930027d512ddf9839c; URL lida https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/blast-radius/README.md.
- https://github.com/BayramAnnakov/claude-reflect — README.md; blob d351fcbbc19f502a8ecedb50709433c7b9aba340; URL lida https://github.com/BayramAnnakov/claude-reflect/blob/main/README.md.
- https://github.com/zenbu-labs/terminal-browser — README.md; blob 2d5f5a3130c9ae38a32cac62626a5a21bf74a20e; URL lida https://github.com/zenbu-labs/terminal-browser/blob/main/README.md.
- https://github.com/anthropics/claude-code-playground — claude-code/mods/replay-theater/README.md; blob fb5d05bc0960a28bc4fc1cb9062a7ecab3723e8b; URL lida https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/replay-theater/README.md.
- https://github.com/BayramAnnakov/claude-reflect/tree/main/mod — mod/README.md; blob ae015a0379167b4a4af844003b4a1b176d128bf8.
- https://github.com/zenbu-labs/terminal-browser/blob/main/claude-code-plugin/README.md — blob f5589ad2a4e69d4f52236e508570d3f13834aa13.
- https://github.com/JohnnyVizz/claude-kit/blob/main/plugins/savvy-progress/hooks/register.tsx — blob 5e2e7ddd31a54caa5b2044c799bf60312cbafe76; inspeção parcial, sem execução.
- https://code.claude.com/docs/en/interactive-mode#you-should-know-suggestions — página oficial consultada em 2026-10-21, seção e Cost of checks; sem SHA estável.
