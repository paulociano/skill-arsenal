---
name: brand-guidelines-authoring
description: "Transformar uma identidade aprovada em guidelines operacionais, humanas e machine-readable com regras de logo, cor, tipografia, voz, aplicações, provenance e fonte de verdade sem criar documentação que deriva do runtime."
---

# brand-guidelines-authoring

## Objetivo

Converter uma identidade aprovada em um manual de marca que realmente possa ser usado por pessoas e agentes. O manual deve explicar decisões e regras; os valores canônicos devem viver em uma fonte estruturada quando isso trouxer ganho real.

## Quando usar

- criação de brand book ou manual de marca;
- organização de assets dispersos em guidelines;
- documentação de logo usage, cor, tipo, imagery, voice ou applications;
- criação de uma fonte de verdade de marca para múltiplos canais;
- revisão de manual que virou PDF estático e começou a divergir da implementação.

## Modelo de autoridade

Separar três camadas:

1. **brand model** — valores canônicos e regras objetivas em formato estruturado quando útil;
2. **guidelines** — explicação humana, rationale, exemplos, do/don'ts e decisões;
3. **derived outputs** — CSS, tokens, templates, books, sites e exports.

Não manter manual, tokens e implementação como três autoridades independentes.

## Workflow

1. Inventariar assets, decisões, fontes, licenças e lacunas.
2. Marcar cada dado como observed, approved, derived ou proposed.
3. Definir o brand model mínimo necessário. Não criar schema enorme quando uma especificação pequena resolve.
4. Normalizar papéis semânticos:
   - logo/mark/wordmark/lockup;
   - cores por função, não apenas por nome;
   - type roles;
   - imagery/icon/motion roles;
   - voice/vocabulary quando aplicável.
5. Documentar logo:
   - versões e lockups;
   - clear space;
   - minimum size;
   - small-size variant quando necessário;
   - light/dark/mono;
   - backgrounds;
   - misuse;
   - co-branding quando aplicável.
6. Documentar cor:
   - roles;
   - ratios/proporção;
   - contrastes permitidos;
   - digital/print quando houver dados reais.
7. Documentar tipografia, imagery, iconografia, grafismos, layout e motion conforme a identidade.
8. Documentar voice/tone separando regra estável de exemplos.
9. Provar aplicações reais, evitando mockups puramente decorativos.
10. Gerar ou atualizar o manual a partir do modelo sempre que possível.
11. Registrar versionamento, owner, data de aprovação e como alterações são governadas.
12. Verificar que o manual não contém valores contraditórios com os assets/tokens canônicos.
13. Quando precisar comparar cobertura e arquitetura documental, consultar exemplos reais em [Branding Style Guides](https://brandingstyleguides.com/), preferindo brand centers/manuais recentes e tratando-os como benchmark, não como template universal.

## Brand model

Quando o projeto se beneficiar de representação machine-readable, pode conter:
- metadata e versão;
- mission/tagline apenas se aprovadas;
- logo asset map;
- colors com role + value + usage;
- typography;
- layout;
- iconography;
- imagery;
- motion;
- voice;
- usage rules;
- links para masters e owners.

O nome do arquivo pode ser `brand.json`, YAML ou outro formato adequado ao projeto. Não impor um schema universal.

## Manual mínimo recomendado

- introdução/essência;
- logo system;
- clear space e minimum size;
- versões e backgrounds;
- misuse;
- color system;
- typography;
- imagery/illustration;
- iconography;
- graphic language;
- layout;
- voice/tone quando necessário;
- motion quando necessário;
- applications;
- quick reference;
- provenance/licenças;
- versão e governança.

## Regras

- manual não deve inventar significado retrospectivo para o logo;
- não declarar CMYK/Pantone sem fonte ou conversão validada;
- não embutir assets proprietários de terceiros sem direito;
- não tratar PDF como fonte de verdade se o produto depende de tokens vivos;
- não regenerar wordmark com uma fonte parecida quando existe artwork aprovado;
- separar assets protegidos de código/tokens com licenças diferentes quando necessário;
- guidelines são explicação, não desculpa para duplicar todos os valores canônicos.

## Saída mínima

- mapa de autoridade;
- brand model quando útil;
- estrutura do manual;
- logo rules;
- visual system rules;
- applications;
- provenance/licenças;
- versionamento e change governance.

## Integração

Recebe de `brand-identity-system` e `brand-logo-exploration`. Usa `brand-asset-production` para exports e `design-system-governance` quando os tokens/componentes viram implementação digital.

## Origem metodológica

Síntese adaptada de ordinarynerds/brand-book, Better-Conversations/bc-brand, ThinkFizzApp/branding, OpenAEC-Foundation/OpenAEC-style-book, Aioverse-HQ/Brand-System-Aiotize-Inc e InfoJobs/brand. O conceito de fonte única foi preservado sem importar hooks, schemas ou toolchains específicos. Branding Style Guides é mantido como arquivo externo para benchmark de estrutura e aplicações, sem transformar manuais de terceiros em regras canônicas.
