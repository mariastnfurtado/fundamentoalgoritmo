km = float(input("Quantos km você quer percorrer?"))
if km<=200:
    preco=km*0.50
else:
    preco=km*0.45
print("O preço da sua passagem é de: $", preco)