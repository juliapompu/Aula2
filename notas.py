nota1= input(print('Qual é a primeira noat?'))
nota2= input(print('Qual é a segunda nota?'))
nota3= input(print('Qual é a terceira nota?'))

N1= int(nota1)
N2= int(nota2)
N3= int(nota3)

media= N1 + N2 + N3 /3

if media > 6:
    print('Aprovada')
if media == 6:
    print('Recuperação')
else: 
    print('Reprovada')