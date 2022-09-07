#FUP para ler dois valores numéricos e apresentar a diferença do maior pelo menor. #
print("Exercicio 3")
num1 = float(input("Digite um primeiro numero: "))
num2 = float(input("Digite um  segundo numero: "))
dif = num1 - num2
dif2 = num2 - num1
if num1 > num2:
    print(f"A diferenca entre os numeros sao de: {dif}")
else:
    print(f"A diferenca entre os numeros sao de: {dif2}")
