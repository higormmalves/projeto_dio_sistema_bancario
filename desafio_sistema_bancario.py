import datetime

menu = """
=======================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=======================
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
total_saques = 0

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
       
        if valor_deposito < 0:
            print("Valor inválido!")
        else:
            saldo += valor_deposito
            print("Depósito realizado com sucesso!")
            hora_atual = datetime.datetime.now()
            mensagem = f"Depósito realizado no valor de R${valor_deposito:.2f} em " + hora_atual.strftime("%d-%m-%y às %H:%M") + "."
            extrato.append(mensagem)
       
       
    elif opcao == "s":
        valor_saque = float(input("Digite o valor a ser sacado: "))
       
        if valor_saque < 0:
            print("Valor inválido!")
            
        elif valor_saque > saldo:
            print("Saldo insuficiente, não foi possível realizar o saque!")
            hora_atual = datetime.datetime.now()
            mensagem = f"Tentativa inválidade de saque por falta de saldo em " + hora_atual.strftime("%d-%m-%y às %H:%M") + "."
            extrato.append(mensagem)
            
        else:
            if total_saques < 3:
                saldo -= valor_saque
                print("Saque realizado com sucesso!")
                total_saques += 1
                hora_atual = datetime.datetime.now()
                mensagem = f"Saque realizado no valor de R${valor_saque:.2f} em " + hora_atual.strftime("%d-%m-%y às %H:%M") + "."
                extrato.append(mensagem)
            else:
                print("Não foi possível realizar o saque pois você já atingiu seu limite diário!")

    elif opcao == "e":
        if len(extrato) == 0:
            print("\nNão foram realizadas movimentações.")
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print()
            for ext in extrato:
                print(ext)
            print(f"\nSaldo atual: R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        