# FUP para ler dois números. Se os números forem iguais imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário,
#  imprimir o de maior valor.

print("Exercicio 5")
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um segundo numero: "))
if num1 == num2:
    print(f"Numeros iguais")
else:

    if num1 > num2:
        print (f"{num1}")
    else:
         print (f"{num2}")
