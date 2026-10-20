# Avaliação de 12 repositórios: vídeo, programação, recursos e ML

Data: 2026-10-20  
Método: `arsenal-autopilot`, `evaluate-and-import-skill` e revisão proporcional de segurança. Fonte de autoridade: GitHub, `ARSENAL INDEX.md` e owners específicos.

## Resumo

| Fonte | Classificação | Decisão | Owner |
|---|---|---|---|
| https://github.com/adrianoz1/ai-video-cut | D/B | UPDATE_EXISTING: documentar pipeline opcional, direitos/segredos/crop/QA | `stacks/ai-reels-production/STACK.md` |
| https://github.com/thealgorithms | B/C | ALREADY_ABSORBED; organização (não um único repositório), exercícios por implementações | `skills/teach/SKILL.md` |
| https://github.com/codecrafters-io/build-your-own-x | B | ALREADY_ABSORBED, learning-by-rebuilding | `skills/teach/SKILL.md` |
| https://github.com/ripienaar/free-for-dev | B/C | KEEP_EXTERNAL_REFERENCE, ofertas voláteis; conferir fornecedor | diretório externo |
| https://github.com/EbookFoundation/free-programming-books | B | UPDATE_EXISTING: catálogo para descoberta de materiais, acesso/licença/freshness | `skills/teach/SKILL.md` |
| https://github.com/nilbuild/developer-roadmap | B | UPDATE_EXISTING: roadmap por competência, requisitos e marcos demonstráveis | `skills/teach/SKILL.md` |
| https://github.com/ossu/computer-science | B | UPDATE_EXISTING: cobertura de fundamentos CS, sem impor currículo completo | `skills/teach/SKILL.md` |
| https://github.com/kilimchoi/engineering-blogs | B/C | KEEP_EXTERNAL_REFERENCE, curadoria com frescor variável | radar de fontes externas |
| https://github.com/btw-so/open-source-alternatives | B/C | ALREADY_EVALUATED/KEEP_EXTERNAL_REFERENCE, alternativas exigem revisão primária | diretório externo |
| https://github.com/sdmg15/Best-websites-a-programmer-should-visit | C/B | KEEP_EXTERNAL_REFERENCE; repositório arquivado e links sujeitos a expiração | diretório histórico |
| https://github.com/eriklindernoren/ML-From-Scratch | B/D | UPDATE_EXISTING: exemplo educacional em `teach`; não usar como baseline de produção | `skills/teach/SKILL.md` |
| https://github.com/GokuMohandas/Made-With-ML | A/B | ALREADY_ABSORBED como ML production lifecycle; sem duplicar | `skills/ml-production-engineering/SKILL.md` |

## Capabilities e valor incremental

- `teach`: triagem de requisitos e competências, grafo mínimo de dependências, seleção crítica de recursos, checkpoints por domínio e construção gradual; complemento aos padrões de recuperação espaçada e learning-by-building já existentes.
- `ai-reels-production`: exemplo concreto de orquestração local/API para download autorizado, transcrição, highlights, SRT e export 9:16; avaliação do risco de segredos por argumentos, direitos de mídia e validação do crop.
- `ml-production-engineering`: já tinha origem explícita Made-With-ML no arquivo canônico, incluindo data/train/evaluate/serve, tracking e monitoramento. Nenhum novo owner necessário.
- Diretórios genéricos de ferramentas, blogs, livros, free tiers e sites são úteis para descoberta, não aptos a promoção automática a skills.

## Segurança e portabilidade

Avaliação estática e leitura seletiva de metadados e READMEs. Nenhum instalador, download de vídeo, projeto de ML, script de shell ou binário externo foi executado. A triagem **não equivale a auditoria completa** de código ou dependências.

- `ai-video-cut` exige `yt-dlp`, FFmpeg, Python, `jq` e chave OpenAI. Não assumir disponibilidade. Seu README apresenta passagem de chave via argumento, opção desaconselhada por risco de exposição em histórico/processos; preferir secret/env. Direitos de origem, termos de plataforma, cookies e uso de APIs devem ser tratados por projeto.
- `Made-With-ML` traz infraestrutura de ML externa (como Ray/MLflow/Anyscale); nenhuma é intrínseca à skill.
- Catálogos de terceiros não endossam segurança, licenças ou status de links individuais.
- O catálogo `sdmg15` estava marcado archived no GitHub consultado; `ML-From-Scratch` tinha última atualização indicada em 2023. Não assumir atualidade técnica.
- Diretórios de preço/free tier precisam confirmação do fornecedor antes de uso.

## Atualizações publicadas

1. `skills/teach/SKILL.md` — seção de trilhas de estudo técnicas: competências, fontes, prática, marcos, prova de domínio; commit `459f2ea6fbd05d851821437a3bfc1d518096d90e`.
2. `stacks/ai-reels-production/STACK.md` — referência ao pipeline `ai-video-cut` como implementação externa opcional, com segurança/QA; commit `7cce2046f3ade6e749791e81a6eb3ea47b318676`.

`ARSENAL INDEX.md` não requer atualização: os owners e suas descriptions de roteamento não mudaram. Nenhuma skill/stack nova criada. Não houve instalação, deploy ou alteração de projetos consumidores.

## Contexto histórico e limites

A avaliação de 2026-09-20 já cobria TheAlgorithms, Build Your Own X, free-for-dev, open-source-alternatives e Made-With-ML; o documento dessa data demonstra que `teach` e `ml-production-engineering` absorveram as metodologias principais. Este lote evita importação redundante. Leitura de READMEs/metadata é suficiente para decidir o roteamento, não para validar segurança operacional de cada subprojeto ou licença dos links encadeados.
