menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[f] Finalizar

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

depositos = []
saques = []

executando = True

while executando:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor depositado precisa ser positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("❌ Operação falhou! O valor para saque precisa ser positivo.")

        elif valor > saldo:
            print("❌ Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("❌ Operação falhou! O valor do saque excede o limite de R$500,00.")

        elif numero_saques >= LIMITE_SAQUES:
            print("❌ Operação falhou! Você já realizou o número máximo de 3 saques.")

        else:
            saldo -= valor
            saques.append(valor)
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")

        if not depositos and not saques:
            print("Nenhuma movimentação realizada.")
        else:
            print("📥 Depósitos:")
            for dep in depositos:
                print(f"   + R$ {dep:.2f}")

            print("\n📤 Saques:")
            for saq in saques:
                print(f"   - R$ {saq:.2f}")

        print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "f":
        print("✅ Serviço finalizado. Obrigado por usar o sistema!")
        executando = False 

    else:
        print("❌ Opção inválida! Tente novamente por gentileza.")
