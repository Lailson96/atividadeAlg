""" er dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a
variávelA passe a ter o valor da variável B e que a variável B passe a ter o valor da variável
A. Apresentar os valores trocados.
prog lea4l
real a, b, aux;
imprima "\ndigite 1 numero com ponto: U;
leia a;
imprima "\ndigite 2 numero com ponto:
leia b;
aux <- a;
a 􀀀<-b;
b 􀀀<-aux;
521 imprima "\na = , a, "\nb = ", b;
imprima "\n";
fimprog """

a = float(input('\nDigite um número com ponto: '))
b = float(input('\nDigite outro número com ponto: '))
aux = a
a = b
b = aux
print(f'\nA: {a} \nB: {b} \nAux:{aux}')
print('\n')