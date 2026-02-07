# Agentes e Ferramentas com LangChain

Exemplo prático de criação de um agente do tipo ReAct com ferramentas customizadas usando LangChain.

## Exemplos

### [1-agent-react-tools.py](1-agent-react-tools.py)
Agente ReAct que utiliza ferramentas customizadas para responder perguntas, incluindo uma calculadora simples e uma busca simulada de capitais de países.

**Características:**
- Implementação de ferramentas customizadas com o decorator `@tool`
- Exemplo de agente ReAct com prompt estruturado
- Uso de `AgentExecutor` para execução do agente
- Integração de múltiplas ferramentas (calculadora e busca mockada)
- Limite de iterações e tratamento de erros de parsing

```bash
python 3-agentes-e-tools/1-agent-react-tools.py
```

## Conceitos Aprendidos
- **Agentes ReAct:** Estrutura de agentes que alternam entre pensamento, ação e observação.
- **Ferramentas customizadas:** Criação de funções utilitárias integradas ao agente.
- **Prompt estruturado:** Definição clara do fluxo de raciocínio do agente.
- **Execução controlada:** Limite de iterações e tratamento de erros.
