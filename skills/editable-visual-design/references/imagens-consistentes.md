# Referências e validação de imagens

Complemento de editable-visual-design para peças com raster gerado ou editado. Para imagem isolada, usar diretamente a ferramenta nativa, sem iniciar um workflow de canvas editável.

## Contrato visual

1. Definir função do asset, proporção do slot, enquadramento, região livre para texto e elementos que devem sobreviver ao crop.
2. Separar atributos fixos (personagem, produto, paleta, luz e acabamento) de variáveis (ação, cenário ou enquadramento).
3. Associar cada referência a uma função: identidade do sujeito, estilo ou composição. Inspecionar as referências disponíveis; não afirmar uso de referência ausente.
4. Para edição, identificar imagem-base, mudança desejada e elementos a preservar. Enviar a referência pelo mecanismo suportado pela ferramenta.
5. Descrever sujeito, estilo, composição e atmosfera com restrições concretas. Preservar a marca existente em vez de copiar paletas genéricas.

## Séries sem deriva

- Usar uma imagem adequada como âncora; na ausência dela, produzir e inspecionar a primeira antes das dependentes.
- Reutilizar a âncora estável nas demais imagens, evitando uma cadeia em que cada resultado alterado vira a única referência do seguinte.
- Registrar por asset: função, referência utilizada, variação, resultado escolhido e correção pendente. Não incluir credenciais.
- Paralelizar apenas itens independentes depois de definir a direção comum e se a ferramenta permitir.
- Revisar lado a lado identidade, paleta, iluminação, proporção e crop. Referência reduz deriva, mas não garante identidade perfeita.
- Corrigir somente falhas observadas; parar quando o contrato estiver atendido.
- Manter texto factual em camada editável e verificar sua legibilidade no render.

## Capacidades reais

Priorizar a ferramenta nativa de geração/edição. Não instalar CLI/MCP, pedir chaves ou trocar de provedor apenas porque a fonte externa usa esse caminho. Não presumir suporte a máscaras, alpha, dimensões exatas, seed ou quantidade de referências.

Se uma integração externa autorizada for necessária, verificar parâmetros e credenciais pelo mecanismo seguro do ambiente. Para operações cobradas, respeitar orçamento e autorização existentes; obter estimativa quando disponível e pedir decisão apenas se custo ou escopo ainda não estiverem autorizados. Não persistir chaves em código, prompts ou perfil de shell.

Em operações assíncronas reais, preservar o identificador retornado, consultar a mesma tarefa até estado terminal dentro de prazo finito e não reenviar automaticamente uma geração de status incerto. Não inventar identificadores ou polling para ferramentas que não os exponham.

## Entrega verificada

Quando houver arquivo local necessário ao artefato:
- abrir/decodificar o arquivo e verificar formato real, dimensões e integridade; extensão ou MIME declarado não bastam;
- alinhar extensão ao formato detectado; não chamar renomeação de conversão nem assumir PNG para tipo desconhecido;
- verificar alpha real quando transparência for requisito; fundo quadriculado desenhado não prova transparência;
- preservar originais e resultados escolhidos com nomes distintos;
- revisar no tamanho e crop de uso.

Quando o ambiente já exibir e salvar a imagem gerada, usar o retorno nativo. Não baixar ou duplicar apenas para redistribuí-la. ID de tarefa, URL ou mensagem de sucesso isolados não provam qualidade visual nem export correto.

## Proveniência

Síntese autoral das capacidades discutidas na [avaliação dos geradores de imagem](../../../evaluations/2026-09-21-image-generation-skills.md). Não inclui código, instaladores, bundles ou templates das fontes.
