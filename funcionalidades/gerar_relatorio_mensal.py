from servicos import obter_contas, criar_relatorio_pdf

meses = [
    "Janeiro",
    "Feveiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

def executar(mes):
    mes_texto = meses[int(mes) - 1]
    print(f"** Gerando relatório do mês {mes_texto} **")

    contas = obter_contas.executar()
    dados_relatorio = {
        'titulo': f'Relatório do mes {mes_texto}',
        'valor_total_credito': 0,
        'valor_total_debito': 0,
        'quantidade_pago': 0,
        'quantidade_cancelado': 0,
        'quantidade_pendente': 0,
        'valor_total': 0,
        'contas': []
    }

    for conta in contas:
        data_vencimento_lista = conta.get("data_vencimento").split("/")
        mes_vencimento = data_vencimento_lista[1]

        if mes_vencimento == mes:
            valor = float(conta.get("valor", 0))

            conta.update({"valor": "R$ {:.2f}".format(valor)})
            dados_relatorio['contas'].append(conta)

            if conta.get("tipo") == "crédito":
                dados_relatorio['valor_total_credito'] += valor
            else:
                dados_relatorio['valor_total_debito'] += valor
            
            if conta.get("status") == "pago":
                dados_relatorio['quantidade_pago'] += 1
            elif conta.get("status") == "pendente":
                dados_relatorio['quantidade_pendente'] += 1
            else:
                dados_relatorio['quantidade_cancelado'] += 1

    if len(dados_relatorio['contas']) == 0:
        print(f"Nenhuma conta encontrada para o mes de {mes_texto}")
        return

    total = dados_relatorio['valor_total_credito'] - dados_relatorio['valor_total_debito']
    dados_relatorio.update({
        "valor_total": "R$ {:.2f}".format(total),
        "valor_total_credito": "R$ {:.2f}".format(dados_relatorio['valor_total_credito']),
        "valor_total_debito": "R$ {:.2f}".format(dados_relatorio['valor_total_debito']),
    })

     
    nome_arquivo_criado = criar_relatorio_pdf.executar(
        dados=dados_relatorio, 
        nome_arquivo=f"relatorio_de_{mes_texto}"
    )

    if len(nome_arquivo_criado) > 0:
        print(f"O arquivo {nome_arquivo_criado} foi gerado com sucesso")
        return
    print("Não foi possível gerar o arquivo")

