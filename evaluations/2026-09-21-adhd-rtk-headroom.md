# Avaliação: i-have-adhd, RTK e Headroom

Data: 2026-09-21. Stack evaluate-and-import-skill; revisão de segurança e adaptação com skill-builder. Índice canônico consultado antes da seleção. As três URLs concatenadas foram separadas nos destinos informados.

## Decisão

Atualizar writing-quality com orientação contextual para instruções fáceis de acompanhar e llm-observability-evaluation com critérios de avaliação de compressão. Não criar skill clínica, modo global, proxy, hook ou nova stack. A importação é de metodologia, não de software.

| Fonte | Categoria | Utilidade real | Decisão |
| --- | --- | --- | --- |
| i-have-adhd | B — metodologia | Formatar tarefas com ação inicial pequena, estado visível e menor dispersão; útil quando essa apresentação atende ao leitor | Adaptar em writing-quality; não presumir diagnóstico ou persistência |
| RTK | D — técnica | Binário Rust que filtra saída de comandos; útil em agentes de terminal com muito output repetitivo | Não instalar; incorporar denominadores corretos e recuperação de evidência nos critérios de avaliação |
| Headroom | D — técnica | Biblioteca/proxy/MCP de compressão, recuperação de originais e funções opcionais de memória/roteamento | Não instalar; adaptar avaliação de fidelidade, retenção, cache e custo total |

RTK e Headroom atuam em camadas diferentes e podem coexistir tecnicamente, mas não há evidência nesta tarefa de que combiná-los compense. Compressão dupla precisa de avaliação própria; não criar uma stack automaticamente.

## Revisões e fontes

- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd/tree/839872f9d1cd634fed642b4589ce7226199cc15f) — `839872f9d1cd634fed642b4589ce7226199cc15f`.
- [rtk-ai/rtk](https://github.com/rtk-ai/rtk/tree/b748a5f75563f410103551689097650be7210d99) — `b748a5f75563f410103551689097650be7210d99`.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom/tree/89a58fd1526ba158a1614c35e455e1af0a7033c0) — `89a58fd1526ba158a1614c35e455e1af0a7033c0`.

Leitura realizada:
- i-have-adhd: skills/i-have-adhd/SKILL.md, evals/README.md, LICENSE e árvore do repositório.
- RTK: README.md, docs/guide/resources/savings-explained.md, install.sh, LICENSE e árvore.
- Headroom: README.md, docs/content/docs/limitations.mdx, headroom/telemetry/beacon.py, LICENSE e árvore.
- Arsenal: índice e skills existentes writing-quality e llm-observability-evaluation, além do workflow de avaliação já consultado na sessão.

## i-have-adhd

A fonte é uma skill textual de apresentação, não tratamento ou instrumento diagnóstico. O núcleo útil já se sobrepõe à clareza e concisão de writing-quality; o ganho incremental é explicitar continuidade de estado e ações pequenas em procedimentos.

Não adotar as afirmações generalizantes sobre memória/dopamina como fatos do leitor. Não inferir condição de saúde por interesse no repositório. Remover ativação por slash command, persistência até comando de desligamento, estimativas obrigatórias sem base, limite rígido que prejudique completude e perguntas que devolvam trabalho autorizado ao usuário.

O README de evals descreve isolamento de configurações entre baseline/candidata, mesma cobertura de casos, modelo fixado e custos ausentes como null. Esse método melhora o contrato de comparação; não foram executadas as evals nem demonstrado benefício clínico.

Segurança: **CAUTION para adoção literal**, pelo escopo persistente e pressupostos sobre o usuário; o texto adaptado é contextual. Instaladores/harnesses e hooks opcionais não foram executados nem auditados integralmente.

## RTK

Opera sobre saída de comandos; depende de binário, comandos subjacentes e, para integração automática, mecanismos de interceptação específicos do agente. O README informa que hooks não cobrem todas as ferramentas nativas. Não assumir que esta conversa suporta reescrita de comandos.

A documentação estima tokens por bytes/4. O percentual de bytes removidos não é percentual garantido de tokens reais ou de conta total; distribuição de caracteres, tokenizer, cache e output do modelo importam. Preservar resultados brutos recuperáveis em falha/truncação é útil, mas retenção e recuperação precisam ser testadas no runtime.

Segurança: **CAUTION**. init pode alterar hooks e arquivos de instruções, e a saída bruta arquivada pode conter dados sensíveis. README declara telemetria opt-in; não foi auditado o transporte completo. install.sh consulta release, baixa binário e checksums por HTTPS, verifica SHA-256 por padrão e rejeita caminhos absolutos/parent traversal na listagem do arquivo. Há bypass de checksum, que não foi usado. O script move o binário e executa --version; checksum do mesmo canal não substitui auditoria de procedência. Nenhum payload binário foi baixado/executado e a cadeia de runtime não foi certificada.

## Headroom

Depende de runtime Python/Rust ou SDK, extras e modelos opcionais; proxy encaminha solicitações ao provedor. wrap pode instalar Serena em escopo de usuário; learn pode escrever em arquivos de instruções; memória compartilhada e cache criam persistência. Esses efeitos vão além de reduzir um texto.

O módulo beacon.py confirma BEACON_DEFAULT_ON = True e tratamento de valor não reconhecido que mantém o default. Telemetria local e upload beacon são controles diferentes. A fonte declara beacon de contadores sem prompts/código; o payload e receptor completos não foram auditados nesta avaliação. Não confundir compressão local com ausência de qualquer tráfego.

README e limitations divergem em escopo de código, imagens, RAG e algumas descrições de gates; a página de limites reconhece medições de amostra sintética. Registrar divergência em vez de escolher a promessa mais ampla. Reversibilidade depende de original retido, TTL e acesso real. Percentuais e latências divulgados não foram reproduzidos.

Segurança: **CAUTION**. Não instalar proxy, registrar MCP global, alterar endpoints, mudar esforço do modelo, desativar validações TLS ou aplicar aprendizado a instruções nesta tarefa. Licença não comprova segurança operacional.

## Extração e sobreposição

| Capacidade | Proprietário | Ganho sobre versão anterior |
| --- | --- | --- |
| Passos pequenos e retomada de estado | writing-quality | Orientação contextual para procedimentos, sem modo clínico/persistente |
| Denominador e economia real | llm-observability-evaluation | Distinguir bytes, tokens de entrada/saída e custo total |
| Recuperação e fidelidade | llm-observability-evaluation | Testar erro raro, negação, número exato e original expirado |
| Comparação não contaminada | llm-observability-evaluation | Isolar hooks/config da candidata e separar compressão de esforço/verbosidade/cache |

## Licenças e limites

MIT em i-have-adhd; Apache 2.0 em RTK e Headroom, conforme LICENSE consultadas. Alterações são sínteses autorais com atribuição e revisão fixada, sem copiar código, templates, instaladores ou partes substanciais das fontes.

Validação estrutural: nomes e descriptions preservados; nenhuma mudança de índice necessária. Revisão de cenários: procedimento longo mantém completude; pedido de explicação não vira lista curta compulsória; consultar uma skill não ativa modo permanente; log com falha rara exige evidência; cache expirado não é recuperação comprovada; menos bytes não é conta proporcionalmente menor.

Revisão estática/manual e de coerência. Nenhum benchmark, API paga ou teste de integração foi executado. Não afirmar redução medida de tokens, custo ou latência nesta sessão. Verificar os três arquivos no remoto após publicar.
