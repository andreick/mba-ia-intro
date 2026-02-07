# Introdução ao LangChain

Repositório de estudos e exemplos práticos de LangChain, explorando diferentes funcionalidades e casos de uso.

## Configuração

### 1. Instalar dependências
```bash
uv sync
```

### 2. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:
```bash
cp .env.example .env
```

Configure suas chaves de API:
- `OPENROUTER_API_KEY`: Chave da API do OpenRouter
- `GEMINI_API_KEY`: Chave da API do Google Gemini

## Estrutura do Projeto

### [1-fundamentos/](1-fundamentos)
Exemplos básicos de inicialização e uso de modelos de chat com diferentes provedores.

### [2-chains-e-processamento/](2-chains-e-processamento)
Exemplos de criação e composição de chains para processamento de dados e prompts.

### [3-agentes-e-tools/](3-agentes-e-tools)
Exemplo de agente ReAct com ferramentas customizadas (calculadora e busca de capitais).

## Executando os Exemplos

Cada pasta contém seu próprio README com instruções específicas de execução.
