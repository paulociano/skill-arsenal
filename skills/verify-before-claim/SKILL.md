---
name: verify-before-claim
description: "Verificar afirmações consequenciais de conclusão, correção ou publicação com evidência fresca do escopo afirmado."
---

# verify-before-claim

## Objetivo

Impedir afirmações de conclusão, correção, segurança, publicação, implantação ou outro fato consequencial sem evidência fresca que corresponda exatamente ao escopo da afirmação.

## Princípio central

**Sem evidência, sem afirmação.** Esforço, confiança, execução de ferramenta ou texto fluente não provam sucesso.

## Quando usar

- antes de declarar uma tarefa concluída;
- depois de alterações em código, arquivos, sistemas externos ou configurações;
- antes de dizer que publicação, deploy, envio, gravação ou atualização ocorreu;
- quando a afirmação pode produzir impacto material.

## Workflow

1. Reescrever a conclusão pretendida como uma afirmação falsificável.
2. Classificar o risco como baixo, material ou consequencial.
3. Escolher o check mais barato que teste diretamente essa afirmação.
4. Executar/verificar **depois da última mudança material**.
5. Comparar resultado esperado versus observado.
6. Classificar como `supported`, `partially_supported`, `unsupported` ou `blocked`.
7. Ajustar a linguagem ao escopo realmente verificado.
8. Para ações consequenciais, preservar separação entre execução, aprovação e verificação; exigir rollback quando aplicável.

## Evidência válida

Pode incluir teste direcionado, build, lint, leitura pós-escrita, inspeção de diff, comparação de fonte, status real de ferramenta/conector, consulta de dashboard ou health check.

## Regras

- Check parcial só autoriza conclusão parcial.
- Evidência anterior à última mudança é stale.
- Disparo de automação não prova execução.
- Ausência de erro não prova sucesso.
- Não repetir check idêntico apenas para fabricar confiança.
- Se não houver método direto de verificação, reduzir a afirmação ou declarar evidência insuficiente.

## Integridade de arquivos

Quando a afirmação for sobre **integridade de arquivo/export**, considerar:

- hash de cada artefato;
- manifest com versões, timestamps e estado;
- digest reproduzível do manifest;
- assinatura separada quando provenance forte for necessária;
- versões antigas sem hash devem ser marcadas como **unverifiable**, nunca promovidas a verified;
- chave pública/verificador precisa vir de canal de confiança separado quando assinatura servir para provenance.

Hash prova igualdade de bytes, não autoria, correção semântica ou legitimidade do conteúdo.

## Integração

Pode funcionar como gate final de praticamente qualquer skill do Arsenal.
Para mudanças de código materiais, pode encadear `code-review`. Consenso entre revisores independentes aumenta cobertura, mas **não substitui teste, build, runtime check ou outra evidência objetiva**. Não substitui os checks próprios de `code-review`, `tdd`, `web-design-engineer` ou outras skills; consolida a regra de claim.

## Referências

Adaptada de Mark393295827/third-brain-v7-skills · verify-before-claim (V8.1).

Origem local: [verify-before-claim.docx](../verify-before-claim.docx).
