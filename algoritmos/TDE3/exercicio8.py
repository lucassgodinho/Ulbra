print("exercicio 8")
raio=float(input("Digite o raio do tanque: "))
altura=float(input("Digite a altura do tanque: "))
arealateral=  2 * 3.14 * raio * altura
base= 3.14 * (raio * raio)
areatotalcil= base + arealateral
print(f"Area total: {areatotalcil}, area lateral: {arealateral} e a base: {base} ")
gasto_total=((areatotalcil/ 3)/5) * 150
latas= gasto_total / 150
print(f"Total de gastos com a tinta: {gasto_total} reais. Sendo necessarias {latas} latas de tintas. ")