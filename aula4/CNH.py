anonascimento = int(input("Em que ano você nasceu?"))
idade = 2026 - anonascimento

if idade >=16 and idade>=18:
    print(idade)
    print("Você está já pode votar e ter sua carteira de habilitação")
else:
    print(idade)