import math

while True:
    print("=== MENU ===")
    print("1-soma")
    print("2-subtração")
    print("3-multiplicação")
    print("4-divisão")
    print("5-média")
    print("6-equação de segundo grau")
    print("7-fatorial")
    print("8-tabuada")
    print("9-fibonacci")
    print("10-sair")
    opcao = int(input("escolha uma opcao de 1 a 10 "))

    if opcao == 10:
        print("saindo...")
        break
    elif opcao == 1:
        num1 = float(input("digite o primeiro numero "))
        num2 = float(input("digite o segundo numero "))
        resultado = num1 + num2
        print(f"o resultado da soma e {resultado}")
    elif opcao == 2:
        num1 = float(input("digite o primeiro numero "))
        num2 = float(input("digite o segundo numero "))
        resultado = num1 - num2
        print(f"o resultado da subtração e {resultado}")
    elif opcao == 3:
        num1 = float(input("digite um numero "))
        num2 = float(input("digite o segundo numero "))
        resultado = num1 * num2
        print(f"o resultado da multiplicação e {resultado}")
    elif opcao == 4:
        num1 = float(input("digite o primeiro numero "))
        num2 = float(input("digite o segundo numero "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"o resultado da divisão e {resultado}")
        else:
            print("erro: divisão por zero")
    elif opcao == 5:
        num1 = float(input("digite um numero "))
        num2 = float(input("digite o segundo numero "))
        resultado = (num1 + num2) / 2
        print(f"o resultado da media e {resultado}")

    elif opcao == 6:
        a = int(input("digite o valor de a: "))
        b = int(input("digite o valor de b: "))
        c = int(input("digite o valor de c: "))
        
        delta = b**2 - (4 * a * c)
        print(f"o valor de delta é {delta}")
        if delta < 0:
            print("a equação não possui raízes reais (delta negativo)")
        elif a == 0:
            print("o valor de 'a' não pode ser zero em uma equação de segundo grau")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"o valor de x1 é: {x1:.2f}")
            print(f"o valor de x2 é: {x2:.2f}")
            
            
            
    elif opcao == 7:
            num = int(input("digite um número inteiro positivo: "))
            if num < 0:
                    print("o fatorial não está definido para números negativos. ")
            else:
                resultado = math.factorial(num)
                print(f"o fatorial de {num} é {resultado}")
        
    elif opcao == 8:
        num = int(input("digite um número para ver a tabuada: "))
        print(f"tabuada do {num}")
        
        for i in range(1, 11):
            resultado = num * i 
            print(f"{num} x {i} = {resultado}")
    
    elif opcao == 9:
        n = int(input("quantos termos da sequência de Fibonacci você quer ver?"))
        t1 = 0
        t2 = 1
        print(f"{t1} -> {t2}" , end="")
        
        cont = 3
        while cont <= n:
            t3 = t1 + t2
            print(f" -> {t3}", end="")
            
            t1 = t2
            t2 = t3
            cont += 1
        print("-> FIM")