# Motores, decisões e trade-offs

| Motor | Caso | Dependência | Limitação |
| --- | --- | --- | --- |
| Potrace | logomarca e silhueta 1-bit | executável potrace | não preserva cores nativamente |
| VTracer | ícones binários e ilustrações coloridas | executável vtracer | ajustes podem criar muitos nós |
| OpenCV fallback | ícone simples e ambiente limitado | opencv-python, Pillow, NumPy | polígonos de segmentos retos, não Bézier |
| SVGO | pós-processamento SVG | Node e svgo (opcional) | otimização agressiva pode alterar geometria |

O helper Python presente foi testado com OpenCV; Potrace/VTracer são integrações condicionais **não testadas neste ambiente**. Verifique opções de CLI na versão instalada antes de confiar nos flags. Execute o SVG em renderizador isolado e valide visualmente. Em imagens com alfa parcial, a máscara usa threshold de alfa e perde semitransparências: documentar ao usuário. Não presumir licença de uso de logos de terceiros.

Testes: `python -m pytest tests/test_vectorize.py -q`.
