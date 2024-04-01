import datetime
import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

#FUNÇÃO DEPOSITAR
def depositar(valor_deposito, saldo, extrato, /):
    if valor_deposito < 0:
        print("Valor inválido!")
    else:
        saldo += valor_deposito
        print("Depósito realizado com sucesso!")
        hora_atual = datetime.datetime.now()
        mensagem = f"Depósito realizado no valor de R${valor_deposito:.2f} em " + hora_atual.strftime("%d-%m-%y às %H:%M") + "."
        extrato.append(mensagem)
        
    return saldo, extrato

##FUNÇÃO SACAR
def sacar(*, valor_saque, saldo, extrato, total_saques, LIMITE_VALOR, LIMITE_SAQUES):
    if valor_saque < 0:
            print("Valor inválido, a operação falhou!")
            
    elif valor_saque > saldo:
        print("Saldo insuficiente, não foi possível realizar o saque!")
        hora_atual = datetime.datetime.now()
        mensagem = f"Tentativa inválidade de saque por falta de saldo em " + hora_atual.strftime("%d-%m-%y às %H:%M") + "."
        extrato.append(mensagem)
                        
    elif valor_saque > LIMITE_VALOR:
        print("O valor do saque excede o limite!")
            
    else:
        if total_saques < LIMITE_SAQUES:
            saldo -= valor_saque
            print("Saque realizado com sucesso!")
            total_saques += 1
            hora_atual = datetime.datetime.now()
            mensagem = f"Saque realizado no valor de R${valor_saque:.2f} em " + hora_atual.strftime("%d-%m-%y às %H:%M") + "."
            extrato.append(mensagem)
                                
        else:
            print("Não foi possível realizar o saque pois você já atingiu seu limite diário!")
                
    return saldo, extrato, total_saques

##FUNÇÃO EXIBIR EXTRATO
def exibir_extrato(saldo, /, *, extrato):
    if len(extrato) == 0:
        print("\nNão foram realizadas movimentações.")
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print()
        for ext in extrato:
            print(ext)
        print(f"\nSaldo atual: R${saldo:.2f}")

##FUNÇÃO PARA VERIFICAR SE UM USUÁRIO JÁ EXISTE NO SISTEMA
def verificar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            return usuario
        else:
            return None

##FUNÇÃO CRIAR USUARIO
def criar_usuario(usuarios):
    print("Digite os dados no novo usuário:")
    cpf = input("Informe o CPF (somente número): ")
    
    if verificar_usuario(cpf, usuarios):
        print("O usuário já está cadastrado no sistema!")
        
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("Usuário criado com sucesso!")

##FUNÇÃO PARA CRIAR CONTA
def nova_conta(agencia, numero_conta, usuarios):
    print("Digite os dados no novo usuário:")
    cpf = input("Informe o CPF (somente número): ")
    usuario = verificar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Não foi possível criar a conta pois não exite nenhum usário com este CPF cadastrado no sistema!")

##FUNÇÃO PARA LISTAR AS CONTAS EXISTENTES
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():
    extrato = []
    saldo = 0
    
    total_saques = 0
    LIMITE_VALOR = 500
    LIMITE_SAQUES = 3
    
    usuarios = []
    
    AGENCIA = "0001"
    contas = []
    
    while True:
        
        opcao = menu()
        
        if opcao == "d":
            valor_deposito = float(input("Informe o valor do depósito: ")) 
            saldo, extrato = depositar(valor_deposito, saldo, extrato)
            
        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: ")) 
            saldo, extrato, total_saques = sacar(valor_saque=valor_saque, saldo=saldo, extrato=extrato, total_saques=total_saques, LIMITE_VALOR=LIMITE_VALOR, LIMITE_SAQUES=LIMITE_SAQUES)
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()


    
