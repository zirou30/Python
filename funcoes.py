#Recebe os Valores
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

'''Utilizando, o elif serve para retirar um if else'''
if n1 > n2:
    print("O primeiro número e maior.")
elif n2 > n1:
    print("O segundo número e maior.")

#Agora utilizando if e else

if n1 > n2:
    print("O primeiro número é maior.")
else:
    print("O segundo número e maior.")

'''Agora utilizando um while, foi necessário utilizar o break.
Pois se o valor de n1 fosse maior que n2, o mesmo entraria em loop
e ficaria printando o a primeira string inifinitamente.'''

while n1 > n2:
    print("O primeiro número é maior.")
    if n1 == n1:
        break
if n2 > n1:
    print("O segundo número é maior.")
else:
    print("Ambos os números são iguais.")
