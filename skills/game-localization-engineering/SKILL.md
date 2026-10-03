---
name: game-localization-engineering
description: "Projetar e validar localization de jogos com stable keys, locales/fallbacks, plural/gender variables, localized assets, pseudo-localization, import/export, font coverage, layout QA e versionamento compatível com conteúdo."
---

# Game Localization Engineering

## Objetivo

Tratar localization como pipeline de dados, assets e QA integrado ao jogo, não como substituição tardia de strings.

## Quando usar

- múltiplos idiomas/regiões;
- string tables;
- pluralization/gender;
- localized assets;
- XLIFF/CSV/Sheets;
- pseudo-localization;
- font/script coverage;
- localized dialogue/UI.

## Workflow

1. **Locale model**
   - locale ids;
   - regional variants;
   - default;
   - fallback chain;
   - user override versus system locale.

2. **Stable keys**
   - key semântica/ID estável;
   - texto source não deve ser key primária se muda frequentemente;
   - ownership por feature/content domain.

3. **Message format**
   - placeholders tipados;
   - plural;
   - select/gender quando necessário;
   - number/date/currency formatting por locale;
   - não concatenar fragmentos que tradutor precisa reordenar.

4. **Assets**
   - texture/audio/video/font por locale quando necessário;
   - fallback;
   - memory/loading policy;
   - release/content version compatível.

5. **Pseudo-localization**
   - expandir texto;
   - acentos/caracteres;
   - RTL simulation quando aplicável;
   - detectar hardcoded strings e clipping antes da tradução real.

6. **Font/script coverage**
   - glyph coverage;
   - fallback fonts;
   - CJK/Arabic/Devanagari/etc conforme escopo real;
   - shaping/RTL dependem do renderer/plataforma e precisam ser testados.

7. **Import/export**
   - XLIFF/CSV/Sheets ou TMS;
   - preservar key, notes/context e placeholders;
   - merge não deve apagar traduções sem diff/approval.

8. **Narrative/audio**
   - dialogue line IDs estáveis;
   - voice asset association;
   - subtitle timing;
   - localized audio pode alterar duração e layout.

9. **QA**
   - missing key;
   - fallback;
   - overflow/clipping;
   - RTL;
   - controller glyphs;
   - plural cases;
   - locale switching;
   - save/profile persistence.

10. **Release**
    - translation version;
    - source freeze window quando necessário;
    - late-string policy;
    - content hotfix precisa manter key compatibility.

## Regras

- localization não é traduzir UI no final;
- string concatenation é risco;
- pseudo-localization deve acontecer cedo;
- fallback silencioso pode esconder cobertura incompleta, então métricas/logs de missing são úteis;
- locale do jogo e região de billing/server não são a mesma coisa.

## Integração

`narrative-dialogue-engineering`, `game-ui-accessibility-engineering`, `game-audio-engineering`, `game-build-release-engineering`, `save-game-persistence-engineering` e `locale-adapter`.

## Provenance

Consolidada do Unity Localization package: string/asset localization, Smart Strings, pseudo-localization e import/export XLIFF/CSV/Google Sheets. Adaptada para um owner engine-agnostic.
