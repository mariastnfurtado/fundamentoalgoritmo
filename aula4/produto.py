preco = float(input("Qual é o preço?"))
cod = int(input("Qual é o código?"))

if cod == 1:
    print("Sul %.2f" % preco)
else:
    if cod == 2:
        print("Norte %.2f" % preco)
    else:
        if cod == 3:
            print("Leste %.2f" % preco)
        else:
            if cod ==4:
                print("Oeste %.2f" % preco)
            else:
                if cod == 5 or cod == 6:
                    print("Nordeste %.2f" % preco)
                else:
                    if cod == 7 or cod == 8 or cod == 9:
                        print("Sudeste %.2f" % preco)
                    else:
                        if cod >= 10 and cod <= 20:
                            print("Centro-Oeste %.2f" % preco)
                        else:
                            if cod>= 25 and cod <= 30:
                                print("Nordeste %.2f" % preco)
                            else:
                                print("Importado %.2f" % preco)