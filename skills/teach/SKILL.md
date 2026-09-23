---
name: teach
description: "Organizar aprendizagem em múltiplas sessões com missão, prática de recuperação, espaçamento e progressão registrada."
---

# teach

## Objetivo

Ensinar um tema ao longo de múltiplas sessões, mantendo estado de aprendizado, missão, recursos, registros e progressão pedagógica.

## Workflow

1. Definir missão, conhecimento atual e resultado de aprendizagem.
2. Escolher conteúdo e prática proporcionais ao nível.
3. Ensinar e pedir recuperação ativa.
4. Revisitar conteúdos com spacing e interleaving.
5. Exigir evidência proporcional de domínio antes de marcos importantes.
6. Registrar progresso e próxima sessão quando autorizado.

## Princípios

- Começar pela missão.
- Diferenciar fluência imediata de retenção de longo prazo.
- Usar retrieval practice, spacing e interleaving.
- Ensinar dentro da zona de desenvolvimento proximal.
- Apoiar conhecimento em fontes confiáveis.
- Registrar aprendizados e preferências de ensino quando apropriado.

## Progressão por domínio demonstrado

Quando a jornada tiver módulos, certificação, preparação profissional ou objetivos cumulativos, não usar apenas “conteúdo concluído” como critério de avanço. Construir uma escada de evidências, proporcional ao risco e ao objetivo:

1. **Lesson / worked example** — introduzir o mecanismo com apoio.
2. **Practice** — resolver exercícios curtos variando contexto e dificuldade.
3. **Review / retrieval** — recuperar conceitos anteriores sem reler a solução.
4. **Quiz / check** — verificar compreensão individual e detectar lacunas.
5. **Lab / project** — produzir um artefato que combine várias competências.
6. **Assessment** — quando necessário, avaliar sem scaffolding excessivo e com critérios explícitos.
7. **Progression** — avançar somente quando a evidência corresponde ao resultado de aprendizagem esperado.

Regras:

- não exigir todas as etapas em toda sessão; usar a menor sequência suficiente;
- projeto não substitui automaticamente conhecimento conceitual, e quiz não substitui capacidade de construir;
- avaliações devem testar o que foi ensinado e praticado, não detalhes-surpresa;
- erros em avaliação alimentam revisão direcionada, não reinício indiscriminado do módulo;
- quando houver projeto integrador, definir critérios de aceitação observáveis antes da execução;
- distinguir **completou atividades** de **demonstrou domínio**;
- certificação ou claim forte exige evidência mais forte do que progresso informal.

## Aprender construindo

Para engenharia e computação, considerar uma trilha de reconstrução quando o objetivo for compreensão profunda.

1. Escolher um sistema pequeno o bastante para ser reconstruído.
2. Definir a interface observável que será reproduzida.
3. Implementar o núcleo mínimo antes de adicionar features.
4. Comparar comportamento com a tecnologia real ou com testes conhecidos.
5. Explicar o mecanismo aprendido após cada milestone.
6. Aumentar fidelidade gradualmente: parser → state → runtime → performance, conforme o domínio.
7. Encerrar com reflexão: quais abstrações da tecnologia real agora fazem sentido e quais continuam escondidas.

A reconstrução é ferramenta pedagógica, não autorização para reimplementar sistemas de forma insegura ou infringir licenças.

## Algoritmos como prática

Ao ensinar algoritmos:

- começar por definição, invariantes e complexidade esperada;
- pedir uma implementação pequena e legível;
- usar exemplos normais + edge cases;
- comparar alternativas por tempo, espaço e clareza;
- priorizar correção e compreensão sobre code golf;
- não copiar implementação de catálogo quando o objetivo é o aluno praticar.

## Uso no Arsenal

Uma sessão isolada e uma jornada de aprendizagem têm escopos diferentes. Esta skill organiza a progressão entre sessões.

## Ferramentas e dependências

Usar arquivos locais ou conectores realmente disponíveis. Recursos externos são referências, não dependências obrigatórias.

## Referências

https://github.com/mattpocock/skills/tree/main/skills/productivity/teach

Project-based reconstruction inspirada em https://github.com/codecrafters-io/build-your-own-x.

Prática algorítmica inspirada no ecossistema https://github.com/TheAlgorithms; o link fornecido aponta para a organização, e TheAlgorithms/Python foi usado como amostra representativa.

Progressão lesson → practice → review/quiz → projeto → avaliação inspirada na arquitetura curricular de https://github.com/freeCodeCamp/freeCodeCamp, sem copiar conteúdo curricular nem transformar sua plataforma em dependência.

Origem local: [teach.docx](../teach.docx).
