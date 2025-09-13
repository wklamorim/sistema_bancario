from datetime import datetime

data = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M")


def menu():
    while True:
        print("Menu".center(12, " "))
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Cadastrar cliente")
        print("5. Cadastrar conta")
        print("6. Listar contas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        return opcao


def depositar(saldo, valor, movimentacao, /):
    op = 'Depósito'
    aux = 30 - (len(f'{op} ') + len(' R$ ') + len(str(valor)) + 3)
    if valor > 0:  # Verifica se o valor é positivo
        saldo += valor
        movimentacao.append(f'{op} {"." * aux} R$ {valor:.2f}')
        print('Depósito realizado com sucesso!')
    else:
        print("Valor de depósito inválido. Tente novamente.")

    return saldo, movimentacao


def sacar(*, saldo, valor, movimentacao, numero_saques, limite_saques, limites_saques_diario):
    op = 'Saque'
    aux = 30 - (len(f'{op} ') + len(' R$ ') + len(str(valor)) + 3)
    if numero_saques >= limites_saques_diario:
        print("Limite diário de saques atingido.")
    if valor > limite_saques:
        print(f"Valor de saque excede o limite.")
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    if valor > 0:  # Verifica se o valor é positivo
        saldo -= valor
        numero_saques += 1
        movimentacao.append(f'{op} {"." * aux} R$ {valor:.2f}')
        print(f"Saque realizado com sucesso.")
    else:
        print("Valor de saque inválido. Tente novamente.")

    return saldo, movimentacao, numero_saques


def exibir_extrato(saldo, /, *, movimentacao):
    aux = 30 - (len(f'Saldo atual: R$ ') + len(str(saldo)) + 4)
    print(" Extrato ".center(28, "="))
    print(f'Data: {data} hora: {hora}')
    print(f"{"=" * 28}")
    if not movimentacao:
        print("Não foram realizadas movimentações!")
    else:
        for row in movimentacao:
            print(row)
    print(f"\n{"=" * 28}")
    print(f"Saldo atual: R$ {"." * aux} {saldo:.2f}")
    print(f"{"=" * 28}\n")


def verificar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf in usuario.values():
            return usuario
        else:
            return None
    return None


def cadastrar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    cadastrado = verificar_usuario(cpf, usuarios)
    if cadastrado:
        print('Usuário já cadastrado!')
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    return usuarios


def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    cadastrado = verificar_usuario(cpf, usuarios)
    if cadastrado:
        print('Conta cadastrada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cadastrado['nome']}
    return None


def listar_contas(contas):
    if len(contas) == 0:
        print('Não há contas cadastradas!')
    else:
        for conta in contas:
            print(f"""Agência: {conta['agencia']}\nConta: {conta["numero_conta"]}\nCliente: {conta["usuario"]}""")


def main():
    # constantes
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_DIARIO_OPERACOES = 10
    AGENCIA = '0001'

    # Variáveis
    saldo = 0.0
    numero_saques = 0
    limite_saques = 500.0

    # listas
    movimentacao = []  # Lista para armazenar movimentacao
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            saldo, movimentacao = depositar(saldo, valor, movimentacao)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            saldo, movimentacao, numero_saques = sacar(saldo=saldo, valor=valor, movimentacao=movimentacao,
                                                       numero_saques=numero_saques,
                                                       limite_saques=limite_saques,
                                                       limites_saques_diario=LIMITE_SAQUES_DIARIOS)
        elif opcao == "3":
            exibir_extrato(saldo, movimentacao=movimentacao)

        elif opcao == "4":
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            else:
                print('Usuário não encontrado!\nConta não cadastrada!')
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            print("""Saindo do sistema.\nObrigado por usar nosso banco!""")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
