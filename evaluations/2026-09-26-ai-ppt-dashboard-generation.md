# IA para geração de PPT e dashboards em slides

Data: 2026-09-26. Índice canônico e stack `evaluate-and-import-skill` lidos antes da seleção. Avaliação estática; nenhum instalador, script ou runtime externo foi executado.

## Decisão

A pesquisa confirmou valor real, mas o melhor encaixe é **evoluir a stack existente `research-to-presentation`**, não importar múltiplas skills concorrentes.

Mudanças adotadas:
- entrada ampliada de pesquisa para pesquisa/documentos/dados;
- rota explícita para decks quantitativos e dashboards executivos;
- framing por audiência, decisão, duração e densidade;
- ledger de claims/números/fontes antes do layout;
- preferência por charts, tabelas, KPIs e shapes nativos/editáveis;
- fonte regenerável como autoridade quando possível;
- QA em duas camadas: checks determinísticos + inspeção do render;
- critic/fresh-eyes proporcional ao risco, sem obrigar arquitetura multiagente;
- regras para apresentações recorrentes e regeneração automática.

## Candidatas

| Fonte | Categoria | Ganho incremental | Decisão |
| --- | --- | --- | --- |
| JohnTan38/presentation-skill-codex | A/D | Workspace estruturado, evidence plan, design DNA, PPTX editável, QA de geometria e visual review | Adaptar metodologia; não copiar runtime/scripts |
| addsumtech/slides_maker | A/D | Source grounding, native charts, planejamento antes do build, critic independente, gates de layout/render e componentes quantitativos | Principal referência metodológica; adaptar sem exigir agentes/subagentes |
| chinu3d/ai_presentation_creator | B/D | Extração de visual language de PPT de referência e compilação via python-pptx | Conceito já coberto por `presentation-template-adaptation`; não duplicar |
| mehdimo/GenSlide | B/D | Pipeline parse → orchestrate → content → build → human approval | Boa arquitetura de referência, mas LangGraph/Streamlit não agregam ao Arsenal |
| PptxGenJS | D | Motor técnico forte para PPTX editável, charts, shapes e tables | Usar quando disponível no ambiente; não transformar biblioteca em skill |

## Segurança e portabilidade

**APPROVE** para a síntese metodológica incorporada ao Arsenal.

**CAUTION** para instalar/rodar as ferramentas externas sem auditoria adicional. As candidatas podem envolver dependências npm/pip, LibreOffice, browser/headless rendering, chaves de API, downloads de assets, geração de imagens e scripts locais. `slides_maker` documenta tratamento de credenciais e billing gate; isso é sinal positivo, mas não substitui auditoria da cadeia de dependências.

Nenhum código externo foi copiado. Nenhum installer, `npx skills add`, `pip install`, Streamlit app, LangGraph graph ou script de build foi executado.

## Padrões preservados

1. **Frame before build** — audiência, decisão, tempo e densidade são parte do contrato.
2. **Evidence before decoration** — claims e números têm origem e período antes de virar visual.
3. **Story before hydration** — função do slide precede layout.
4. **Native/editable dashboard components** — dados importantes não devem virar screenshot por conveniência.
5. **Source-level iteration** — corrigir a fonte regenerável e reconstruir.
6. **Deterministic + rendered QA** — geometria/arquivo e julgamento visual cobrem classes de falha diferentes.
7. **Fresh-eyes proportional review** — crítica independente é valiosa, mas custo deve acompanhar risco.
8. **Recurring deck contract** — schema de dados, cálculo e layout precisam sobreviver à próxima atualização.

## Sobreposição com o Arsenal

- `presentation-template-adaptation` já cobre template, visual language, layout contracts e fidelidade.
- `dashboard-design` já cobre KPIs, exceções, drivers, comparação, ownership e ação.
- `publication-figure-engineering` cobre figuras quantitativas.
- `verify-before-claim` cobre validação antes da entrega.

Por isso, criar uma skill separada de “AI PPT dashboard” fragmentaria o workflow. A stack `research-to-presentation` passa a coordenar essas competências.

## Fontes

- https://github.com/JohnTan38/presentation-skill-codex
- https://github.com/addsumtech/slides_maker
- https://github.com/chinu3d/ai_presentation_creator
- https://github.com/mehdimo/GenSlide
- https://github.com/gitbrent/PptxGenJS

## Limites

A avaliação foi documental e estática. Não comparei qualidade visual em benchmark comum, não medi fidelidade de PPTX no PowerPoint/Keynote/Google Slides e não auditei todas as dependências transitivas. As regras incorporadas são portáveis e não dependem dessas ferramentas específicas.
