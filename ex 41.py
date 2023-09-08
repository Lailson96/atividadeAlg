""" Entrar com quatro números e imprimir a média ponderada, sabendo-se que os
pesos são respectivamente: 1, 2, 3 e 4.'''
prog leal4
real a, b, c,d, mp;
imprima "\nentre com 1 numero:
leia a;
imprima \nentre com 2 numero:
leia b;
imprima "\nentre com 3 numero:
leia c;
imprima "\nentre com 4 numero:
leia d;
mp <- (a*1 + b*2 + c*3 + d*4)/10 ;
imprima "\nmedia ponderada: ", mp;
imprima "\n";  """

numa= int (input('\nentre com um numero:'))
numb= int (input('\nentre com 2 numero:'))
numc= int (input('\nentre com 3 numero:'))
numd= int (input('\nentre com 4 numero:'))

print(f'\nNumeros: {numa,numb,numc, numd}')

mp=((numa*1+numb*2+numc*3+numd*4)/10)

print(f"\nmedia ponderada: {mp}")