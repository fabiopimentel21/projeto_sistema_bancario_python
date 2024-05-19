menu = """



[d] Depositar

[s] Sacar

[e] Extrato

[nc] Novo conta

[lc] Listar Contas

[nu] Novo Usuário

[q] Sair


=> """


saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUE = 3


while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Qual é o valor que você desejar depositar "))

        if valor > 0:

            saldo += valor

            extrato += f"Depósito: R${valor: .2f}\n"

        else:

            print("Operação falhou tente outro valor ")

    elif opcao == "s":

        valor = float(input("Informe o valor do saque"))

        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saques = numero_saques >= LIMITE_SAQUE

        if exedeu_saldo:

            print("Você não tem saldo suficiente.")

        elif exedeu_limite:

            print("Você não tem limite suficiente.")

        elif exedeu_saques:

            print("Número de tenativas de saques exedido.")

        elif valor > 0:

            saldo -= valor

            extrato += f"Saque: R$ {valor: .2f}\n"

            numero_saques += 1

        else:

            print("Valor invalido")

    elif opcao == "e":

        print("\n#################EXTRATO###################")

        print("Não foram realizados movimentos." if not extrato else extrato)

        print(f"\nsaldo: R$ {saldo:.2f}")

        print("#############################################")

    elif opcao == "q":

        break

    else:

        print("operação inavalida, por favor selecione a opçãp desejada.")

import textwrap


def menu():
    menu = """\n
    =========MENU===========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNovo Usuário
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n===Depósito realizado com sucesso!===")
    else:
        print("\n@@@ operação falhou! o valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite
    exedeu_saques = numero_saques > limite_saques

    if exedeu_saldo:
        print("\n@@@ operação falhou! Você não tem saldo suficiente. @@@")

    elif exedeu_limite:
        print("@@@ operação falhou! exedeu o limite . @@@")

    elif exedeu_saques:
        print("\n@@@ operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n #### Saque Realizado com Sucesso! ###")

    else:
        print("\n @@@ operação falhou! o valor informado e inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n################ EXTRATO ############")
    print("Não foram realizadas movimentações. " if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo: .2f}")
    print("###################################")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, cep, bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})
    print("##### Usuário Criado com sucesso! ###")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Conta criada com Sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontardo, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agênacia:\t{conta['agencia']}
            C\C:\t\t{conta['numemro_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
          valor = float(input("informe o valor do depósito: "))
  
          saldo, extrato = depositar(saldo, valor, extrato)
  
        elif opcao == "s":
          valor = float(input("informe o valor do saque: "))

          saldo, extrato = sacar(
              saldo=saldo,
              valor=valor,
              extrato=extrato,
              limite=limite,
              numero_saques=numero_saques,
              LIMITE_SAQUE=LIMITE_SAQUE,
          )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break


    



