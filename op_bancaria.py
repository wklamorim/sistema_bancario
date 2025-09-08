# Criar um sistema bancário com as operações:sacar, depositar e visualizar extrato.
saldo = 0.0
depositos = []  # Lista para armazenar depósitos
saques = []  # Lista para armazenar saques
extratos = []  # Lista para armazenar extratos
LIMITE_SAQUES = 500.0  # Constante para o limite de saque
LIMITE_SAQUES_DIARIOS = 3  # Contsante para o limite de saques diários
numero_saques = 0


def depositar(valor):
    global saldo
    if valor > 0:  # Verifica se o valor é positivo
        saldo += valor  # Atualiza o saldo (variavel global)
        depositos.append(valor)  # Adiciona o valor à lista de depósitos
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido. Tente novamente.")


def sacar(valor):
    global saldo, numero_saques
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite diário de saques atingido.")
        return
    if valor > LIMITE_SAQUES:
        print(f"Valor de saque excede o limite de R$ {LIMITE_SAQUES:.2f}.")
        return
    if valor > saldo:
        print("Saldo insuficiente para saque.")
        return
    if valor > 0:  # Verifica se o valor é positivo
        saldo -= valor
        saques.append(valor)
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de saque inválido. Tente novamente.")


def exibir_extrato():
    print("\n=== Extrato ===")
    if not depositos and not saques:
        print("Não foram realizadas movimentações!")
    else:
        for valor in depositos:
            print(f"Depósito: R$ {valor:.2f}")
        for valor in saques:
            print(f"Saque: R$ {valor:.2f}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("========================\n")


def menu():
    while True:
        print("Menu".center(12, " "))
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(valor)
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            print("""Saindo do sistema.\nObrigado por usar nosso banco!""")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
