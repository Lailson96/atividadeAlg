""" Entrar com a razão de uma PA e o valor do 1 2 termo. Calcular imprimiro 10 termo
da serie
prog 1ea33
int dec, razao, termo,
imprima "\nEntrar com o lo termo:
leia termo,
imprima "\nEntrar com a razao
leia razao,
dec <- termo + 9 razao,
imprima "\nO 10 termo desta P.A. e ", dec,
imprima "\n,
fi mprog """
import math as m

termo = float(input('\nEntrar com 1° termo: '))
razao = float(input('\nEntrar com a razao: '))
dec = termo + 9 * razao

print(f'\nO 10 termo desa P.A é: {dec:.2f}')
print('\n')