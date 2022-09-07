#FUP que leia o número da conta bancária e o saldo de um cliente. Caso a conta tenha saldo negativo,
#  o programa deve enviar a seguinte mensagem: CONTA ESTOURADA, caso contrário CONTA NORMAL.
print("Exercicio 10")
numconta=float(input("Digite o numero da sua conta: "))
saldo=float(input("Digite corretamento o seu saldo: "))
if saldo >=0:
    print("CONTA NORMAL")
else: 
    print("CONTA ESTOURADA")