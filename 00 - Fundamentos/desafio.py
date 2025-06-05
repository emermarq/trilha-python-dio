from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def print_color(texto, color=Color.RED):
    if color == Color.RED :
        print(f"\033[31m{texto}\033[0m")
    elif color == Color.BLUE :
        print(f"\033[34m{texto}\033[0m")
    else:
        print(texto)

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print_color("Operação Realizada com sucesso !.", Color.BLUE)
        else:
            print_color("Operação falhou! O valor informado é inválido.", Color.RED)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print_color("Operação falhou! Você não tem saldo suficiente.", Color.RED)

        elif excedeu_limite:
            print_color("Operação falhou! O valor do saque excede o limite.", Color.RED)

        elif excedeu_saques:
            print_color("Operação falhou! Número máximo de saques excedido.", Color.RED)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print_color("Operação Realizada com sucesso !.", Color.BLUE)
        else:
            print_color("Operação falhou! O valor informado é inválido.", Color.RED)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print_color("Saída solicitada. Até a próxima ;-)", Color.BLUE)
        break

    else:
        print_color("Operação inválida, por favor selecione novamente a operação desejada.", Color.RED)