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

### [5-summarize.py](5-summarize.py)
Resumo direto de um documento longo usando uma chain simples.

**Características:**
- `ChatPromptTemplate.from_template()` para criar prompts simples
- Resumo direto de texto longo sem divisão prévia
- Chain simplificada: Prompt → Model → Parser
- Abordagem direta ideal para textos que cabem no contexto do modelo
- Demonstra caso básico de sumarização

```bash
python 2-chains-e-processamento/5-summarize.py
```

### [6-summarize-map-reduce.py](6-summarize-map-reduce.py)
Padrão Map-Reduce para resumir documentos muito longos em múltiplos estágios.

**Características:**
- `RecursiveCharacterTextSplitter` para dividir textos longos em chunks
- Padrão **Map**: resume cada chunk individualmente com `.map()`
- Padrão **Reduce**: combina todas as resumências em uma única resumência
- Pipeline com múltiplos estágios: divisão → transformação de inputs → map → join → reduce
- Uso de `RunnableLambda` para funções de transformação (`to_inputs`, `join_summaries`)
- Suporte para `.stream()` para obter resultados incrementados
- Ideal para documentos que não cabem no contexto da primeira passada

```bash
python 2-chains-e-processamento/6-summarize-map-reduce.py
```

## Conceitos Aprendidos

- **Composição com Pipes**: Operador `|` para encadear componentes
- **Runnables**: Bloco de construção fundamental para fluxos de processamento
- **Decoradores e Lambdas**: `@chain` e `RunnableLambda` para criar componentes customizados
- **Output Parsers**: Converter saídas de modelos em formatos específicos
- **Text Splitters**: Dividir documentos longos em chunks com tamanho e sobreposição configuráveis
- **Templates de Prompt**: `PromptTemplate` e `ChatPromptTemplate` para prompts reutilizáveis
- **Padrão Map-Reduce**: Processar múltiplos chunks em dois estágios (map e reduce)
- **Streaming**: Obter resultados incrementados com `.stream()`
