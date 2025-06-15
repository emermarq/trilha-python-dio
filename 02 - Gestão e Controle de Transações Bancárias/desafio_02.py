''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    for transacao in transacoes:
        if abs(transacao) > limite :
            transacoes_filtradas.append(transacao)
            
    return transacoes_filtradas 


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float

transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")