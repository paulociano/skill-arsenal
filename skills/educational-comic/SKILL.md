---
name: educational-comic
description: Transformar conteúdo factual, histórico, científico ou instrucional em HQ educativa com objetivos de aprendizagem, roteiro, storyboard por painéis, personagens, prompts visuais e QA factual/narrativo.
---

# Educational Comic

## Objetivo
Converter conhecimento em narrativa sequencial sem deixar a dramaturgia apagar fatos, causalidade ou objetivo pedagógico.

## Quando usar
- história em quadrinhos educativa;
- biografia em quadrinhos;
- explicação científica/histórica em painéis;
- tutorial ou guia ilustrado em linguagem de HQ.

Não use para quadrinho puramente ficcional sem objetivo de ensinar.

## Entradas mínimas
- tema ou fonte;
- público/faixa etária quando relevante;
- objetivo de aprendizagem;
- fatos/claims que não podem ser distorcidos;
- extensão ou formato desejado.

## Workflow
1. Ground: para conteúdo factual, reunir fontes suficientes antes de dramatizar.
2. Learning contract: declarar o que o leitor deve compreender ao final.
3. Fact spine: listar fatos, ordem causal/temporal e limites que a narrativa não pode quebrar.
4. Narrative frame: escolher protagonista, ponto de vista, conflito/pergunta e tom adequados ao público.
5. Characters: separar personagens históricos/reais, compostos permitidos e personagens ficcionais. Não atribuir fala inventada a pessoa real como citação factual.
6. Storyboard: dividir em páginas e painéis; cada painel deve ter função narrativa e/ou pedagógica.
7. Continuity: usar character-continuity quando houver personagens recorrentes.
8. Prompt plan: descrever cena, personagens, ação, composição e continuidade; manter lettering exato fora da imagem quando possível.
9. Generate: usar a capacidade visual real disponível.
10. Editorial assembly: inserir balões, legendas, títulos e fontes em camada controlável quando o formato permitir.
11. QA factual: verificar claims consequenciais; em saúde/ciência usar evidence-claim-verification.
12. QA sequencial: verificar ordem, transições, continuidade, legibilidade e se cada página avança a compreensão.

## Storyboard mínimo por painel
- página/painel;
- função;
- cena/ação;
- personagens e estado;
- texto/diálogo;
- fato ou conceito comunicado;
- referência visual necessária.

## Regras para história real
- distinguir reconstrução narrativa de citação/documento;
- não inventar precisão histórica ausente;
- preservar datas, locais, relações causais e consequências relevantes;
- conteúdo sensível para crianças deve ser verdadeiro sem depender de choque visual.

## Regras para saúde
A HQ pode explicar e educar, mas não deve transformar simplificação em recomendação clínica individual. Claims médicos materiais passam por fonte adequada e verificação antes de serem convertidos em linguagem simples.

## Critério de conclusão
Um leitor do público-alvo consegue reconstruir o conceito central e a sequência essencial sem depender de notas externas, e a dramatização não contradiz a fact spine.

## Origem adaptada
Principalmente JimLiu/baoyu-skills baoyu-comic, com arquitetura observada em jmilinovich/comicgen. Foram preservados análise → storyboard → personagens → prompts → páginas → composição, removendo Bun, scripts próprios, backends específicos, EXTEND.md e convenções de agentes externos.
