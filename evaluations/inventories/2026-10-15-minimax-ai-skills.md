# Inventário individual verificável: MiniMax-AI/skills

Data: 2026-10-15. 23 arquivos SKILL.md encontrados. Base main. Truncada: false.

**Limite:** classificação automatizada com base no caminho, não leitura/auditoria individual do arquivo. Todas as decisões são provisórias. As entradas do VoltAgent e os snippets 30-seconds não estão nesta árvore como SKILL.md; devem ser inventariados na fonte de referência, e não presumidos como avaliados.

| # | Origem | Classe preliminar | Revisão pendente | Hipótese |
|---:|---|---|---|---|
| 1 | [pr-review](https://github.com/MiniMax-AI/skills/blob/main/.claude/skills/pr-review/SKILL.md) | B/D | REVIEW_OVERLAP | compare to quality/security owners |
| 2 | [color-font-skill](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/color-font-skill/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 3 | [design-style-skill](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/design-style-skill/SKILL.md) | B/D | REVIEW_OVERLAP | compare to creative/UI/media owners |
| 4 | [ppt-editing-skill](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/ppt-editing-skill/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 5 | [ppt-orchestra-skill](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/ppt-orchestra-skill/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 6 | [slide-making-skill](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/slide-making-skill/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 7 | [android-native-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/android-native-dev/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 8 | [buddy-sings](https://github.com/MiniMax-AI/skills/blob/main/skills/buddy-sings/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 9 | [flutter-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/flutter-dev/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 10 | [frontend-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/frontend-dev/SKILL.md) | B/D | REVIEW_OVERLAP | compare to creative/UI/media owners |
| 11 | [fullstack-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/fullstack-dev/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 12 | [gif-sticker-maker](https://github.com/MiniMax-AI/skills/blob/main/skills/gif-sticker-maker/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 13 | [ios-application-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/ios-application-dev/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 14 | [minimax-docx](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-docx/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 15 | [minimax-multimodal-toolkit](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-multimodal-toolkit/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 16 | [minimax-music-gen](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-music-gen/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 17 | [minimax-music-playlist](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-music-playlist/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 18 | [minimax-pdf](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-pdf/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 19 | [minimax-xlsx](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-xlsx/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 20 | [pptx-generator](https://github.com/MiniMax-AI/skills/blob/main/skills/pptx-generator/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 21 | [react-native-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/react-native-dev/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 22 | [shader-dev](https://github.com/MiniMax-AI/skills/blob/main/skills/shader-dev/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |
| 23 | [vision-analysis](https://github.com/MiniMax-AI/skills/blob/main/skills/vision-analysis/SKILL.md) | B/D | REVIEW_CONTENT | inspect full content and dependencies |

## Leitura de conteúdo individual e decisão (23 skills)

Cada SKILL.md abaixo foi aberto e inspecionado em seu conteúdo principal, incluindo description, workflow e dependências declaradas. Isso **não** equivale a inspeção completa de todos os arquivos references/scripts, nem teste de execução; veredito de segurança da fonte: CAUTION para adoção com runtime externo até revisão específica.

| Skill | Classe | Decisão | Owner | Razão específica |
|---|---|---|---|---|
| pr-review | B | REFERENCE | code-review | Revisão com hard/soft gates, sem runtime nativo garantido |
| color-font-skill | B | REFERENCE | design-direction | Paletas e fontes; preferências visuais não universais |
| design-style-skill | B | REFERENCE | design-direction | Tokens de radius, densidade e estilo; sobreposição |
| ppt-editing-skill | B/D | REFERENCE | research-to-presentation | Edição OpenXML exige ferramentas e verificação de pacote |
| ppt-orchestra-skill | B/D | REFERENCE | research-to-presentation | Orquestração de slides/subagentes exige suporte real |
| slide-making-skill | D | REFERENCE | research-to-presentation | PptxGenJS e QA visual específicos |
| android-native-dev | B/D | REFERENCE | software-engineering-cycle | Kotlin Compose/MD3 com SDK e emulador externos |
| buddy-sings | D | REJECT_GENERAL_IMPORT | synthetic-presenter-video | Integra pet Claude Code e geração musical; dependência sem equivalente geral |
| flutter-dev | B/D | REFERENCE | software-engineering-cycle | Flutter, Bloc/Riverpod e SDK externo |
| frontend-dev | B/D | REFERENCE | creative-web-engineering | Fluxo visual forte, depende de serviços de mídia externos |
| fullstack-dev | B/D | REFERENCE | functional-web-app-builder | Arquitetura e auth já cobertas; comandos externos requerem runtime |
| gif-sticker-maker | B/D | REFERENCE | content-production | GIF a partir de fotos depende de gerador e edição |
| ios-application-dev | B/D | REFERENCE | software-engineering-cycle | SwiftUI/UIKit e SDK Apple dependem de dispositivo/runtime |
| minimax-docx | D | REFERENCE | document production | OpenXML SDK .NET; não é ferramenta nativa ChatGPT |
| minimax-multimodal-toolkit | D | REJECT_GENERAL_IMPORT | content-production | CLI mmx, chave e gastos; não assumir provedores nem --yes |
| minimax-music-gen | D | REFERENCE | content-production | Geração musical depende de MiniMax API, licença e custo |
| minimax-music-playlist | D | REFERENCE | content-production | Personalização depende de histórico e APIs de música |
| minimax-pdf | B/D | REFERENCE | research-to-presentation | Pipelines PDF precisam ferramentas e QA próprios |
| minimax-xlsx | B/D | REFERENCE | financial-analysis-cycle | Edição OpenXML; atenção a fórmulas e artefatos |
| pptx-generator | B/D | REFERENCE | research-to-presentation | PptxGenJS e pipeline editável; não duplicar stack |
| react-native-dev | B/D | REFERENCE | software-engineering-cycle | Expo/RN: versão SDK, build e devices externos |
| shader-dev | A/D | REFERENCE_FUTURE | creative-web-engineering | 36 técnicas GLSL com roteamento útil; aprofundar references antes de adoção |
| vision-analysis | D | REJECT_GENERAL_IMPORT | evidence-claim-verification | Dependência MCP MiniMax; visão interna não equivale a acesso externo |
