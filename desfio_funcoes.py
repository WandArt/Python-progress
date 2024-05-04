import textwrap  # Importando textwrap para formatação de texto

def menu():
    menu_text = """
    ######### MENU #########
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"===\nDepósito de R$ {valor:.2f} realizado com sucesso!\n===")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato
    

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("### Saque realizado! ###")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("CPF informado já cadastrado!")
        return
    nome = input("Informe seu nome completo: ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"nome": nome, "endereco": endereco, "cpf": cpf})
    print("Usuário criado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado!")


def main():
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()  # Corrigido: chamada correta da função menu()
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas)
            conta = criar_conta("0001", numero_conta, usuarios)  # Corrigido: agência fixa
            if conta:
                contas.append(conta)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
