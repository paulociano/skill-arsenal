---
name: crossplatform-mobile-engineering
description: "Implementar ou revisar apps Flutter e React Native/Expo respeitando versões, comportamento nativo e testes por plataforma."
---

# crossplatform-mobile-engineering

## Objetivo

Projetar, implementar e revisar apps móveis cross-platform com Flutter ou React Native/Expo, escolhendo a stack correta, preservando comportamento nativo, desempenho, acessibilidade, testes e release discipline.

## Quando usar

- projeto Flutter/Dart;
- projeto React Native/Expo;
- navegação, estado, formulários, networking, listas, animações, performance e testes;
- upgrades de SDK;
- preparação para App Store/Play Store;
- integração com capacidades nativas.

## Princípio central

**Framework cross-platform não elimina decisões de plataforma.** Compartilhar código é útil, mas performance, permissões, navegação, safe areas, acessibilidade e lifecycle ainda precisam respeitar iOS e Android.

## Roteamento

### Flutter
Usar quando o projeto for Flutter/Dart.
Foco:

- widget composition;
- state management compatível com o projeto;
- routing;
- responsive/adaptive layout;
- rebuild/repaint control;
- DevTools/profile mode;
- widget/unit/integration tests.

### React Native / Expo
Usar quando o projeto for React Native/Expo.
Foco:

- Expo Router ou navegação real do projeto;
- server/client state separados;
- listas/virtualização;
- imagens e mídia;
- Reanimated/gestures quando realmente necessários;
- permissões/capacidades nativas;
- EAS/build/release quando aplicável.

## Workflow

1. **Ground project** — detectar framework, versão instalada, package/lockfiles e plataforma alvo.
2. **Version grounding** — aplicar `library-version-grounding` antes de recomendar APIs específicas.
3. **Read existing conventions** — navegação, state management, styling, tests, build e CI.
4. **Choose native-capable primitives** — preferir soluções que preservem acessibilidade, lifecycle e performance.
5. **Implement smallest coherent change** — evitar introduzir nova biblioteca quando o projeto já resolve com stack existente.
6. **Test**:
   - unit/business logic;
   - component/widget behavior;
   - integração/fluxos críticos;
   - device/simulator quando a conclusão depender de runtime.
7. **Profile before optimizing** — medir jank, startup, rebuild/re-render, memory ou bundle conforme o caso.
8. **Platform pass** — verificar Android/iOS separadamente para safe area, keyboard, permissions, back behavior, dark mode e accessibility.
9. **Release check** — env/config, signing/build variants, crash/error handling e store constraints.
10. **Verify final** — usar `verify-before-claim`.

## Realtime voice, media e tool calls

Para apps Expo/React Native com WebRTC, áudio contínuo, background execution ou ferramentas acionadas por uma sessão de IA:

- assumir que Expo Go pode não suportar módulos nativos necessários; validar em dev build/device real;
- manter API keys e credenciais de provider no servidor, nunca em variáveis `EXPO_PUBLIC_*`;
- tokens expostos ao app devem ter escopo e finalidade próprios; não reutilizar secret do backend;
- lifecycle da sessão deve possuir cancelamento: ao encerrar chamada, abortar lookups/tool calls pendentes quando eles não devam continuar;
- se uma operação precisa sobreviver ao hangup/background, persistir job/estado fora da conexão efêmera;
- tool runner deve validar argumentos, limitar quantidade/tempo e propagar abort signal para requests externos;
- ações consequenciais como mensagem, compra ou mudança de conta exigem confirmação do usuário antes da execução;
- background audio/call é comportamento específico de plataforma e precisa de teste separado por OS;
- autenticação real é obrigatória antes de expor backend de desenvolvimento à internet.

## Regras

- não impor Riverpod, Bloc, Zustand, Jotai, React Query, NativeWind, FlashList ou qualquer lib só porque aparece na fonte;
- detectar primeiro o stack já instalado;
- performance thresholds são metas contextuais, não leis universais;
- não copiar breakpoints fixos de outra app sem validar layout real;
- não tratar Expo Go como prova de compatibilidade com módulos nativos de produção;
- não dizer que algo funciona em iOS e Android sem evidência em ambos quando isso for relevante;
- não migrar navegação/state management em massa sem motivo material.

## Segurança

- permissões móveis devem ser pedidas no contexto de uso;
- biometria, câmera, localização e notificações exigem rationale e handling de denial;
- secrets não devem ficar hardcoded no bundle;
- deep links, auth callbacks e storage sensível precisam de revisão específica.

## Ferramentas e dependências

Não presumir Flutter SDK, Xcode, Android Studio, Expo CLI, EAS, simuladores ou devices. Quando o runtime não estiver disponível, produzir implementação/revisão version-grounded e declarar o que não foi executado.

## Integração

Combina com `runtime-ui-verification`, `mobile-device-automation`, `tdd`, `diagnosing-bugs`, `code-review`, `swiftui-modern-ui` e `compose-performance-audit`.

## Referências

Adaptada de MiniMax-AI/skills, especialmente `flutter-dev` e `react-native-dev`.

Realtime voice/tool lifecycle adaptado de [davidmokos/expo-gpt-live](https://github.com/davidmokos/expo-gpt-live), preservando princípios e não versões específicas de APIs/modelos.

Origem local: [crossplatform-mobile-engineering.docx](../crossplatform-mobile-engineering.docx).
