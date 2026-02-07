# Gerenciamento de Memória em LangChain

Exemplos práticos de estratégias para armazenar e gerenciar o histórico de conversas em aplicações com LangChain.

## Exemplos

### [1-in-memory-history.py](1-in-memory-history.py)
Histórico de mensagens armazenado inteiramente em memória, permitindo múltiplas sessões simultâneas.

**Características:**
- Uso de `InMemoryChatMessageHistory` para cada sessão
- Função para recuperar/criar histórico por session_id
- Encapsulamento do chain com `RunnableWithMessageHistory`
- Ideal para protótipos e aplicações sem persistência

```bash
python 4-gerenciamento-de-memoria/1-in-memory-history.py
```

### [2-sliding-window-history.py](2-sliding-window-history.py)
Histórico de mensagens com janela deslizante, limitando o número de mensagens mantidas para controle de contexto e tokens.

**Características:**
- Uso de função `trim_messages` para limitar histórico
- Estratégia de janela deslizante (últimas 3 mensagens)
- Sempre inclui mensagem do sistema para contexto
- Encapsulamento do chain com `RunnableWithMessageHistory`
- Útil para aplicações que precisam controlar o tamanho do contexto

```bash
python 4-gerenciamento-de-memoria/2-sliding-window-history.py
```

## Conceitos Aprendidos
- **Histórico em memória:** Armazenamento simples e rápido, ideal para múltiplas sessões.
- **Janela deslizante:** Controle do contexto enviado ao modelo, evitando excesso de tokens.
- **Gerenciamento de sessões:** Criação e recuperação de históricos por session_id.
- **Integração com chains:** Uso de `RunnableWithMessageHistory` para facilitar o gerenciamento.
