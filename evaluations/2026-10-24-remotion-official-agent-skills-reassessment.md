# Reavaliação — Remotion Agent Skills (2026-10-24)

## Evento e baseline
- Origem oficial: https://www.remotion.dev/docs/ai/skills (página atualizada em 2026-10-23).
- Código oficial: https://github.com/remotion-dev/skills.
- Avaliação anterior: [2026-10-15-remotion.md](2026-10-15-remotion.md): classe D, runtime React/TypeScript e metodologia absorvida em `video-editing-pipeline`.
- Gatilho **SOURCE_CHANGED**: catálogo oficial de doze Agent Skills com responsabilidades específicas, não apenas documentação geral do framework.

## Capacidade incremental e ownership
As funções oficiais incluem `remotion-best-practices`, `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade` e `remotion-multimedia`.

**Classificação A/D** para o conjunto como roteamento operacional valioso, porém dependente de runtime e versão Remotion. **Decisão UPDATE_EXISTING**, não criar skill concorrente. Owner: `skills/video-editing-pipeline/SKILL.md`, seção 'Roteamento para Agent Skills oficiais Remotion'. `remotion-docs` reduz risco de API desatualizada; `remotion-interactivity` destaca editabilidade diferente de simples render; `remotion-maps` introduz especialização com dados, licenças e custo próprios.

## Segurança, portabilidade e verificação
- **CAUTION** para instalação via `npx skills` ou GitHub CLI, scripts externos, Node/build, APIs/chaves, licença Remotion comercial, assets e dados potencialmente sensíveis no bundle ou cloud render.
- Não foram instaladas Agent Skills, dependências, bibliotecas ou infraestrutura; não houve execução do Studio/render nem validação de saída MP4.
- Usar a instrução oficial atual como referência sob demanda e selecionar apenas componentes necessários.
- **Should trigger:** projeto Remotion existente que requer legendas editáveis e render vertical.
- **Near miss:** simples corte/transcode MP4, que não precisa Remotion.
- **Failure path:** runtime ausente ou incompatível: não declarar teste, render ou arquivo pronto.

## Publicação
- Owner modificado: `skills/video-editing-pipeline/SKILL.md`.
- Commit de implementação: `cac8ea37fb08227041e3d1accee14da6f7cfc311`.
- Sem novo owner nem alteração material de description; `ARSENAL INDEX.md` permanece igual.
- Evidência limitada à documentação oficial e leitura estrutural dos repositórios; sem auditoria de scripts ou benchmarking.
