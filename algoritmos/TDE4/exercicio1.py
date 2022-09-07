#Dados dois números A e B, some 100 ao maior número e imprima#
print("Exercicio 1")
A=float(input('Digite um numero: '))
B=float(input("Digite um segundo numero: "))

if A>B:
    soma=A+100
else:
    soma=B+100

print(f' Adicionando-se 100 ao maior numero é igual= {soma}')   
