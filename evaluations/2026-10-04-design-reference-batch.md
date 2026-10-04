# Avaliação — Design reference batch (2026-10-04)

## Escopo

Fontes avaliadas:

1. https://www.toools.design/
2. https://brandingstyleguides.com/
3. https://designspells.com/
4. https://growth.design/psychology
5. https://www.fontbrief.com/fontbrief
6. https://palitra.app/
7. https://mediacheatsheet.com/

Router canônico: `ARSENAL INDEX.md`.

Stack aplicada: `arsenal-autopilot`.

Owners comparados:
- `design-direction`
- `design-principles-audit`
- `typographic-composition`
- `interaction-polish`
- `social-carousel-engineering`
- `brand-guidelines-authoring`
- `color-psychology-context`
- `web-design-engineer`

## Resumo executivo

Nenhuma das sete fontes justifica uma nova skill standalone. O ganho incremental está em usá-las como repertório, benchmark ou grounding atual dentro de owners já existentes.

A decisão do lote foi:
- criar **0 novas skills**;
- atualizar **5 skills existentes**;
- atualizar **1 catálogo de referências**;
- manter Palitra e TOOOLS principalmente como referências externas;
- registrar Media Cheat Sheet como apoio de specs atuais, sem substituir fontes oficiais de plataforma.

## Capability ledger

| Fonte | Capability útil | Classe | Owner | Decisão |
|---|---|---:|---|---|
| TOOOLS.design | Descoberta ampla de ferramentas e referências de design | B | design-direction / reference library | KEEP_EXTERNAL_REFERENCE |
| Branding Style Guides | Benchmark de estrutura e cobertura de brand manuals reais | B | brand-guidelines-authoring | UPDATE_EXISTING |
| Design Spells | Repertório de microinterações e detalhes de produto | B | interaction-polish | UPDATE_EXISTING |
| Growth.Design Psychology | Índice de vieses, heurísticas e princípios para formar hipóteses de UX | B | design-principles-audit | UPDATE_EXISTING |
| FontBrief | Exploração tipográfica por eixos de personalidade | B | typographic-composition | UPDATE_EXISTING |
| Palitra | Descoberta rápida de paletas a partir de conceitos/referências | B/D | design-direction / color-psychology-context | KEEP_EXTERNAL_REFERENCE |
| Media Cheat Sheet | Grounding atual de dimensões, formatos e safe zones sociais/ads | A/B | social-carousel-engineering | UPDATE_EXISTING |

## 1. TOOOLS.design

### O que faz de verdade

Diretório curado de recursos e ferramentas para design, com categorias como inspiração, icons, illustrations, UI kits, UX tools, color tools, typography, marketing e web builders. A página pública se apresenta como um catálogo com milhares de recursos e atualizações recorrentes.

### Ganho incremental

Serve bem como **radar de descoberta**, sobretudo quando o Arsenal precisa localizar uma ferramenta atual para uma necessidade específica.

Não serve como autoridade sobre a qualidade da ferramenta listada. Destaque editorial, parceria, trending ou presença no catálogo não provam segurança, licença, fit ou superioridade.

### Decisão

**Classe B. KEEP_EXTERNAL_REFERENCE.**

Foi incorporado ao catálogo de referências de `design-direction` com a regra: usar para descobrir candidatos e resolver depois a fonte original.

Não criar uma skill `toools-design`.

## 2. Branding Style Guides

### O que faz de verdade

Arquivo de milhares de brand manuals e dezenas/centenas de brand centers online, incluindo documentação recente e exemplos de diferentes países e setores.

### Ganho incremental

O Arsenal já sabe escrever guidelines, mas faltava uma fonte explícita e ampla para **benchmark de arquitetura documental**, cobertura de seções e aplicações reais.

### Decisão

**Classe B. UPDATE_EXISTING.**

Atualizado `brand-guidelines-authoring` para permitir benchmark com manuais reais, mantendo:
- identidade do projeto como autoridade;
- exemplos externos como referência, não template;
- preferência por materiais recentes;
- proibição de copiar identidade ou tratar documento histórico como vigente sem confirmação.

Não criar nova skill.

## 3. Design Spells

### O que faz de verdade

Coleção curada de pequenos detalhes de interface encontrados em produtos reais: transitions, motion, easter eggs, loading, confirmations, navigation details, skeuomorphism e outros padrões de delight/polish.

### Ganho incremental

Há valor como **biblioteca de exemplos concretos de microinteração**, especialmente para sair de descrições vagas como “deixe mais premium”.

O Arsenal já possui `interaction-polish` e `ui-motion-design`, então o método novo não é suficiente para outro owner.

### Decisão

**Classe B. UPDATE_EXISTING.**

Adicionado como repertório externo em `interaction-polish`, com exigência de extrair:
- comportamento;
- função;
- contexto;
- alternativa acessível.

Não transformar delight em checklist.

## 4. Growth.Design Psychology

### O que faz de verdade

Catálogo de mais de cem vieses cognitivos e princípios de design organizados em torno de quatro momentos do ciclo de decisão: filtrar informação, buscar significado, agir sob tempo e armazenar memória. Inclui exemplos e explicações resumidas.

### Ganho incremental

O Arsenal já tem `design-principles-audit`, portanto importar o catálogo como nova skill duplicaria ownership.

O ganho está na **taxonomia de descoberta** e no repertório de princípios quando um sintoma de UX precisa ser transformado em hipóteses.

### Risco

Catálogos de “leis” de UX podem induzir uso como argumento de autoridade ou causalidade inventada.

### Decisão

**Classe B. UPDATE_EXISTING.**

Growth.Design entrou como índice de repertório em `design-principles-audit`, com guardrail explícito:
- a taxonomia não é tratada como científica/canônica;
- princípio não substitui evidência;
- escolher poucas lentes ligadas ao sintoma real.

## 5. FontBrief

### O que faz de verdade

Ferramenta de descoberta de fontes orientada por pares de atributos de personalidade, por exemplo:
- neutral ↔ expressive;
- elegant ↔ rugged;
- serious ↔ friendly;
- technic ↔ organic;
- classic ↔ progressive;
- familiar ↔ daring;
- loud ↔ discreet;
- cold ↔ warm.

Também permite filtros como serif/sans e outras propriedades do catálogo.

### Ganho incremental

O Arsenal já possui radar de fontes e `typographic-composition`, mas FontBrief adiciona um mecanismo útil para transformar linguagem de briefing em shortlist tipográfica.

### Decisão

**Classe B. UPDATE_EXISTING.**

`typographic-composition` passa a permitir exploração por eixos de personalidade, com regras:
- os eixos são linguagem de briefing, não medição objetiva;
- shortlist ainda precisa ser validada por legibilidade, cobertura, pesos/eixos, licença e uso real.

Não criar skill exclusiva.

## 6. Palitra

### O que faz de verdade

Ferramenta web para encontrar paletas a partir de palavras-chave e referências visuais. Fontes públicas sobre o produto descrevem busca por imagens relacionada ao termo e extração de cores para gerar opções de paleta.

### Ganho incremental

Útil no estágio de ideação, especialmente quando a direção começa por um conceito, lugar, filme, material ou atmosfera em vez de uma cor pronta.

O Arsenal já cobre:
- direção visual;
- papéis de cor;
- psicologia contextual;
- contraste;
- acessibilidade;
- tokens.

Palitra não substitui nenhuma dessas etapas.

### Dependência

É um serviço web externo. O comportamento e disponibilidade podem mudar.

### Decisão

**Classe B/D. KEEP_EXTERNAL_REFERENCE.**

Adicionado ao catálogo de referências como ferramenta de exploração inicial. Não foi incorporado como dependência nem como motor presumidamente disponível.

## 7. Media Cheat Sheet

### O que faz de verdade

Diretório pesquisável de especificações de mídia social e publicidade, atualizado para 2026, cobrindo múltiplas plataformas e formatos. A fonte declara links para especificações de origem e disponibiliza templates/safe zones em vários casos.

### Ganho incremental

Este é o recurso com maior efeito operacional do lote.

O Arsenal já exige aspect ratio correto e safe zones, mas não apontava para uma fonte externa atual de specs antes do export. Como plataformas mudam dimensões, overlays e regras, um passo explícito de grounding reduz erro de produção.

### Decisão

**Classe A/B. UPDATE_EXISTING.**

`social-carousel-engineering` recebeu um passo de **Spec grounding** antes do export:
1. verificar dimensões;
2. aspect ratio;
3. formato;
4. duração/tamanho quando aplicável;
5. safe zones;
6. usar Media Cheat Sheet para acelerar a consulta;
7. manter documentação oficial da plataforma como autoridade final em caso de conflito.

Não criar skill de specs sociais porque a capacidade pertence ao owner de produção/export.

## Mudanças publicadas

Atualizados:
- `skills/design-direction/references/design-reference-libraries.md`
- `skills/design-principles-audit/SKILL.md`
- `skills/typographic-composition/SKILL.md`
- `skills/interaction-polish/SKILL.md`
- `skills/social-carousel-engineering/SKILL.md`
- `skills/brand-guidelines-authoring/SKILL.md`

Não houve nova skill nem novo stack, portanto `ARSENAL INDEX.md` não precisou de nova rota.

## Segurança e portabilidade

Nenhuma fonte exigiu execução de instalador, script, extensão ou binário para extrair valor.

Foram mantidos como externos:
- catálogos;
- web apps;
- datasets dinâmicos;
- templates e downloads.

O Arsenal não presume que Palitra, FontBrief, TOOOLS, Media Cheat Sheet ou qualquer ferramenta citada esteja integrada ao runtime.

## Acceptance cases

### Should trigger

- “Quero referências atuais para uma landing de fintech.” → `design-direction` pode usar TOOOLS como radar e então aprofundar fontes específicas.
- “Nossa marca é séria mas acolhedora; que tipo de fonte procurar?” → `typographic-composition` pode usar eixos de FontBrief para montar shortlist.
- “Revise este checkout que confunde usuários.” → `design-principles-audit` pode usar Growth.Design como repertório, escolhendo poucas lentes ligadas à evidência.
- “Deixe as interações mais refinadas.” → `interaction-polish` pode consultar Design Spells por comportamentos concretos, sem copiar efeitos automaticamente.
- “Crie carrossel para LinkedIn/Instagram.” → `social-carousel-engineering` verifica specs atuais e safe zones antes do export.
- “Monte um manual de marca.” → `brand-guidelines-authoring` pode comparar cobertura com brand manuals reais.

### Near misses

- “Escolha uma cor bonita.” → não acionar Palitra automaticamente se o contexto já define paleta.
- “Faça o site parecer premium.” → não buscar microinterações antes de resolver hierarquia e estrutura.
- “Use a lei de Hick para provar que precisamos de 3 opções.” → rejeitar uso de heurística como prova causal.
- “Qual o tamanho do post?” → não confiar cegamente em agregador quando a plataforma oficial divergir.
- “Copie o manual da marca X.” → referências externas não autorizam cópia de identidade.

## Conclusão

O lote acrescentou valor principalmente como **camada de repertório e grounding**, não como novos workflows autônomos.

A arquitetura do Arsenal permaneceu enxuta: owners existentes foram fortalecidos e as sete fontes ficaram posicionadas de acordo com a pergunta que realmente ajudam a responder.
