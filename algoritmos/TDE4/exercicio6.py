# FUP para ler e escrever três números. Se o primeiro for positivo, imprimir sua raiz quadrada, caso contrário, imprimir o seu quadrado;
# se o segundo número for maior que 10 e menor que 100, imprimir a mensagem: "NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO";
# se o terceiro número for menor que o segundo, calcular e escrever a diferença entre eles, caso contrário,
# calcular e escrever a soma entre eles.
from math import sqrt
print("Exercicio 6")
num1 = float(input("Digite um primeiro numero: "))
num2 = float(input("Digite um segundo numero:  "))
num3 = float(input("Digite um terceiro numero: "))
dif = num2 - num3
raizq = sqrt(num1)
soma= num2+num3
quadrado = num1*num1
if num1 >= 0:
    print(f" Raiz quadrada do primeiro numero e de: {raizq}")
else:
    print(f"Seu quadrado e de {quadrado}")
if num2 >= 10 <= 100:
    print(f"NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO")
if num3 < num2:
    print(f"A diferenca e igual a : {dif}")
else:
    print (f"A soma e igual a: {soma}")
