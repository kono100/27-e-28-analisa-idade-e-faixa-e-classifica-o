
#27. A Organização Mundial de Saúde classifica as pessoas pela sua faixa etária, de acordo com
#a tabela a seguir:

#   FAIXA        IDADE       CLASSSIFICAÇÃO
#    A           0 A 12         CRIANÇA
#    B          13 A 18         ADOLESCENTE
#    C          19 A 59         ADULTO
#    D          60 E ACIMA      TERCERIRA IDADE

#28. Elabore um programa que leia a Idade do usuário e informe na tela a sua Faixa e a sua
#Classificação, segundo a tabela acima.

idade = int(input("Digite a sua Idade: "))

if idade <=12:  
        print (f"\nFaixa:A Idade:{idade}  Criança\n")
elif idade <=18:
    print (f"\nFaixa:B Idade:{idade}  Adolescente\n")
elif idade <=59:
    print (f"\nFaixa:C Idade:{idade}  Adulto\n")
elif idade <=200:
    print (f"\nFaixa:D Idade:{idade}  Terceira Idade\n")
elif idade <=10000:
    print (f"\né alienígena ?\n")
