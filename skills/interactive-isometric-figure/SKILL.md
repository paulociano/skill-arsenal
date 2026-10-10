---
name: interactive-isometric-figure
description: "Criar ilustrações técnicas isométricas interativas em um HTML/SVG autocontido, com projeção geométrica, controles funcionais, estado observável e verificação de teclado e ponteiro."
---

# Interactive Isometric Figure

## Origem
Metodologia adaptada de https://github.com/MrBongoC/ai-iso-skill (MIT). Não copiar scripts ou instaladores de Claude.

## Quando usar
Quando a entrega for especificamente um objeto/placa isométrica interativa, como calculadora, sintetizador, timer, máquina ou diagrama de produto cujos controles produzem mudanças reais. Para ilustração estática, escolher skill visual simples; para jogo completo, game-development-engineering.

## Contrato
Defina antes de desenhar: objeto, controle pressionado, efeito verificável, superfície de saída e restrição de acessibilidade. Se não houver ação observável, não simule um controle falso.

## Construção
1. Decomponha o objeto em 3–8 volumes prismáticos (x,y,z,width,depth,height).
2. Calcule projeção isométrica: `P(x,y,z)=[(x-y)cos(π/6)+ox,(x+y)sin(π/6)-z+oy]`.
3. Crie faces por matrizes SVG a partir de origem e dois vetores locais. Faça composição de caixas e detalhes sem escrever manualmente polígonos distorcidos para cada face.
4. Renderize de trás para frente, com preenchimentos opacos. Use `vector-effect:non-scaling-stroke` para preservar os traços.
5. Organize um objeto de estado, um render determinístico e uma mesma função de ação para mouse/toque/teclado.
6. Desenhe moldura estilo prancha técnica com identificação, instrução de uso e leitura do estado atual. Ajuste `viewBox` calculando extremos projetados.
7. Priorize HTML/SVG local sem bibliotecas; estilos por tokens CSS, estados focus-visible e reduced motion.
8. Escape qualquer texto externo antes de inserir em SVG/HTML. Evite scripts remotos, permissões, acesso a dados privados, marcas indevidas e HTML fornecido pelo usuário sem sanitização.
9. Verifique clique, teclado, leitura de saída, foco, tamanho mobile, recorte, oclusão e erros de console no navegador disponível.

## Portabilidade
Gere arquivo autocontido quando o ambiente permitir. Se o runtime de chat não permitir executar JS arbitrário, não prometa interação dentro da própria resposta: ofereça HTML baixável ou representação compatível com os controles realmente disponíveis.

## Critério de aceite
O usuário pressiona um controle e observa uma alteração correta do estado/resultado; o objeto mantém projeção e oclusão coerentes em viewport pequeno.
