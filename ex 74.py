""" Para vários tributos, a base de cálculo é o salário mínimo. Fazer um algoritmo que
leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e impri -
mir quantos salários mínimos ela ganha.
prog 1ea47
real salmin, salpe, num;
imprima "\nentre com o salario minimo:
leia salmin;
imprima °\nentre com o salario da pessoa:
leia salpe;
num <- salpe / saimin;
imprima "\na pessoa ganha ", num, " salarios minimos";
imprima " \n " ;
fimprog """

salmin = float(input('\nEntre com o salário mínimo: '))
salpe = float(input('\nEntre com o salario da pessoa: '))
num = salpe / salmin
print(f'\nA pessoa ganha {num} salários mínimos')
print('\n')