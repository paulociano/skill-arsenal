# Avaliação — nathanonn/agent-skills + skills.sh

Data: 2026-09-27

## Fontes
- https://github.com/nathanonn/agent-skills
- https://www.skills.sh/
- https://www.skills.sh/docs
- https://www.skills.sh/docs/api
- https://www.skills.sh/terms

## Resumo executivo
A coleção `nathanonn/agent-skills` tem boa engenharia operacional, mas grande parte do valor já tem owner no Arsenal ou depende fortemente de Codex CLI, Claude Code, Playwright CLI, Firecrawl, Node/npm e infraestrutura WordPress. O ganho incremental mais claro é metodológico em design-system extraction e em descoberta de skills via skills.sh.

`skills.sh` deve ser tratado como catálogo/radar externo, não como fonte canônica. Rankings e contagens de instalação são sinais de descoberta, não prova de qualidade, segurança ou adequação. A própria documentação recomenda revisar o `SKILL.md` e o repositório original antes de instalar.

## Capability ledger

| Fonte/capability | Classificação | Decisão | Owner canônico | Motivo |
| --- | --- | --- | --- | --- |
| ask-first | B | ABSORB_METHOD_ONLY | quick-grill / deep-grill | Batching e recommendations são úteis, mas já existe owner; evitar trigger amplo que force perguntas desnecessárias. |
| handoff-doc | B | KEEP_EXTERNAL_REFERENCE | handoff | Quase totalmente sobreposto ao handoff atual, que já preserva contexto, decisões e zero-context resume. |
| extract-design-md | A/D | UPDATE_EXISTING | design-system-extraction | Boa disciplina de separar tokens observados de screenshots e usar múltiplas páginas; ferramentas originais não são requisito no ChatGPT. |
| extract-design-system | A/D | UPDATE_EXISTING | design-system-extraction | O conceito de catálogo de componentes, estados e section patterns melhora o owner existente sem exigir skill nova. |
| design-system-to-skill | B/D | KEEP_EXTERNAL_REFERENCE | skill-builder / source-to-skill | Empacotamento por marca é útil, mas muito específico a .claude/ e worker Node. |
| cli-spec-to-goal / webg-spec-to-goal / wp-spec-to-goal / wp-requirements-to-goals | B/D | KEEP_EXTERNAL_REFERENCE | project-planning / to-spec / to-tickets / behavior-contract-validation | GOAL/VERIFY/PROGRESS é uma boa convenção, porém acoplada ao workflow /goal do Codex. Não justifica duplicar owners. |
| codex-imagegen | D | REJECT | high-fidelity-image-generation | O ambiente ChatGPT já possui geração de imagem nativa; scripts de Codex CLI/cache são infraestrutura externa sem ganho canônico. |
| prototype-wp | A/D | KEEP_EXTERNAL_REFERENCE | sem owner WordPress específico | Metodologia forte para protótipos WordPress, porém estreita e dependente de kit/assets. Criar owner só quando houver demanda recorrente real. |
| validate-block-markup | A/D | KEEP_EXTERNAL_REFERENCE | behavior-contract-validation | Validação Gutenberg é tecnicamente útil, mas requer runtime Node pesado e snapshot WordPress pinado. Melhor não prometer até haver demanda e runtime apropriado. |
| wp-rest-api | A/D | KEEP_EXTERNAL_REFERENCE | sem owner WordPress específico | Guardrails REST são bons, mas execução depende de credenciais, curl/jq e mutações de site. Não importar sem caso de uso recorrente. |
| skills.sh directory/API | B/D | UPDATE_EXISTING | arsenal-autopilot | Excelente radar de descoberta, com API/search e sinais de popularidade, mas não autoridade. Deve alimentar triagem, nunca adoção automática. |

## Segurança e portabilidade
- Não foram executados installers, scripts ou runtimes externos.
- Várias skills usam `npm`, `npx`, Playwright CLI, Firecrawl, Codex CLI, curl/jq, credenciais WordPress ou hooks Claude Code.
- `wp-credential-guard` é Claude-Code-only e não tem equivalente direto; não foi adotado.
- `validate-block-markup` faz bootstrap de centenas de pacotes npm no primeiro uso. Isso é aceitável em um runtime controlado, mas excessivo para adoção automática.
- `wp-rest-api` contém operações destrutivas ou externas que exigem approval gates claros.
- `skills.sh` declara auditorias e scanners, mas não garante qualidade ou segurança de toda skill. A fonte original continua sendo necessária para revisão.

## Mudanças adotadas
1. Atualizar `design-system-extraction` para capturar explicitamente component anatomy, variants, interactive states, section patterns e trilha de evidência por página/tema quando o runtime permitir.
2. Atualizar `arsenal-autopilot` para aceitar diretórios/ecossistemas como skills.sh como discovery source, com funil: descobrir → resolver repo original → revisar fonte → security/portability → ownership.
3. Não criar novas skills WordPress neste lote. Há valor, mas ainda não há evidência de recorrência suficiente para justificar owners estreitos.

## Decisão sobre skills.sh
Usar como fonte de descoberta secundária. Sinais úteis: busca semântica, popularidade, origem/repo, first-party curated sets e auditorias publicadas. Não usar install count como score de qualidade e não instalar diretamente do ranking sem ler a fonte original.

## Validação
Adoção limitada a duas melhorias em owners existentes e a este registro de avaliação. Nenhum runtime externo foi prometido como disponível.


---

## Adendo — madebychip/madebychip-illustration-skills

Fonte: https://github.com/madebychip/madebychip-illustration-skills

### Capability ledger

| Fonte/capability | Classificação | Decisão | Owner canônico | Motivo |
| --- | --- | --- | --- | --- |
| Guild Enamel | B | ABSORB_METHOD_ONLY | high-fidelity-image-generation | A força está no style-lock, family router e checklist de drift. O estilo específico é conteúdo de marca, não skill canônica. |
| Premium 3D Claymorphism | B | UPDATE_EXISTING | high-fidelity-image-generation | Boa separação WHAT/HOW/COLOR/FORMAT, defaults úteis e preservação em edições iterativas. |
| Soft 3D Otter | A/B | UPDATE_EXISTING | high-fidelity-image-generation | Excelente método para personagem fixo: autoridades separadas por identidade, pose e rendering, invariantes explícitos e regra de adaptar pose à anatomia. |
| reference images / prompt libraries | D | KEEP_EXTERNAL_REFERENCE | n/a | Assets e exemplos têm licenças específicas e não devem ser copiados para o Arsenal; funcionam como dados de referência do estilo. |

### Segurança e portabilidade
- Não há necessidade de executar código, installer ou runtime externo para absorver a metodologia.
- O repositório foi desenhado para ChatGPT Projects e geração de imagem nativa, portanto a portabilidade conceitual é alta.
- Os estilos, tokens, personagem e imagens de referência permanecem externos; o Arsenal absorve apenas a metodologia genérica de consistência visual.
- A licença do workflow/texto é MIT, mas o próprio repositório alerta que imagens de referência podem ter licenças separadas.

### Mudança adotada
Atualizar `high-fidelity-image-generation` com:
1. autoridade explícita por dimensão de referência;
2. invariantes para personagem fixo e famílias visuais;
3. separação WHAT / HOW / COLOR / FORMAT;
4. consistência de série e QA de drift.

Não criar skills específicas como `guild-enamel`, `claymorphism` ou `soft-3d-otter`: elas são estilos/packs, não capacidades gerais.
