# Avaliação consolidada — 16 fontes externas (2026-11-18)

**Processo:** `arsenal-autopilot` + `evaluate-and-import-skill` + revisão estática de segurança. Fontes acessadas via GitHub, índice canônico `ARSENAL INDEX.md` lido antes das escolhas. Avaliação de README/root e, nos candidatos relevantes, SKILL.md, documentação e comparações com owners existentes. Nenhum instalador, binário, arquivo de modelo ou script externo foi executado.

## Capability ledger e decisões

| Fonte | Classe | Veredito/decisão | Owner ou motivo |
|---|---|---|---|
| [oinkvm/oink](https://github.com/oinkvm/oink) | D | KEEP_EXTERNAL_REFERENCE | KVM/software peer-to-peer Mac/Windows; exige instalação e permissões de input, áudio, clipboard e rede; não é competência textual do ChatGPT. GPL-3.0-only + termos adicionais declarados |
| [Immortal-Protocols/lastbook](https://github.com/Immortal-Protocols/lastbook) | B/D | UPDATE_EXISTING | `kb-retriever`: modo urgente vs aprendizagem, lacunas, localizadores de página, biblioteca offline verificável; runtime local não instalado |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | B/D | UPDATE_EXISTING | `sales-pipeline-diagnostics`: sinais sobre carteira, schema real e integridade de fonte; marketplace, comandos Claude e MCPs não importados. Outras categorias se sobrepõem às skills do Arsenal |
| [huggingface/pybot](https://github.com/huggingface/pybot) | D | KEEP_EXTERNAL_REFERENCE | Experimento de chatbot baseado em regras e benchmark, não skill útil para execução das tarefas; grandes módulos e testes não auditados |
| [pithings/unkernel](https://github.com/pithings/unkernel) | D | KEEP_EXTERNAL_REFERENCE | Kernel Linux/Wasm e SDK requerem runtime, browser/Node e testes de isolamento; não equivale a sandbox presente; sem importar execução |
| [AFangTeam/PrintLab](https://github.com/AFangTeam/PrintLab) | A/D | CREATE_NEW adaptada | `3d-print-production` para ciclo ideia → CAD → slicer → autorização → validação física. Produto original PolyForm Noncommercial, não copiado |
| [davidondrej/superbot](https://github.com/davidondrej/superbot) | B/D | UPDATE_EXISTING | `multi-agent-orchestration`: distinguir capacidades demonstradas das planejadas e isolamento lógico de OS; runtime Rust/VPS não instalado |
| [yetanotherbrowser/yab](https://github.com/yetanotherbrowser/yab) | B/D | UPDATE_EXISTING | `computer-use-agent-engineering`: privacidade de abas, retenção, isolamento do histórico e ações autenticadas; browser macOS não integrado |
| [krezio/roomy](https://github.com/krezio/roomy) | D | KEEP_EXTERNAL_REFERENCE | Gerenciador de limpeza de disco Windows; técnica de read-only scan e confirmação já coberta por action governance; deleção é efeito destrutivo e requer runtime real |
| [tim-today/TinyDrop](https://github.com/tim-today/TinyDrop) | D | KEEP_EXTERNAL_REFERENCE | Compartilhamento via LAN/Tailscale, endpoint de rede, PIN persistente e upload/delete; não é skill sem serviço real e autenticação testada |
| [erkamyaman/unslopovich](https://github.com/erkamyaman/unslopovich) | B/D | UPDATE_EXISTING | `design-principles-audit`: defeitos funcionais antes de estereótipos visuais, testes reais vs detector estático |
| [leostera/git-twig](https://github.com/leostera/git-twig) | B/D | UPDATE_EXISTING | `multi-agent-orchestration`: medição e limites de worktree CoW; filesystem específico, não presumido |
| [n4ze3m/tiny-voca](https://github.com/n4ze3m/tiny-voca) | D | KEEP_EXTERNAL_REFERENCE | Modelo TTS inglês com duas vozes, inferência PyTorch/ONNX e pesos externos; não há execução nem suporte a português garantido |
| [claration/cis](https://github.com/claration/cis) | D/insuficiente | KEEP_EXTERNAL_REFERENCE | Sem README na raiz nas rotas comuns; busca GitHub identificou projeto Swift/Xcode e parser de DMG (`CIS/Utilities/DMG.swift`, `DMG/Sources/DMG`). Objetivo/licença/segurança não foram suficientemente verificados para importar |
| [boringmarketer/boring-marketing-skills](https://github.com/boringmarketer/boring-marketing-skills) | B | UPDATE_EXISTING | `paid-media-operations` (incrementalidade com medidas first-party) e `sales-pipeline-diagnostics` (speed-to-lead). Restante contém overlap com SEO, conteúdo, paid media, GTM e branding |
| [joshpuckett/allo](https://github.com/joshpuckett/allo) | D | KEEP_EXTERNAL_REFERENCE | Família tipográfica/asset sob SIL OFL; relevante a projetos de UI, mas não workflow/skill; sem distribuição de fontes |

## Segurança e portabilidade
**Veredito geral: CAUTION / static_only para softwares externos; APPROVE / static_only apenas para adaptação textual original.** Sem scanner automatizado ou testes runtime. Nenhuma ausência de finding foi tratada como garantia de segurança.

Riscos por categoria:
- Mac/Windows desktop com input, keychain, clipboard e navegador (Oink, Yab, Roomy, TinyDrop): permissões de sistema, dados privados, rede e efeitos destrutivos. Não instalar nem habilitar acesso por inferência.
- Agentes e plugins (Anthropic, SuperBot, Unslopovich): prompt injection em dados externos, comandos de shell, credenciais e permissões de ferramentas; integrar somente através de ações realmente disponíveis.
- Ambientes e modelos (unkernel, PyBot, tiny-voca): dependência de runtime e pesos, rede e comportamento não testado. Um VM em wasm não equivale automaticamente a sandbox com isolamento comprovado.
- Impressão 3D (PrintLab): dispositivo físico, envio e segurança mecânica, compatibilidade de filamento e controle de máquina; exigir preflight e autorização; licença não comercial do projeto.
- Git Twig: worktree parcial após falha, semântica de checkout, filesystem e proteção de alterações do usuário.
- CIS: falta documentação suficiente para inferir segurança/funcionalidade.

## Materialização efetiva

- Novo owner: `skills/3d-print-production/SKILL.md` (commit `2d271a6d5d2c658942be7c3e56bf99ab0bc97023`).
- Router: `ARSENAL INDEX.md` (`2ded14a75b007102f2ec56e44847964f89bcd48a`).
- Atualizações: `skills/kb-retriever/SKILL.md` (`77d7cb3e4cb5e0aa55e0c821230ab637b5f300b8`), `skills/computer-use-agent-engineering/SKILL.md` (`b71aa814666d124ee4c0a2051b7dd236986dec93`), `skills/design-principles-audit/SKILL.md` (`22619fb4fb51277622624d937dd5f635e55f31cc`), `skills/multi-agent-orchestration/SKILL.md` (`18cf5e5516eb2c3700450ae9068d09556d27d3e3`), `skills/paid-media-operations/SKILL.md` (`abdbd9c38a5a0b4dfd135d2e1cfd2fb51caf492d`), `skills/sales-pipeline-diagnostics/SKILL.md` (`c1e0ccec1af352ea582ba182a446c2f4e7926adc`).

## Limitações da verificação
Leitura de documentação e arquivos publicados via conector GitHub; nenhuma auditoria completa de código-fonte, licença transitive, supply chain, testes de app real ou benchmark reproduzido. Afirmações de performance são descrições dos autores, não métricas verificadas neste ambiente. Todos os casos KEEP_EXTERNAL_REFERENCE ficam registrados, mas não instalados.
