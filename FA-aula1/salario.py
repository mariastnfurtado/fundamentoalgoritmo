ganhahora = float(input("Quanto ganha por hora?"))
horatrabalhada = float(input("Quantas horas trabalhadas?"))
salariobruto = ganhahora*horatrabalhada
ir = salariobruto*0.11
inss= salariobruto*0.08
sindicato= salariobruto*0.05
salarioliquido = salariobruto - (ir+inss+sindicato)
print("O salário bruto é", salariobruto)
print("O imposto de renda é", ir)
print("O INSS é", inss)
print("O sindicato é", sindicato)
print("O salário líquido é", salarioliquido)