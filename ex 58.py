""" real xnuml, xnuni2, xnum3, x;
imprima "\nEntrar com 1 valor:
leia xnuml;
imprima "\nEntrar com 2 valor:
leia xnum2,
imprima "\nEntrar com 3 valor: hI
leia xnum3;
x <- xnuml + xnum2 / (xnum3 + xnuml) + 2 *(xnuml - xnum2) + log(64 )/
log(2 ),
imprima 11 \nX = 􀀀x,
imprima " \n 11 , """

import math as m

xnum1 = float(input('\nEntrar com 1° valor: '))
xnum2 = float(input('\nEntrar com 2° valor: '))
xnum3 = float(input('\nEntrar com 3° valor: '))
x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 * (xnum1 - xnum2) + m.log(64.) / m.log(2.)

print(f'\nX: {x:.2f}')
print('\n')