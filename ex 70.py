""" Todo restaurante embora por lei não possa obrigar o cliente a pagar, cobra 10%
para o garçom. Fazer um algoritmo que leia o valor gasto com despesas realizadas
em um restaurante e imprima o valor total com a gorjeta.
prog lea43
real cres, cgorj;
imprima "\nEntre com o valor da conta:
leia cres;
cgorj <- cres *11;
imprima "\nO valor da conta com a gorjeta sera: II, formatar(cgorj,2);
imprima "\n";
fi mprog """

cres = float(input('\nEntre com o valor da conta: '))
cgorj = cres * 1.1
print(f'\nO valor da conta com a gorjeta será: {cgorj:.2f}')
print('\n')