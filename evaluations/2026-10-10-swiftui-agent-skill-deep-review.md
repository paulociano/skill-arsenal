# Avaliação aprofundada — twostraws/SwiftUI-Agent-Skill

Data: 2026-10-10
Fonte: https://github.com/twostraws/SwiftUI-Agent-Skill
Branch examinada: main
Método: `arsenal-autopilot`; comparação com `skills/swiftui-modern-ui/SKILL.md` e `skills/crossplatform-mobile-engineering/SKILL.md`.

## Cobertura da fonte

Foram lidos `swiftui-pro/SKILL.md` e **todos os 12 documentos de referência** da skill: `accessibility.md`, `api.md`, `data.md`, `design.md`, `hygiene.md`, `localization.md`, `navigation.md`, `performance.md`, `performance-plus.md`, `resizability.md`, `swift.md`, `views.md`. README e estrutura da raiz examinados na triagem do lote. Não foram executados scripts, plugins ou código externo.

## Capacidades, valor e ownership

| Área | Metodologia aproveitada | Decisão |
|---|---|---|
| API/SDK | identificar soft deprecations, diferenciar SDK, deployment target e runtime | UPDATE_EXISTING |
| Estado/dados | ownership e lifecycle de State/Observable, bindings e SwiftData | UPDATE_EXISTING |
| Navegação | destinos tipados, registro e apresentações consistentes | UPDATE_EXISTING |
| Views/Swift | separar lógica e composição, revisão de concorrência, higiene | UPDATE_EXISTING |
| Design/adaptação | layouts por espaço, safe area, janelas redimensionáveis e acessibilidade | UPDATE_EXISTING |
| Localização | recursos existentes, bundle, locale, calendário e timezone | UPDATE_EXISTING |
| Performance | estabilidade de identidade, custo de body/initializers, profiling; revisão avançada só sob evidência | UPDATE_EXISTING |
| Verificação | findings por linha, severidade, exemplo antes/depois, testes disponíveis e limites | UPDATE_EXISTING |

**Owner canônico:** `swiftui-modern-ui`. Existia cobertura de APIs visuais e layout adaptativo, mas faltava um protocolo completo de revisão técnica. A skill `crossplatform-mobile-engineering` continua dedicada a Flutter e React Native/Expo. **Classificação A:** skill útil e portátil quando adaptada. Não há motivo para criar nova skill duplicada.

## Regras deliberadamente não importadas como absolutas

- Versões exatas de iOS/Xcode, disponibilidade de dispositivo dobrável e de APIs novas: sempre verificar com SDK/doc oficial.
- “Sempre” trocar `ObservableObject` por `@Observable`, cada type para arquivo separado, todas as APIs pelo nome mais novo: depende de compatibilidade, impacto e convenções.
- Otimizações profundas de propriedades observadas sem profiling não são etapa padrão.
- Xcode MCP, `RenderPreview` e `DocumentationSearch` são opcionais e nunca presumidos.
- Modernização fora do escopo solicitado não deve virar refatoração silenciosa.

## Segurança e portabilidade

Revisão estática dos textos de instrução e referências: **APPROVE** para metodologia adaptada, **CAUTION** para mecanismos de plugin/instalação e afirmações de SDK específicas do repositório original sem confirmação independente. Não há necessidade de credenciais, acesso a dados privados, execução de installer ou mudança automática de ambiente. A análise não é auditoria integral de qualquer código executável ou de ferramentas futuras.

## Prova de ganho incremental

**Should-trigger:** revisão de projeto SwiftUI com deployment target identificado, cobrindo acessibilidade, dados, navegação e erros de compatibilidade, resultando em findings por linha.
**Near-miss:** interface HTML ou projeto Flutter/React Native.
**Critério:** não reportar deprecações especulativas, não prometer build sem Xcode, não migrar legado por preferência; separar verificação estática e execução.

## Alterações e escopo

Atualizado `skills/swiftui-modern-ui/SKILL.md` com protocolo de revisão completa nas 11 dimensões e gate de versão/segurança. Não foi criada nova skill, nem alterado o índice, porque o nome e a description existentes continuam adequados.

## Limites de validação

A skill foi analisada e integrada por inspeção estática do conteúdo. Não foi executado build/teste de um aplicativo SwiftUI real nem verificada disponibilidade de SDK Apple no ambiente; tais verificações pertencem ao uso da skill em um projeto concreto.
