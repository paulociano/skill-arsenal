# Avaliação — visual layout, motion, apresentações e fontes modernas — 2026-09-27

## Escopo

Lote avaliado para ampliar o Arsenal em landing pages, creative web, apresentações, geração visual/motion e tipografia moderna. Comparação feita contra os owners canônicos existentes antes de decidir adoção.

## Decisões por fonte

| Fonte | Classe | Decisão | Owner / destino |
|---|---|---|---|
| elayadesign/ai-design-skills · landing-page-design | A/B | KEEP_EXTERNAL_REFERENCE | `landing-craft` já registra absorção dos princípios úteis; não duplicar |
| LottieFiles/motion-design-skill | A | UPDATE_EXISTING | `ui-motion-design` recebe motion personality e choreography; `creative-web-engineering` usa a linguagem antes da implementação |
| rbaumier/skills · ui-animations | B | KEEP_EXTERNAL_REFERENCE | já é origem explícita de `ui-motion-design` |
| feitangyuan/motion-web | A/D | ABSORB_METHOD_ONLY | `creative-web-engineering` recebe gate de física/procedural verificável; scripts e verificadores externos não são importados |
| SlideSpeak/slide-design-skill | A/D | ABSORB_METHOD_ONLY | `cinematic-presentation` recebe style discovery; engine HTML/fal.ai não vira dependência |
| MiniMax-AI/skills · frontend-dev | D | KEEP_EXTERNAL_REFERENCE | capacidades úteis já têm owners; MiniMax API/media runtime não é assumido disponível |
| vercel/geist-font | asset/reference | ADD_TO_RADAR | `typographic-composition/references/MODERN-FONT-RADAR.md` |
| rsms/inter | asset/reference | ADD_TO_RADAR | idem |
| arrowtype/recursive | asset/reference | ADD_TO_RADAR | idem; destaque para variable axes e motion tipográfico |
| IBM/plex | asset/reference | ADD_TO_RADAR | idem; sistema multi-role/multilingual |
| Omnibus-Type/Archivo | asset/reference | ADD_TO_RADAR | secundária |
| weiweihuanghuang/Work-Sans | asset/reference | ADD_TO_RADAR | secundária |
| indestructible-type/Jost | asset/reference | ADD_TO_RADAR | secundária |
| JetBrains/JetBrainsMono | asset/reference | ADD_TO_RADAR | mono técnica |
| be5invis/Iosevka | D/reference | ADD_TO_RADAR | referência paramétrica; não importar toolchain |
| google/fonts | D/ecosystem | KEEP_EXTERNAL_REFERENCE | ecossistema/distribuição; resolver família específica quando necessário |

## Valor incremental adotado

### Motion direction
O Arsenal já decidia função, paradigma e tecnologia. Faltava uma camada explícita de personalidade do movimento e coreografia multi-elemento. Foi absorvida de LottieFiles sem transformar presets de duração/easing em regra universal.

### Creative web com física verificável
`motion-web` traz uma disciplina útil: movimento procedural deve ter comportamento observável e verificável, não drift aleatório. O princípio entrou na stack; Playwright/scripts da fonte não foram copiados.

### Presentation style discovery
O SlideSpeak formaliza bem a ideia de derivar o sistema visual do briefing/referências em vez de selecionar um tema pronto. Isso entrou em `cinematic-presentation`, preservando template/brand como autoridade quando existente.

### Modern font radar
Repositórios de fontes não justificam skills próprias. O valor está em uma referência curada ligada a `typographic-composition`, com seleção por função, licença, cobertura, loading e eixos variáveis. Geist, Inter, Recursive e IBM Plex formam o núcleo; demais famílias são alternativas especializadas.

## Segurança e portabilidade

- nenhum installer ou script externo foi executado;
- nenhuma API key externa foi requerida;
- dependências MiniMax e fal.ai não foram adotadas;
- verificadores e runtimes de `motion-web` não foram tratados como capacidades disponíveis;
- fontes são referências/assets sujeitos à licença e à verificação de cobertura/formato;
- nenhuma fonte binária foi copiada para o Arsenal.

## Rejeições de duplicação

Não criar:
- nova skill `landing-page-design`, pois `landing-craft` já possui o ownership;
- nova skill `ui-animations`, pois `ui-motion-design`, `gsap-animation` e owners adjacentes já cobrem o runtime;
- nova skill por família tipográfica;
- wrapper do MiniMax ou SlideSpeak sem integração realmente disponível.

## Resultado

Mudanças justificadas:
1. atualizar `ui-motion-design`;
2. atualizar `creative-web-engineering`;
3. atualizar `cinematic-presentation`;
4. atualizar `typographic-composition`;
5. criar `skills/typographic-composition/references/MODERN-FONT-RADAR.md`;
6. registrar esta avaliação.

O `ARSENAL INDEX.md` não precisa de alteração porque nenhum recurso foi criado/renomeado e as descriptions roteáveis permaneceram materialmente iguais.
