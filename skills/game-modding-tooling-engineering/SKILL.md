---
name: game-modding-tooling-engineering
description: "Projetar suporte autorizado a mods/plugins com API estável, manifests, dependency/version contracts, sandbox/permission boundaries, compatibility diagnostics e hooks explícitos antes de recorrer a runtime patching."
---

# Game Modding & Tooling Engineering

## Objetivo

Criar extensibilidade para jogos de forma intencional, versionável e diagnosticável, reduzindo a necessidade de mods dependerem de internals frágeis.

## Quando usar

- plugin/mod API para jogo próprio/autorizado;
- custom content;
- scripting;
- mod manifests;
- compatibility/versioning;
- mod loader;
- editor/runtime tooling para creators.

Não usar esta skill para burlar anti-cheat, DRM, licenças, controles de acesso ou modificar software sem autorização.

## Princípio central

**Prefira extension points suportados a patching de internals.**

## Workflow

1. Definir superfície extensível:
   - data/content;
   - UI;
   - gameplay hooks;
   - scripts;
   - assets;
   - server-side extensions.

2. Criar mod manifest:
   - id;
   - version;
   - game/API version range;
   - dependencies;
   - load order apenas quando necessário;
   - capabilities/permissões.

3. API pública:
   - contracts estáveis;
   - events/hooks explícitos;
   - context objects mínimos;
   - deprecation window;
   - feature detection.

4. Loader:
   - discovery;
   - dependency resolution;
   - deterministic load order;
   - isolation/failure reporting;
   - disable individual mod sem derrubar o jogo quando possível.

5. Config/logging:
   - namespace por mod;
   - structured diagnostics;
   - não expor secrets;
   - logs devem indicar owner/mod origin.

6. Content safety:
   - tratar mod files como input não confiável;
   - paths normalizados;
   - evitar arbitrary file/network/process access quando scripting não precisa;
   - signed/curated distribution é opção, não garantia total.

7. Compatibility:
   - API semantic version;
   - explicit breaking changes;
   - migration guide;
   - compatibility test fixtures;
   - mod list/version incluída em bug reports.

8. Runtime patching:
   - último recurso em ecossistema autorizado;
   - patch mínimo e version-gated;
   - conflito entre patches precisa de diagnóstico;
   - não tratar Harmony/IL patching como API de produto ideal.

9. Multiplayer:
   - separar client-only mods de server-authoritative mods;
   - handshake de mod/version quando gameplay state muda;
   - servidor pode exigir allowlist/mod parity;
   - não confiar em client mod para regra competitiva.

10. Verify
   - clean game sem mods;
   - um mod;
   - múltiplos mods;
   - dependency missing;
   - incompatible version;
   - exception during load;
   - uninstall/disable;
   - save compatibility.

## Regras

- mod support oficial deve minimizar dependência em private internals;
- plugin crash não deve corromper save;
- mod script sem sandbox é code execution com todos os riscos correspondentes;
- não carregar binário desconhecido apenas para “inspecionar” mod;
- permissões precisam ser proporcionais.

## Integração

`game-development-engineering`, `save-game-persistence-engineering`, `secure-code-privacy-review`, `skill-security-review`, `library-version-grounding` e `game-networking-engineering`.

## Provenance

Consolidada de BepInEx, Harmony e ecossistemas de plugin/modding .NET/Unity. O Arsenal absorve loader, config/logging, compatibility e hooks, mas prioriza APIs oficiais e limita runtime patching a contextos autorizados.
