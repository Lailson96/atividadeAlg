""" Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular
seu rendimento, ela deverá fornecer o valor constante da aplicação mensal, a
taxa e o número de meses. Sabendo-se que a fórmula usada para este cálculo é:
fl+ 􀀀' 1
valor acumulado = P * ' . - 􀀀i = taxa
P = aplicação mensal
n= número de meses
prog 1ea52
real va, i, p;
int n;
imprima "\ndigite o valor da aplicacao:
leia p;
imprima "\ndigite a taxa( O - 1):
leia i;
imprima "\ndigite o numero de meses: H;
leia n;
va <_p*(((1+ i )** n)-1) / i;
imprima "\nO valor acumulado: ", va;
imprima "\n";
fimprog """

p = float(input('\nDigite o valor da aplicação: '))
i = float(input('\nDigite a taxa ( 0 - 1): '))
n = int(input('\nDigite o número de meses: '))
va = float(p * (((1 + i) ** n) -1) / i)
print(f'\nO valor acumulado: {va:.2f}')
print('\n')