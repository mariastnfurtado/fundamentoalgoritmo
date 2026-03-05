codigoalimento = int(input("Digite o código do alimento"))

if codigoalimento==1:
    print("Alimento não perecível")
if codigoalimento==2 or codigoalimento==3 or codigoalimento==4:
    print("Alimento perecível")
if codigoalimento==5 or codigoalimento==6:
    print("Vestuário")
if codigoalimento==7:
    print("Higiene pessoal")
if codigoalimento>=8 and codigoalimento<=15:
    print("Limpeza e utensílios domésticos")
if codigoalimento>15:
    print("Inválido")