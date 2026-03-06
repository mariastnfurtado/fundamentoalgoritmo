while 1:
    n = int(input("Digite um número entre 0 e 10:"))
    if n >= 0 and n <= 10:
        print("Número aceito")
        break
    else:
        print("Informe um valor válido")