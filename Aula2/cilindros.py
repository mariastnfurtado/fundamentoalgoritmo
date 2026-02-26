from math import ceil

altura = float(input("Qual é a altura do cilindro?"))
raio = float(input("Qual é o raio do cilindro?"))
areabase = (raio**2)*3.1415
perimetro = 2*3.1415*raio
arealateral = perimetro*altura
areatotal = areabase+arealateral

litronecessario = areatotal/3
latas = litronecessario/5
qtdelatas = ceil(latas)

print("Altura: %.2f" % altura)
print("Raio: %.2f" % raio)
print("Área a ser pintada: %.2f" % areatotal)
print("Quantidade de litros necessários: %.2f" % litronecessario)
print("Quantidade de latas: %d" % qtdelatas)
if qtdelatas == 1:
    print("Preço unitário da lata: R$50,00")
    custototal = qtdelatas*50
if qtdelatas == 2:
    print("Preço unitário da lata: R$48,00")
    custototal = qtdelatas*48
if qtdelatas == 3:
    print("Preço unitário da lata: R$46,00")
    custototal = qtdelatas*46
if qtdelatas>3:
    print("Preço unitário da lata: R$45,00")
    custototal = qtdelatas*45
print("Custo total: R$%.2f" % custototal)