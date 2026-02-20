dias = int(input("Qual é a quantidade de dias?"))
hora = int(input("Qual é a quantidade de horas?"))
minuto = int(input("Qual é a quantidade de minutos?"))
segundo = int(input("Qual é a quantidade de segundos?"))
ht = (minuto*60) + (dias*86400) + (hora*3600) + segundo
print("o total de segundos percorridos é", ht)