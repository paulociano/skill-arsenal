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


## Revisão SwiftUI completa (fonte: twostraws/SwiftUI-Agent-Skill)

### Gatilho e escopo
Ativar para escrita, manutenção ou auditoria de projetos **SwiftUI nativos**. Para mudança pontual, verificar só as dimensões relevantes; para auditoria completa, percorrer todas as dimensões abaixo. Não aplicar regras de SwiftUI a Flutter/React Native. Ao corrigir um bug, não aproveitar para migrar arquitetura ou API não relacionada.

### Sequência operacional
1. Identificar Xcode, Swift, SDK, deployment targets, módulos, testes, configurações de compilação e convenções do código; **não assumir versões citadas pela fonte externa como instaladas**.
2. Inspecionar documentação oficial/SDK para cada API nova, renomeada ou soft-deprecated antes de propor substituição. Separar disponibilidade por **SDK compilador** e por **sistema operacional em runtime**; `#available` não resolve símbolo desconhecido pelo compilador.
3. Revisar **APIs e views**: deprecações explícitas ou suaves, `Tab` vs `tabItem`, `tint`, `foregroundStyle`, `clipShape`, `#Preview`, uso desnecessário de `GeometryReader`, ações e lógica fora de `body`, extração de subviews quando há ganho claro. Não tratar preferência estilística como defeito.
4. Revisar **estado e dados**: ownership e ciclo de vida de `@State`, bindings, `@Observable`, isolamento de ator quando aplicável, separação entre modelos e UI, SwiftData/CloudKit quando presentes. Respeitar legados e evitar migrações automáticas de `ObservableObject` e `@StateObject` sem justificativa.
5. Revisar **navegação e apresentações**: `NavigationStack`/`NavigationSplitView`, destinos tipados, evitar registros conflitantes, sheet/alert/dialog com estado consistente, testes de dismiss e restoration.
6. Revisar **responsividade e design**: adaptação por espaço disponível, tamanho dinâmico, safe areas, mudanças de janela, multitarefa iPad, layout ao redor de sensores/dobras quando houver suporte real; manter funcionalidades em todas as dimensões. Preferir controles nativos e garantir alvos de toque adequados.
7. Revisar **acessibilidade**: Dynamic Type, VoiceOver, Voice Control, labels para botões de ícone, ordem de foco, contraste, diferenciação sem depender só de cor, Reduce Motion, estados vazio/erro e ações acessíveis.
8. Revisar **localização**: preservar `.strings`/`.stringsdict`/`.xcstrings` atuais, `LocalizedStringResource` quando aplicável, bundle correto em módulos, contexto de tradução, formatação por locale/calendar/timeZone vindos do ambiente.
9. Revisar **performance**: identidade estrutural das views, trabalho em `body`/initializers, filtros em listas, carregamento remoto de imagens, cancelamento de tasks e comportamento com mudanças frequentes. **Perfil e evidência antes de micro-otimizar**. Carregar critérios avançados de separação de dependências observáveis apenas se houver problema demonstrado ou solicitação de revisão profunda.
10. Revisar **Swift e higiene**: concurrency/cancelamento, optionals, erros, formatação localizada, armazenamento seguro no Keychain em vez de `@AppStorage` para segredos, testes de lógica e de fluxos críticos, warnings, launch-screen/build settings conforme SDK confirmado.
11. Produzir findings **por arquivo e linha**, regra violada, impacto, evidência e exemplo mínimo antes/depois quando útil; priorizar por severidade e não listar arquivos sem findings. Distinguir revisão estática de build/testes/previews realmente executados.

### Portabilidade e critérios de segurança
- Preferir ambiente Apple/Xcode e documentação Apple quando efetivamente disponíveis; não declarar que `RenderPreview`, `DocumentationSearch` ou Xcode MCP estão conectados sem verificação.
- Nenhum installer ou plugin externo é necessário. Não executar scripts da skill de origem.
- Não remover fallback nem aumentar deployment target silenciosamente.
- Não criar dependências terceiras ou trocar UIKit/SwiftUI por preferência sem requisito.
- Regras como “um tipo por arquivo”, escolhas de formatação e API mais recente são **heurísticas**, não findings automáticos sem impacto, contexto ou convenções verificadas.
- Versões/hardware mencionados por fontes externas (inclusive iOS 27, Xcode 27 e iPhone Duo) devem ser verificados no ambiente e documentação oficiais antes de recomendar comportamento específico.

### Testes de aceitação da skill
- **Should-trigger:** auditoria SwiftUI que identifica bugs de estado, VoiceOver e compatibilidade com deployment target com arquivos/linhas comprováveis.
- **Near-miss:** projeto Flutter/Expo ou ajuste apenas de layout HTML; não aplicar este checklist.
- **Falha a evitar:** recomendar um modificador presente em SDK posterior sem verificar Xcode; tratar otimização hipotética como correção necessária.
- **Resultado esperado:** findings priorizados, patch restrito ao escopo e relatório de testes realizados versus não realizados.

### Provenance
Metodologia adaptada após leitura do `SKILL.md` e das 12 referências (accessibility, api, data, design, hygiene, localization, navigation, performance, performance-plus, resizability, swift, views) em https://github.com/twostraws/SwiftUI-Agent-Skill/tree/main/swiftui-pro. Não incorpora regras absolutas sem contexto nem presume integração do agente original.
