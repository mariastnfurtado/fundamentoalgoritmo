salario = float(input("Qual é o seu salário?"))
if salario>1250:
    aumento = salario*0.10
    novosalario = salario + aumento
else:
    aumento = salario*0.15
    novosalario = salario + aumento
print("O novo salario é", novosalario)