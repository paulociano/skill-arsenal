---
name: crm-data-quality
description: "Auditar e limpar exportações de CRM com deduplicação conservadora, normalização, revisão de conflitos, plano de merge reversível e controle de integridade sem alterar cadastros automaticamente."
---

# CRM Data Quality

## Quando usar
Deduplicar contatos, leads, empresas ou oportunidades; revisar exportações de CRM; preparar migração ou reintegração; resolver cadastros repetidos, campos inválidos e relacionamentos quebrados. Não usar para simples escrita de mensagens comerciais.

## Fluxo
1. Capturar esquema, fonte, data, IDs estáveis, granularidade, convenções regionais, contatos, empresas, negócios, atividades e relacionamentos. Não presumir coluna-chave pelo nome.
2. Produzir backup/export completo antes de qualquer ação destrutiva, incluindo associações, histórico e campos customizados. Para análise de arquivo, não modificar originais.
3. Normalizar email, telefone (E.164 apenas com região explícita), domínio, nome e endereço em colunas derivadas. Documentar transformações; não presumir que emails corporativos equivalem a pessoa.
4. Criar candidatos de duplicidade com bloqueio por sinais fortes, similaridade e verificações negativas. Email ou telefone compartilhado de equipe, família e empresa nunca deve gerar fusão automática. Mesma grafia de nome não prova mesma pessoa.
5. Classificar grupos em confiança alta, revisão humana e não-unir; analisar cada par dentro de um cluster para evitar encadeamento transitivo errado.
6. Escolher registro sobrevivente com regra auditável: integridade, histórico, data e IDs; listar conflitos por campo, valores perdidos, associações órfãs e dados faltantes. Nunca sobrescrever valores preenchidos com vazios; preservar dados relevantes em campos alternativos quando permitido pelo destino.
7. Entregar diagnóstico (quantidade e tipos), amostras mascaradas, CSV de candidatos, decisões de fusão/manutenção, plano de importação ou merge com IDs, riscos e testes.
8. Executar alterações no CRM real somente com integração realmente disponível, autorização explícita, lote-piloto, verificação após escrita e método específico de rollback. Uma exportação não constitui autorização para mutar o sistema.
9. Validar contagens, unicidade, relacionamento contato-empresa, perdas de campos, possíveis falsos positivos e qualidade em amostra rotulada. Se sem base rotulada, não afirmar precisão/recall.
10. Separar dados pessoais e registros sensíveis nos artefatos; usar mínimo acesso e minimizar exposição.

## Portabilidade
Pode ser aplicado com CSV/XLSX, Python/pandas/openpyxl ou conectores autenticados realmente disponíveis. Scripts `dedupe.py` de terceiros não são presumidos instalados nem executados.

## Casos de aceitação
- "No export do CRM tenho três cadastros para a mesma pessoa" -> mapear suspeitas e conflitos sem fusão automática.
- "Preciso de um relatório de vendas semanais" -> usar gestão comercial / análise, não deduplicação.
- Mesmo email `contato@` usado por duas pessoas -> revisão, não merge.
- `A=B` e `B=C` mas `A!=C` -> nunca unir o cluster inteiro sem investigação.

## Fonte
Adaptada da metodologia `crm-data-cleanup` de https://github.com/onewave-ai/claude-skills, revisada em 2026-10-10. Não incorporar instaladores, scripts ou recursos específicos do Claude.
