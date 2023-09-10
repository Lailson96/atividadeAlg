""" Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal.
prog 1ea26
real a, b, c, diagonal;
imprima "\nentre com a base: H;
leia a;
imprima "\nentre com a altura:
461 1eia b;
imprima "\nentre com a profundidade:
leia c;
diagonal <-raiz( a**2 + b**2 + c**2 );
imprima "\ndiagonal : ", diagonal;
imprima "\n"; """

import math as m

a = int(input('\nEntre com a base: '))
b = int(input('\nEntre com a altura: '))
c = int(input('\nEntre com a profundidade: '))

diagonal = m.sqrt(a**2 + b**2 + c**2)

print(f'\nDiagonal: {diagonal:.2f} ')
print('\n')