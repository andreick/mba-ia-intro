# Fundamentos do LangChain

Exemplos básicos demonstrando diferentes formas de inicializar e usar modelos de chat com LangChain.

## Exemplos

### [1-hello-world.py](1-hello-world.py)
Inicialização direta usando `ChatOpenAI` com OpenRouter.

**Características:**
- Uso do modelo `meta-llama/llama-3.3-70b-instruct:free`
- Configuração manual da URL base e API key
- Ideal para entender a estrutura básica

```bash
python 1-fundamentos/1-hello-world.py
```

### [2-init-chat-model.py](2-init-chat-model.py)
Inicialização simplificada usando `init_chat_model`.

**Características:**
- Uso do modelo `gemini-2.5-flash` do Google
- Abstração de configuração via função helper
- Facilita a troca entre diferentes provedores

```bash
python 1-fundamentos/2-init-chat-model.py
```

## Conceitos Aprendidos

- Inicialização de modelos de chat
- Invocação básica de mensagens
- Integração com diferentes provedores (OpenRouter, Google Gemini)
- Duas abordagens: configuração direta vs. função helper
