# Chains e Processamento com LangChain

Exemplos práticos de criação e composição de chains, demonstrando diferentes formas de combinar componentes do LangChain.

## Exemplos

### [1-chains.py](1-chains.py)
Composição simples de uma chain usando o operador pipe (`|`).

**Características:**
- Uso do operador pipe para compor PromptTemplate e ChatOpenAI
- Chain simples com entrada de variáveis
- Demonstra a sintaxe básica de composição
- Invocação com `.invoke()`

```bash
python 2-chains-e-processamento/1-chains.py
```

### [2-chains-decorator.py](2-chains-decorator.py)
Chain com processamento customizado usando o decorator `@chain`.

**Características:**
- Decorator `@chain` para transformar uma função em um componente reutilizável
- Composição de múltiplos componentes: função → PromptTemplate → Model
- Processamento intermediário (cálculo matemático) antes do prompt
- Demonstra fluxo de dados através da chain

```bash
python 2-chains-e-processamento/2-chains-decorator.py
```

### [3-runnable-lambda.py](3-runnable-lambda.py)
Envolvimento de funções Python simples em um Runnable.

**Características:**
- `RunnableLambda` para converter funções em Runnables
- Processamento de dados sem dependência de modelos de IA
- Útil para transformação e validação de dados
- Integração fácil com chains maiores

```bash
python 2-chains-e-processamento/3-runnable-lambda.py
```

### [4-chains-pipeline.py](4-chains-pipeline.py)
Pipeline complexo com múltiplas transformações encadeadas.

**Características:**
- `StrOutputParser` para converter saída do modelo em texto simples
- Múltiplas chains compostas em um pipeline sequencial
- Uso de dicionários para mapeamento de entradas entre estágios
- Fluxo: Tradução → Resumo (2 transformações encadeadas)
- Demonstra processamento em múltiplos estágios de um documento

```bash
python 2-chains-e-processamento/4-chains-pipeline.py
```

## Conceitos Aprendidos

- **Pipes e Composição**: Uso do operador `|` para compor componentes
- **Runnables**: Entidade base do LangChain para criar fluxos de processamento
- **Decorator @chain**: Transformar funções Python em componentes de chain
- **RunnableLambda**: Converter funções simples em Runnables reutilizáveis
- **Output Parsers**: `StrOutputParser` para converter saída de modelos em texto simples
- **Fluxo de Dados**: Como dados fluem através de componentes compostos
- **Processamento Intermediário**: Adicionar lógica customizada entre componentes
- **Pipelines Complexos**: Criar pipelines com múltiplos estágios de transformação
- **Mapeamento de Entradas**: Usar dicionários para mapear dados entre componentes
- **Invocação de Chains**: Execução de chains com `.invoke()`
