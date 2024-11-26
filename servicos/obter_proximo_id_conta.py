from servicos import obter_contas

def executar():
    """
        - abrir e ler os dados - ok
        - pegar a ultima linha do arquivo
        - pegar o id da linha
        - incrementar + 1 no id
        - retornar
    """
    contas = obter_contas.executar()

    if len(contas) == 0:
        return '1'

    ultima_conta = contas[-1]
    proximo_id = int(ultima_conta.get("id", 0)) + 1
    return str(proximo_id)