""" Criar um algoritmo que leia o numerador e o denominador de uma fração e trans -
formá-lo em um número decimal.
prog 1ea42
int num, denom;
imprima "\ndigite numerador:
leia num;
imprima "\ndigite denominador:
leia denom;
imprima "\ndecimal: ", num / denom;
imprima "\n";
fimprog """

num = int (input('\nDigite um numerador: '))
denom = int (input('\nDigite denominador: '))

print(f'\nDecimal: {num / denom}')
print('\n')