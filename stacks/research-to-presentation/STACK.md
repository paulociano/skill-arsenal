---
name: research-to-presentation
description: Converte pesquisa, documentos ou dados em apresentações e dashboards executivos editáveis, estruturados por evidência, narrativa e QA visual.
---

# Research To Presentation

## Objetivo
Partir de pesquisa, documentos, dados ou material bruto e chegar a uma apresentação clara, defendível e visualmente coerente, incluindo decks executivos orientados a KPIs e dashboards.

## Skills candidatas
- discovery-research-synthesis
- dashboard-design
- presentation-template-adaptation
- publication-figure-engineering
- writing-quality
- verify-before-claim

## Workflow
1. **Frame** — definir audiência, decisão/objetivo, contexto de uso, duração, densidade e formato de entrega antes de desenhar slides.
2. **Evidence** — sintetizar as fontes e manter um ledger mínimo de claims, números, figuras, origem, período e lacunas. Não inventar número para preencher layout.
3. **Story** — definir tese, arco e função de cada slide antes de hidratar o deck. Para apresentações relevantes, revisar a sequência enquanto mudanças ainda são baratas.
4. **Design contract** — definir direção visual, ritmo, densidade e famílias de componentes. Use `presentation-template-adaptation` quando houver template ou deck de referência.
5. **Dashboard route** — quando o deck for quantitativo ou recorrente, usar `dashboard-design` e mapear cada pergunta decisória para KPI, comparação, driver, exceção ou ação. Preferir gráficos, tabelas, KPIs e shapes nativos/editáveis quando o runtime permitir.
6. **Visual encoding** — usar `publication-figure-engineering` quando gráficos ou figuras quantitativas exigirem tratamento especializado. A geometria deve representar os valores corretamente; decoração não pode se passar por evidência.
7. **Build from source** — manter uma fonte regenerável do deck sempre que o ambiente permitir. Corrigir plano, dados, conteúdo ou layout na fonte e reconstruir, em vez de remendar apenas o PPTX final.
8. **Deterministic QA** — verificar, conforme as ferramentas disponíveis: overflow, overlap, texto cortado, contraste, placeholders, fontes, arquivo inválido/corrompido, ausência de notas/citações exigidas e consistência entre dado e visual.
9. **Rendered QA** — renderizar ou inspecionar visualmente o deck final quando possível. Avaliar hierarquia, ritmo, repetição, densidade, alinhamento, legibilidade e se cada slide comunica sua mensagem sem depender da intenção do autor.
10. **Critic pass** — em decks relevantes, fazer uma revisão independente ou fresh-eyes proporcional ao risco depois do primeiro render; priorizar poucos findings de alto impacto e reconstruir o necessário.
11. **Verify** — conferir dados, claims, fontes, períodos, consistência narrativa e entregáveis antes de afirmar conclusão.

## Contrato para dashboards em slides

Para decks executivos, business reviews, board decks e relatórios recorrentes:

- abrir com estado e mensagem executiva, não com catálogo de métricas;
- KPI deve carregar comparação útil quando houver baseline/meta/período equivalente;
- exceção deve apontar driver, owner ou próxima decisão quando os dados permitirem;
- distinguir dado ausente/desatualizado de desempenho positivo;
- manter período, unidade, denominador e filtros relevantes visíveis;
- usar componentes nativos/editáveis para gráficos, tabelas, KPIs e formas quando isso não reduzir fidelidade;
- reservar imagem raster para fotografia, ilustração ou visual que não precise continuar semanticamente editável;
- separar slides de leitura executiva de slides de diagnóstico e backup;
- para geração recorrente, preservar schema de entrada, regras de cálculo e contratos de layout para regeneração.

## QA proporcional

- **Rápido:** validação estrutural + inspeção visual do conjunto.
- **Padrão:** estrutural + render + revisão fresh-eyes + uma rodada de correção.
- **Alto risco:** adicionar auditoria de claims/dados, revisão independente mais profunda e validação do arquivo no aplicativo de destino quando disponível.

Não transforme QA em painel de agentes por padrão. Aumente o custo de revisão somente quando materialidade, audiência ou risco justificarem.

## Regras

- Não criar slide apenas para completar contagem.
- Não usar layout genérico repetido quando o argumento pede figura, tabela, comparação ou composição diferente.
- Não rasterizar um dashboard inteiro se o usuário precisa editar números e gráficos depois.
- Não afirmar que o deck foi revisado visualmente se não houve render/inspeção equivalente.
- Não exigir PptxGenJS, LibreOffice, LangGraph, Streamlit ou qualquer runtime externo específico; use as capacidades reais disponíveis no ambiente.
- Se a apresentação for recorrente, preferir pipeline regenerável a edição manual cumulativa.

## Regra de parcimônia
Não use todas as skills visuais se a apresentação não precisar delas. Para um deck simples, narrativa + build + QA podem bastar; `dashboard-design` entra apenas quando a apresentação realmente funcionar como interface quantitativa de decisão.
