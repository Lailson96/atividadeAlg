""" Criar um algoritmo que calcule e imprima a área de um triângulo.
prog 1ea27
real 􀀀a, b;
imprima "\nEntre com a base:
leia a;
imprima "\nEntre a altura do um triângulo:
leia b;
imprima "\nArea = ", (a *
imprima "\n"; """

import math as m

a = float(input('\nEntre com a base: '))
b = float(input('\nEntre com a altura de um triângulo: '))

print(f'\nÁrea: {(a * b) / 2} ')
print('\n')