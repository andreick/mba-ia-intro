# Loaders e Banco de Dados Vetoriais com LangChain

Exemplos práticos de ingestão, armazenamento e busca de dados em bancos vetoriais usando LangChain.

## Exemplos

### [1-web-loader.py](1-web-loader.py)
Carregamento de dados a partir de páginas web.

**Características:**
- Uso de loaders para extrair texto de URLs
- Pré-processamento de dados para ingestão
- Ideal para aplicações de busca e análise de conteúdo web

```bash
python 5-loaders-e-banco-de-dados-vetoriais/1-web-loader.py
```

### [2-pdf-loader.py](2-pdf-loader.py)
Carregamento de dados a partir de arquivos PDF.

**Características:**
- Extração de texto de PDFs usando loaders
- Preparação de dados para armazenamento vetorial
- Útil para indexação de documentos

```bash
python 5-loaders-e-banco-de-dados-vetoriais/2-pdf-loader.py
```

### [3-ingestion-pgvector.py](3-ingestion-pgvector.py)
Ingestão de dados em um banco vetorial (pgvector).

**Características:**
- Armazenamento de embeddings em banco PostgreSQL com pgvector
- Integração entre loaders e banco vetorial
- Preparação para buscas semânticas

```bash
python 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
```

### [4-search-vector.py](4-search-vector.py)
Busca semântica em banco vetorial.

**Características:**
- Consulta de dados usando similaridade vetorial
- Recuperação de documentos relevantes
- Demonstração de busca baseada em embeddings

```bash
python 5-loaders-e-banco-de-dados-vetoriais/4-search-vector.py
```

## Conceitos Aprendidos
- **Loaders:** Extração de dados de fontes diversas (web, PDF)
- **Banco vetorial:** Armazenamento e busca de embeddings
- **Ingestão de dados:** Pipeline de preparação e armazenamento
- **Busca semântica:** Recuperação de informações por similaridade
