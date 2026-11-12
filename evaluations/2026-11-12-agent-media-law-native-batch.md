# Avaliação de sete fontes — 2026-11-12

## Escopo e método
Fonte oficial do Arsenal consultada: ARSENAL INDEX.md e AGENTS.md no GitHub; stack arsenal-autopilot; skill-security-review. Skill Creator consultado para princípios de redação; alterações são no Arsenal, não instalação em diretório pessoal do ChatGPT.
Leitura seletiva, comparação por capacidade e adaptação metodológica sem executar fontes, scripts, instaladores, modelos, serviços ou aplicações.

## Decisões

| Fonte | Classe | Decisão | Resultado efetivo |
|---|---|---|---|
| KKKKhazix/agent-autoloop | D/B | ABSORB_METHOD_ONLY + KEEP_EXTERNAL_REFERENCE | durable-workflow-engineering: separar reparo de recibo de repetição de trabalho; liberar executor em espera; limite causal que atravessa timers/aprovações; pause/replay explícitos |
| modelflare-ai/AnyModelBot | D/B | ABSORB_METHOD_ONLY + KEEP_EXTERNAL_REFERENCE | ai-workflow-automation-engineering: observar antes de ativar, budgets por execução/período, entrega persistida separada do trabalho, retenção sem apagar entregáveis |
| shinyobjectz/raea | D | KEEP_EXTERNAL_REFERENCE | Motor de vídeo/jogos/3D; não importar pacote ou nova skill. procedural-film já cobre timeline determinística, frames e QA; README não demonstra ganho metodológico adicional suficiente |
| lexifina/global-law | D/B | CREATE_NEW para método; KEEP_EXTERNAL_REFERENCE para servidor/dados | legal-temporal-research: cobertura e tipo de história, datas jurídicas, correções/revogações, origem oficial, limites de busca, distinção de precedentes |
| Sandflow-ai/sand3d | D/B | ABSORB_METHOD_ONLY + KEEP_EXTERNAL_REFERENCE | procedural-3d-reconstruction: peças/frames nomeados, contrato de unidades/articulação/exportação e readback; backend bpy opcional |
| expo/exact | D/B | ABSORB_METHOD_ONLY + KEEP_EXTERNAL_REFERENCE | runtime-ui-verification: relógio virtual quando suportado, testes por host, build corresponde a fontes; nenhum runtime Contract importado |
| daveebbelaar/bama | A/D | ABSORB_METHOD_ONLY | swiftui-modern-ui: store de teste separado, fixtures representativas, snapshots claro/escuro, detectar janela inativa/fallback antes de corrigir UI |

Nova skill justificada: pesquisa temporal de lei não é revisão de contrato nem discovery de produto, e impõe um contrato distinto de fonte, data e cobertura. Não criar novas stacks para combinar ocasionalmente estas fontes.

## Proveniência consultada
- KKKKhazix/agent-autoloop: 439be64f319db47e1948c737a7d88c43940f72f5; README blob 34f3f215da4df5381cc434135528c484251b42d1
- modelflare-ai/AnyModelBot: bf4c1531bdd50c4436a22bd30e48ae756041005d; README blob a35208e645bbe0f692da6e6ae2d94de88a29c546
- shinyobjectz/raea: dfca0bcf122eb1604b05f09257e89da6421ae876; README blob 8ebdd207ccff5ca12765c35f5f2fc434a8c23109
- lexifina/global-law: eb74b642424415b374fde37e9bc9f3791e4cdb01; README blob 01429764c736f269a7c75d211102f0eaae16eb56
- Sandflow-ai/sand3d: 5cdb54e4aef76377ad1a8bbc11e257eee8fc2341; README blob 48a1a51e1df09d076efd216fa29ffc9071edc03d
- expo/exact: 8f43a35aea2c4bb8f02504e732d23a754c2081ae; README blob ead1859a056e0c643053004e6e4695a299e43f84
- daveebbelaar/bama: 22dc792ea040a35270c219c669f626594267aa1f; README blob 1f773e723063b282f87ad6d5467d7ea7cb617973

Refs capturadas após as leituras; blobs dos arquivos identificam o conteúdo de README efetivamente lido. Não se afirma auditoria integral dos commits.

Arquivos adicionais:
- agent-autoloop: SECURITY.md.
- AnyModelBot: README_pt.md (trechos sobre regras, privacidade, arquitetura e limitações); documentação contém divergências entre recursos anunciados e checklist de roadmap — confirmar implementação antes de uso.
- raea: LICENSE, linhas 1–90.
- global-law: MCP.md (texto completo recuperado; foco em cobertura, data, correções e fontes).
- sand3d: docs/api.md.
- bama: skills/ship/build-and-verify/SKILL.md.
- Exact: README, seção de limites e contrato de testes/driver.
Owners comparados: durable-workflow-engineering, ai-workflow-automation-engineering, procedural-3d-reconstruction, swiftui-modern-ui, runtime-ui-verification e procedural-film; discovery-research-synthesis lida e descartada como owner para pesquisa jurídica temporal.

## Segurança e portabilidade
Veredito geral: CAUTION, static_only, limitado à revisão documental. Sem scanner, build, execução, inspeção integral do código, auditoria de dependências ou prova de segurança.
- agent-autoloop: installers curl/irm com execução, plugins como código confiado, shell/CLI, persistência local, notificações e merge/deploy opcionais. SECURITY declara que askFirst não é enforcement; links são bearer capabilities e MCP de aprovação pode permitir autoaprovação se entregue ao executor. Não importar esses poderes. Contador de saltos e separação de dados não eliminam prompt injection.
- AnyModelBot: runtime Node/Electron/Go/DSH, comandos, desktop, chaves e canais. Dados locais podem sair nos prompts via fornecedor/gateway. Não importar acesso amplo padrão, preços, envio automático ou exclusão em 30 dias. Nenhuma conta conectada.
- raea: Rust/Bun/CMake, GPU e bibliotecas nativas, installers que escrevem diretórios de skills/PATH; rede opcional para assets/modelos/provedores. FSL-1.1-ALv2 tem restrição de uso concorrente antes da futura licença Apache; não tratar como licença permissiva atual nem copiar código. Não instalar motor. Avaliação não constitui parecer de licença.
- global-law: MCP local depende de Python/git e corpora; existe também hospedado, que recebe consultas. Configurações no clone podem iniciar servidores em clientes que confiem no projeto. Corpus é cópia de terceiro, não autoridade, cobertura e termos variam. Nenhum corpus baixado nem afirmação jurídica substantiva validada.
- sand3d: Python/bpy, malhas e exportadores; scripts Python não são sandbox. Biblioteca declarada Apache-2.0, datasets descritos com atribuição e termos próprios; não presumir mesma licença para todos os assets. Não confundir joints em extras com rig suportado ou proxies IFC com BIM completo.
- Exact: toolchain Rust/Bun/Hermes e hosts nativos, setup e releases; pre-1.0 sem compatibilidade estável, plataformas desiguais e parte do design privado. Não adotar infraestrutura nem capacidades ausentes. Princípios de clock/build são portáteis condicionalmente.
- BAMA: skills MIT com scripts de build, instalação local, capturas, permissões Apple e toolchain macOS. Esta sessão não prova runtime Apple. Não instalar templates, copiar marcas/assets de referências ou capturar dados privados.

## Arquivos e publicação
- skills/durable-workflow-engineering/SKILL.md — 9f4a5acc7f4abb98e7f89503df73d8b53efda06b
- skills/ai-workflow-automation-engineering/SKILL.md — e53609480e6928a0942fa447f344d34c6075ad06
- skills/procedural-3d-reconstruction/SKILL.md — cf011bb2c5238e896d000d423a2d9fdeb7d2195b
- skills/runtime-ui-verification/SKILL.md — 5336cfdc2716e25dd5d46cefc9725abdee3b20e8
- skills/swiftui-modern-ui/SKILL.md — 2c24b9fe19f275db32f5417d8d791b488f6eeb2f
- skills/legal-temporal-research/SKILL.md — 16cb4a44e4fbab8a31828be9bd637e8ce7c7d04c
- ARSENAL INDEX.md — 429e5aec0559857a54d3b19f019d32e5a0691e76
Descriptions existentes preservadas; só o novo owner requer entrada nova no índice.

## Validação e critérios
Releitura pós-escrita compara textos publicados com os preparados; frontmatter name/description e caminho de rota conferidos. Casos de aceitação abaixo são critérios de uso, não execuções reais:
- recibo inválido depois de efeito externo → reparar recibo, não refazer efeito;
- evento cíclico atravessa espera → budget causal não reinicia;
- regra em observação → zero efeitos de negócio e registros diferenciados de execução;
- export GLB com joints → verificar consumidor, não prometer rig;
- captura macOS inativa/fallback → UNKNOWN, não “corrigir” contraste;
- clock não exposto → não inventar controle temporal;
- corpus só atual → não afirmar texto histórico; lei posterior não invalida precedente automaticamente.
Near-miss geral: avaliar repositório não autoriza instalar, conectar, agendar, enviar, gastar ou publicar produtos consumidores. Limitação: melhoria documental publicada, nenhum comportamento de runtime certificado.
