print("exercicio 10")
idvendedor=float(input('Digite seu numero de identificacao: '))
salafixo= float(input('Digite seu salario fixo: '))
numcarros= float(input('Digite quantos carros voce vendeu: '))
comissao= float(input("Digite qual o valor que recebe por carro vendido: "))
salario_comi= salafixo + comissao * numcarros  
print(f"Funcionario do codigo: {idvendedor}, vendeu {numcarros}, recebendo {comissao} reias por carro vendido, sendo seu salario final de {salario_comi} reais.  ")


