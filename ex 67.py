""" Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
prestação = valor + (valor*(taxa/100)*tempo).
prog lea4O
real prest, valor, taxa;
int tempo;
imprima "\ndigite o valor da prestação:
leia valor;
imprima "\ndigite a taxa:
leia taxa;
imprima "\ndigite o tempo(numero de meses):
leia tempo;
prest <- valor+(valor*(taxa/100)*tempo);
imprima "\no valor da prestacao em atraso e =", prest;
imprima "\n";
fi mprog """

valor = float (input('\nDigite o valor da prestação: '))
taxa = float (input('\nDigite a taxa: '))
tempo = int(input('\nDigite o tempo (Número de meses: '))
prest = valor + (valor * (taxa / 100) * tempo)

print(f'\nO valor da prestacao em atraso é {prest}')

print('\n')