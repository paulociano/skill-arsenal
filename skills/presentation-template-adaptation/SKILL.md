---
name: presentation-template-adaptation
description: "Adaptar conteúdo a um deck de referência preservando identidade visual, elementos fixos e capacidade dos layouts."
---

# presentation-template-adaptation

## Objetivo

Adaptar uma apresentação nova a partir de um deck/template de referência preservando identidade visual, distinguindo decoração de conteúdo editável e respeitando limites reais de cada layout.

## Quando usar

- usuário fornece PPTX/Slides como template ou referência;
- é necessário preservar layout, tipografia, cores, logos, componentes e ritmo do deck;
- a apresentação nova deve continuar editável e coerente com o sistema original.

## Princípio central

**Não reconstruir o design a partir de aparência genérica. Separar estrutura fiel, semântica editável e decoração fixa.**

## Workflow

1. **Source read** — ler o deck/template real, não apenas uma descrição.
2. **Dual evidence** — quando disponível, usar tanto estrutura editável quanto preview/render visual; uma fonte sozinha pode esconder semântica ou aparência.
3. **Classify elements** — marcar cada elemento como:
   - conteúdo editável;
   - componente repetível/flexível;
   - decoração fixa;
   - asset/brand element.
4. **Layout contract** — para cada layout, registrar:
   - finalidade;
   - campos editáveis;
   - slots opcionais;
   - limites de repetição;
   - safe text capacity;
   - assets fixos;
   - proporções e alinhamentos.
5. **Theme extraction** — derivar cores, tipografia e papéis semânticos sem substituir os assets reais.
6. **Outline first** — gerar/revisar outline antes de hidratar slides quando a tarefa permitir revisão.
7. **Layout selection** — escolher o layout compatível com o tipo e a quantidade de conteúdo; não forçar um layout bonito a um conteúdo que excede sua capacidade.
8. **Schema-conforming content** — gerar conteúdo que caiba no contrato do layout, em vez de escrever texto livre e depois esmagá-lo.
9. **Hydrate** — aplicar texto, dados, imagens e ícones somente nos campos editáveis.
10. **Visual QA** — renderizar/revisar slide por slide e corrigir overflow, hierarquia, alinhamento, contraste, repetição e brand drift.

## Regras

- imagem de slide + estrutura editável são complementares;
- preservar logos, fundos, frames e divisores quando forem decoração/brand assets;
- não trocar um layout por outro só porque o conteúdo não coube sem antes reduzir/reformular o conteúdo;
- conteúdo gerado nunca deve alterar geometry crítica silenciosamente;
- falha em análise opcional deve preservar fidelidade, não produzir uma invenção criativa;
- limites de texto são propriedades do layout, não metas universais.

## Modos

- **Standard:** layouts fixos, outline review, previsibilidade.
- **Adaptive:** layouts podem responder ao conteúdo quando não há template rígido.
- **Template adaptation:** template de referência é autoridade visual.

## Ferramentas e dependências

Usar a skill de apresentações e os runtimes disponibilizados pelo ambiente para ler, gerar e renderizar decks; para serviços conectados, usar suas ferramentas reais. Não exigir Presenton, Docker ou Template V2 JSON. Declarar qualquer limite de leitura/render da referência.

## Referências

Adaptada de presenton/presenton, especialmente Template V2.

Origem local: [presentation-template-adaptation.docx](../presentation-template-adaptation.docx).
