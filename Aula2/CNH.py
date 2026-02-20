anoatual = int(input("Qual é o ano atual?"))
nascimento = int(input("Qual é o seu ano de nascimento?"))
idade = anoatual - nascimento
if idade>=18:
    print("Você pode tirar a CNH")
if idade<18:
    print("Você ainda não pode tirar a CNH")