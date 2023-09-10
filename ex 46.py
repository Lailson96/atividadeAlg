""" Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o
novo saldo, considerando o reajuste de 1%.
prog leal9
real saldo, nsaldo;
imprima "\ndigite saldo: "; 􀀀 43
leia saldo;
nsaldo <-saldo * 1.01;
imprima " \nnovo saldo: ",nsaldo;
imprima \n";
 """

saldo = float(input('\nDigite o seu saldo: '))

nsaldo = saldo * 1.01

print(f'\nNovo salvo: {nsaldo}')
print('\n')
