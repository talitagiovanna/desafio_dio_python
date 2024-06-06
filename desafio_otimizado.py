# Menu de opções
def menu_opcoes():
    menu = """
    ==================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==================
    => """
    return input(menu).lower()

# Métodos para realizar as operações bancárias

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================== EXTRATO ==================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================================")

#Função main para inicializar o programa
def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu_opcoes()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Saindo... Obrigado por usar nosso sistema!")
            break
        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
