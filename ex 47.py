""" Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo:
123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser
impresso.
prog lea2O
int num, c, d, u, numl;
imprima "\nentre com um número de 3 dígitos:
leia num;
c <- num div 100;
d <- num % 100 div 10;
u <- num %10;
numl <- u*100 + d*10 + c;
imprima "\nnúmero: ", num;
imprima "\ninvertido: ", numl;
imprima "\n"; """

import math as m

num = int(input('\nEntre com um número de 3 dígitos: '))

c = num // 100
d = num % 100 // 10
u = num % 10

num1 = u*100 + d*10 + c

print(f'\nNumero: {num} ')
print(f'\nInvertido: {int(num1)} ')
print('\n')