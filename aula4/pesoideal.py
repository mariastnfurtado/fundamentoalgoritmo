altura = float(input("Qual é a sua altura?"))
sexo = input("Qual é o seu sexo?")

if sexo == "homem":
    pesoideal = (72.7 * altura) - 58
else:
    pesoideal = (62.1 * altura) - 44.7
print("O seu peso ideal é %.2f" % pesoideal)