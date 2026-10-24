# Avaliação de cinco projetos externos — 2026-10-24

## Método e escopo
Índice canônico: ARSENAL INDEX.md (branch master). Router: stacks/arsenal-autopilot/STACK.md. Fontes: READMEs e metadados GitHub públicos dos cinco repositórios em sua branch main. Foi uma avaliação documental, **não** auditoria completa de código, instalação, execução, nem reprodução independente de claims, benchmarks ou licenças.

| Fonte | Classe | Capacidade | Decisão / owner existente |
| --- | --- | --- | --- |
| [FavioVazquez/showtime](https://github.com/FavioVazquez/showtime) | A/D | Studio de vídeo local para coding agents, preflight, preview, QA e artefatos segregados | UPDATE_EXISTING skills/video-editing-pipeline/SKILL.md |
| [Worklenz/worklenz](https://github.com/Worklenz/worklenz) | B/D | Gestão de projetos, timesheets, capacidade, custo e dashboards | UPDATE_EXISTING skills/project-health-review/SKILL.md |
| [harshalgajjar/Reminal](https://github.com/harshalgajjar/Reminal) | D | Acesso remoto a GUI, desktop e shell, sessions/ownership | UPDATE_EXISTING skills/agent-action-governance/SKILL.md |
| [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | A/D | Screens navegáveis Material 3 Expressive convertidos em prompt para implementação | UPDATE_EXISTING skills/material-design-3/SKILL.md |
| [olalie/tapmap](https://github.com/olalie/tapmap) | B/D | Observabilidade local de sockets/processos e geolocalização aproximada | UPDATE_EXISTING skills/secure-code-privacy-review/SKILL.md |

## Incremento comprovável na metodologia
1. Showtime: exigir preflight, artefatos e QA de render, incluindo legibilidade entre quadros e versões vertical/horizontal; complementa, sem duplicar, shot ledger já existente.
2. Worklenz: reconciliar horas planejadas/registradas, utilização, custo e resultado, preservando granularidade e fonte em review do portfólio.
3. Reminal: criar fronteiras distintas para view-only, janela, desktop, shell, revogação e reentrada após desconexão; não introduzir capacidade remota inexistente.
4. M3E Canvas: transpor protótipo navegável para contrato de telas, transições, estados e critérios de verificação na aplicação compilada.
5. TapMap: distinguir socket observado, executável atribuído, GeoIP aproximado e inferência de ameaça; não vender visibilidade como prevenção.

## Segurança, licença e portabilidade
- Showtime: Python/Node, instalação de runtimes e modelos, processamento de mídia e acesso ao filesystem. Revisão completa de instaladores/dependências e custos deve preceder qualquer implantação.
- Worklenz: aplicação AGPL-3.0 com serviços e persistência. Método foi adaptado em texto, sem reutilizar código; implantação exigiria revisão de configuração, autenticacao, dados e obrigações de licença.
- Reminal: maior risco de controle remoto, shell e alteração persistente do host. Não executar curl-pipe-shell/PowerShell installer na etapa de avaliação; exigir threat model, revogação e sandbox.
- M3E Canvas: browser tool e assistente opcional com chave do usuário. Prototipação e prompt não equivalem à implementação funcional; proteger chaves e verificar saída.
- TapMap: leitura de metadados de rede/processos, banco GeoIP, autostart e MQTT opcional. IP/ASN e geolocalização não provam exfiltração; verificar retenção e exposição do painel.
- Todos: **CAUTION** para instalação, pois nenhum script/dependência foi auditado ou executado.

## Casos de aceitação (testes futuros)
| Should trigger | Near miss | Evidência de sucesso |
| --- | --- | --- |
| Gerar vídeo com agente e render local | Apenas escrever roteiro | Preview e render validado com QA |
| Revisão financeira/capacidade de portfólio com fontes operacionais | Lista de tarefas sem time tracking | Conciliar períodos, horas e custo com owner |
| Abrir sessão remota de controle real | Apenas consultar docs do desktop | Testar grants, takeover, revogação e logs |
| Implementar app M3 a partir de protótipo clicável | Uma screenshot isolada sem fluxo | Navegação/eventos funcionais no runtime |
| Investigar processos e destinos de conexões | Diagnóstico de ataque sem logs | Baseline, limites GeoIP, processo e confiança |

## Publicação e limites
Arquivos alterados: skills/video-editing-pipeline/SKILL.md; skills/project-health-review/SKILL.md; skills/agent-action-governance/SKILL.md; skills/material-design-3/SKILL.md; skills/secure-code-privacy-review/SKILL.md.

Não foi necessário criar owner novo nem modificar o ARSENAL INDEX.md. Ganho descrito é metodológico; não significa que ferramentas externas foram instaladas, integradas ou testadas na plataforma ChatGPT.
