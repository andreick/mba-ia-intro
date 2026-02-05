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

### [3-promp-template.py](3-promp-template.py)
Uso de `PromptTemplate` para gerar texto com variaveis.

**Caracteristicas:**
- Template com `input_variables`
- Formatação simples com `.format()`
- Ideal para prompts reutilizaveis

```bash
python 1-fundamentos/3-promp-template.py
```

### [4-chat-prompt-template.py](4-chat-prompt-template.py)
Uso de `ChatPromptTemplate` para montar mensagens de chat.

**Caracteristicas:**
- Sistema e usuario separados
- Montagem de mensagens com `.format_messages()`
- Integracao com `ChatOpenAI`

```bash
python 1-fundamentos/4-chat-prompt-template.py
```

## Conceitos Aprendidos

- Inicialização de modelos de chat
- Invocação básica de mensagens
- Integração com diferentes provedores (OpenRouter, Google Gemini)
- Duas abordagens: configuração direta vs. função helper
- Templates de prompt (texto e chat)
