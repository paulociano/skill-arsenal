---
name: 3gpp-standards-research
description: "Pesquisar padrões celulares 3GPP, protocolos e evolução de releases com TS/TR e status normativo verificáveis."
---

# 3gpp-standards-research

## Objetivo

Responder perguntas de telecom celular com grounding explícito em especificações 3GPP, distinguindo geração, release, plano de protocolo e status normativo, e verificando fontes oficiais quando a precisão temporal importar.

## Quando usar

- GSM / UMTS / LTE / NR / 5G-Advanced / 6G;
- RAN, Core, IMS;
- PHY, MAC, RLC, PDCP, SDAP, RRC, NAS;
- handover, mobility, QoS, slicing;
- NTN, RedCap, V2X, NB-IoT;
- 3GPP TS/TR;
- releases e feature evolution;
- arquitetura e migração de rede.

## Princípio central

**Em padrões, “parece certo” não basta. Identifique a especificação, o release e o status da afirmação.**

## Workflow

1. Classificar a pergunta:
   - conceito;
   - procedure/protocol;
   - comparação;
   - release/roadmap;
   - deployment/consultoria;
   - troubleshooting.
2. Identificar RAT/generation e release quando relevantes.
3. Separar:
   - normative spec;
   - technical report/study item;
   - implementação/vendor practice;
   - inferência.
4. Citar TS/TR e seção quando houver base suficiente.
5. Para fatos recentes, releases futuros/atuais ou detalhes incertos, pesquisar fonte oficial 3GPP antes de responder.
6. Em comparações, declarar o que mudou e o que permaneceu.
7. Em troubleshooting/deployment, distinguir padrão de prática operacional.
8. Se não houver confirmação, dizer que o ponto está não verificado.

## Regras contra alucinação

- não inventar número de TS/TR;
- não inventar section number;
- não extrapolar study item para feature congelada;
- não tratar Release futuro como especificação final;
- não confundir LTE e NR apenas porque nomes de camadas são parecidos;
- não usar blogs/vendor docs como autoridade normativa quando a spec oficial estiver disponível.

## Profundidade

- pergunta introdutória → visão conceitual;
- pergunta de protocolo → state/message/IE flow;
- pergunta de PHY → precisão matemática/sinal quando suportada;
- pergunta de arquitetura → funções, interfaces e responsabilidades;
- pergunta de deployment → assumptions, trade-offs e constraints.

## Fontes

Prioridade:

1. 3GPP specs/portal;
2. documentação oficial de organismos/plataformas relacionadas;
3. vendor docs para implementação, claramente rotulados;
4. papers/blogs como apoio secundário.

## Ferramentas e dependências

Consultar fontes oficiais pela pesquisa web disponível. Mapas e snapshots da fonte orientam a busca, mas não comprovam o status atual de releases; não exigir o pacote original.

## Integração

- `library-version-grounding` como analogia de version/release grounding;
- `kb-retriever` para navegar corpos documentais;
- `eli5` para adaptar profundidade;
- `verify-before-claim`.

## Referências

Adaptada de lugasia/3gpp-skill.

Origem local: [3gpp-standards-research.docx](../3gpp-standards-research.docx).
