---
name: swiftui-modern-ui
description: "Implementar ou revisar SwiftUI adaptativo com APIs nativas compatíveis com o SDK e deployment target reais."
---

# swiftui-modern-ui

## Objetivo

Implementar e revisar SwiftUI moderno com abordagem native-first e adaptive-first, incluindo APIs recentes de apresentação quando a versão real do projeto as suportar.

## Quando usar

Implementar ou revisar SwiftUI adaptativo com APIs nativas compatíveis com o SDK e deployment target reais.

## Workflow

1. Confirmar SDK e deployment target pelo grounding abaixo.
2. Aplicar a ordem de adaptação e preservar estado.
3. Implementar com APIs disponíveis e fallbacks.
4. Executar a verificação de layout e comportamento no ambiente Apple quando disponível; distinguir revisão de execução.

## Princípios

1. **Layout reage ao espaço, não ao nome do dispositivo.**
2. Completar adaptação universal antes de lógica específica de hardware.
3. Preferir containers e APIs nativas a reimplementações visuais manuais.
4. State da aplicação deve sobreviver às mudanças de layout.
5. Não implementar comportamento específico de hardware/plataforma que não possa ser verificado no SDK/simulator disponível.

## Ordem de adaptação

1. layout adaptativo;
2. navegação adaptativa;
3. toolbars/tabs adaptativos;
4. safe areas e conteúdo fold-safe quando aplicável;
5. APIs específicas de hardware somente quando realmente agregarem valor.

## Liquid Glass / APIs visuais recentes

Quando o SDK instalado suportar APIs nativas equivalentes:

- preferir estilos/containers nativos;
- não reconstruir o efeito com pilhas arbitrárias de blur, shadow e material;
- aplicar availability gates e fallback para versões anteriores;
- evitar efeitos caros ou inadequados em superfícies scrolláveis sem evidência de necessidade.

## Grounding obrigatório

Antes de recomendar APIs dependentes de versão:

1. usar `library-version-grounding`;
2. confirmar Swift/Xcode/iOS SDK/deployment target reais;
3. verificar documentação oficial Apple atual;
4. distinguir API disponível no SDK de comportamento que foi realmente testado.

## Regras

- evitar `UIScreen.main.bounds`/device identity para layout comum quando containers resolvem;
- preferir `NavigationSplitView`, layouts adaptativos e system bars quando aplicáveis à versão;
- largura extra deve revelar estrutura útil, não apenas esticar conteúdo;
- comportamento de hinge/fold deve servir interação física específica, não substituir layout responsivo.

## Ferramentas e dependências

Não presumir Xcode, simulator ou device conectados. Se não houver ambiente de execução, limitar-se a revisão/implementação version-grounded e declarar o que não foi verificado.

## Referências

Adaptada de FloWritesCode/fwc-swiftui-skills, especialmente `swiftui-liquid-glass` e `swiftui-iphone-duo`.

Origem local: [swiftui-modern-ui.docx](../swiftui-modern-ui.docx).
