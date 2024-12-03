# Gerenciador de contas a pagar e receber
Sistema para controle financeiro pessoal. Registros de despesas e receitas, consultas avançadas, atualização de dados e geração de relatórios.

# Funcionalidades
- Criar (Create):
    - Registro de contas.
    - Informações a serem salvas:
        - Tipo: Crédito ou Débito.
        - Descrição: Ex.: "Conta de luz", "Salário".
        - Valor: Quantia em moeda local.
        - Data de vencimento.
        - Data de recebimento.
        - Categoria: Ex.: "Alimentação", "Moradia", "Lazer".
        - Status: Pago, Recebido ou Pendente.
- Ler (Read):
    - Visualização de uma lista das contas registradas, com filtros por:
        - Tipo (Crédito/Débito)
        - Status (pago, pendente, cancelado)
        - Todos
- Atualizar (Update):
    - Alteração de qualquer informação previamente registrada.
- Excluir (Delete):
    - Remoção de contas registradas.
    - Opção de confirmação para evitar exclusões acidentais.
- Gerar relatório (PDF) do mês
    - Gerar dados do mês atual com a soma das despesas e receitas
    - Listar as contas utilizadas nos cálculos agrupados por data


## Instalação de bibliotecas

```bash
  pip install pdfkit
  pip install jinja2
```
- [Link de instalação do wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)