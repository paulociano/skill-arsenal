---
name: save-game-persistence-engineering
description: "Projetar save/load de jogos com schema versionado, migrations, atomic writes, backups, corruption recovery, async I/O, cloud conflict policy e separação entre state persistente e runtime objects."
---

# Save Game Persistence Engineering

## Objetivo

Persistir estado de jogo de forma reproduzível e evolutiva, tolerando upgrades, interrupções e corrupção sem acoplar o formato salvo à estrutura efêmera da cena.

## Quando usar

- save/load;
- autosave/checkpoints;
- slots;
- cloud save;
- persistent progression;
- narrative state;
- settings/profile;
- migrations entre versões.

## Princípio central

**Salvar dados canônicos, não objetos vivos do runtime.**

## Workflow

1. Inventariar state persistente por domínio.
2. Separar IDs/dados de referências a GameObjects/scene objects.
3. Definir schema e `saveVersion`.
4. Serializar DTO/state explícito.
5. Escrever para arquivo temporário, flush quando necessário, depois substituir atomically quando plataforma suportar.
6. Manter backup/last-known-good proporcional ao risco.
7. Validar checksum/parse/schema antes de aceitar load.
8. Migrar versões em etapas conhecidas.
9. Falha de migration/load deve preservar save original para recuperação.
10. I/O grande deve ser async/background sem bloquear frame thread, respeitando APIs da engine.

## Save boundaries

Separar quando útil:
- profile/account;
- settings;
- world/progression;
- active run;
- narrative;
- inventory/economy;
- transient cache.

Nem tudo precisa ser salvo no mesmo blob.

## Cloud save

Definir:
- revision/etag/version;
- last-write policy;
- mergeable versus non-mergeable fields;
- conflict UI/policy;
- offline queue;
- server authority para economy/competitive state.

Nunca usar timestamp local sozinho como prova de versão correta.

## Migrations

- upgrade forward explícito;
- fixtures de saves antigos;
- migration idempotente quando possível;
- não reserializar silenciosamente antes de validar;
- major schema change exige backup e rollback strategy.

## Security

- save local é input não confiável;
- encryption local pode dificultar casual tampering, mas não cria authority;
- não embutir chaves secretas como proteção confiável;
- competitive/value-bearing state deve ser validado server-side;
- nunca usar DES ou algoritmo legado apenas porque um sample oferece.

## Testes

- clean install;
- missing file;
- truncated/corrupt file;
- old version;
- future/unknown version;
- disk full/write interruption;
- concurrent save;
- autosave during scene transition;
- cloud conflict;
- restore backup.

## Regras

- serialização bem-sucedida não prova recovery;
- scene references não são save IDs;
- autosave precisa de debounce/queue;
- não apagar backup antes do novo save ser validado;
- cloud sync sem conflict policy pode perder progresso.

## Integração

`game-development-engineering`, `narrative-dialogue-engineering`, `live-game-operations-engineering`, `game-networking-engineering`, `secure-code-privacy-review` e `library-version-grounding`.

## Provenance

Consolidada de padrões de unity-save-system, SaveGameFree e story/save format versioning do ink. O Arsenal rejeita como default algoritmos criptográficos legados observados em samples e prioriza schema, atomicity, migrations e recovery.
