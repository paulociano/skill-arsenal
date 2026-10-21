# Fila inicial de reavaliação (semente, não inventário completo)

> Registro derivado e incremental. O diretório `evaluations/` tem histórico maior e é a autoridade para decisões antigas. Esta amostra NÃO significa que os demais registros foram triados.

| Candidato / avaliação | Decisão anterior | Condição concreta para reabrir | Estado inicial |
| --- | --- | --- | --- |
| `evaluations/2026-10-21-docling-openhands-automatic1111.md#docling` | KEEP_EXTERNAL_REFERENCE | Parser estruturado ou conector de documentos muda cobertura/QA dos owners locais com caso reproduzível | WATCH |
| `evaluations/2026-10-21-docling-openhands-automatic1111.md#openhands` | UPDATE_EXISTING | Um backend de agentes com isolamento, observabilidade e aprovação é conectado e testado | WATCH |
| `evaluations/2026-10-21-docling-openhands-automatic1111.md#automatic1111` | UPDATE_EXISTING | Backend de difusão acessível fornece seeds, inpainting e parâmetros reproduzíveis reais | WATCH |
| `evaluations/2026-10-21-betterstackhq-ecosystem.md#betterstack-mcp` | UPDATE_EXISTING | Integração Better Stack ativa + pedido/uso repetido revelar gap entre playbook e operação real | READY |
| `evaluations/2026-10-21-obra-superpowers.md#harness-regression` | UPDATE_EXISTING | Falhas reais de roteamento/execução ou testes de regressão entre sessions | WATCH |
| `evaluations/2026-10-19-listmonk-postiz-docling-browseruse-agent-evals.md#postiz` | Verificar arquivo original | Ferramenta de publishing estiver conectada e demanda real de social scheduling justificar owner | WATCH |
| `evaluations/2026-10-20-ostris-ai-toolkit.md#finetuning` | Verificar arquivo original | Ambiente de treino e dataset apropriados estiverem disponíveis; avaliar custo/segurança | WATCH |

**Como usar:** antes de promover READY a TESTING, ler avaliação original e confirmar decisão, risco e owner. O estado READY do Better Stack marca só a ferramenta conectada/verificada em sessão recente; não prova ganho de uma nova skill nem autoriza modificar monitores.

## Observação sobre inventário
Na criação desta stack, a listagem da API do GitHub retornou 209 entradas em `evaluations/`. Não inferir que todas são avaliações de uma fonte ou que já foram totalmente revisitadas. Em execução futura, paginar e normalizar incrementalmente.
