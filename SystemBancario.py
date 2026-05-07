saldo = 0
extrato = ""

taxa_mensal = 0.05 
meses_para_mostrar = 5
anos_para_mostrar = 1

while True:
    print ("=== SISTEMA BANCÁRIO ===")
    
    print ("")
    print ("1 - Ver saldo ")
    print ("2 - Depositar ")
    print ("3 - Sacar ")
    print ("4 - Ver extrato ")
    print ("5 - Investimentos")
    print ("6 - Meu porquinho")
    print ("7 - Sacar valor do porquinho")
    print ("8 - Sair")
    print ("========================") 

    Opcao = input("Digite seu interesse:  ")

    if Opcao == "1":
        print ("Seu saldo atual é = ", saldo)

    elif Opcao == "2":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo = saldo + valor
            print ("Deposito Realizado! ")
            extrato = extrato + f"Depósito de R$ {valor}\n"

        else:
            print ("Valor Inválido! ")    
    
    elif Opcao == "3":
        valor = float(input("Digite a quantia que deja sacar R$: "))
        if valor > 0:
            if valor >= valor:
                saldo = saldo - valor
                print ("Saque realizado !")
                extrato = extrato + f"Saque de R$ {valor}\n"
            else:
                print ("Saldo Insuficiente! ")
        else:
            print ("Valor Inválido! ")                     
    
    elif Opcao == "4":
       if extrato == "":
            print ("Nenhuma movimentação")
       else:
            print (extrato)

    elif Opcao == "5":
        print ("Digite o quanto você deseja investir: ")
        valor = float(input("Valor do investimento R$: "))
        if valor > 0:
            saldo = saldo - valor #o valor do investimento é retirado do saldo para ser investido
            print ("Investimento realizado! ")
            extrato = extrato + f"Investimento de R$ {valor}\n" #o f antes da string permite a inserção de variáveis dentro da string usando chaves {}

            meses = meses_para_mostrar
            anos = anos_para_mostrar   
            meses_em_anos = anos * 12  #conversão de anos para meses ja que a taxa é mensal

            montante_meses = valor * (1 + taxa_mensal) ** meses #o 1 representa o 100% do valor inicial
            montante_anos = valor * (1 + taxa_mensal) ** meses_em_anos #os dois ** significam "elevado a"

            print (f"Em {meses} meses, seu dinheiro vira: R$ {montante_meses:.2f}")
            print (f"Em {anos} anos, seu dinheiro vira: R$ {montante_anos:.2f}")
        else:
            print ("Valor Inválido! ")

    elif Opcao == "6":
        print ("Digite o quanto você deseja depositar no porquinho: ")
        valor = float(input("Valor do depósito R$: "))
        if valor > 0:
            saldo = saldo + valor
            print ("Depósito realizado! ")
            extrato = extrato + f"Depósito de R$ {valor}\n"

    elif Opcao == "7":
        valor = float(input("Digite a quantia que deja sacar do seu porquinho R$: "))
        if valor > 0:
            if valor <= saldo:  #mostra que o valor a ser sacado é menor ou igual ao saldo do porquinho
                saldo = saldo - valor
                print ("Saque realizado !")
                extrato = extrato + f"Saque de R$ {valor}\n"
            else:
                print ("Saldo Insuficiente! ")

    elif Opcao == "8":
        print ("Saindo...")
        break   #o break é usado para sair do loop while quando o usuário escolhe a opção 8

    else:
        print ("Opção inválida! Por favor, escolha uma opção válida.") 