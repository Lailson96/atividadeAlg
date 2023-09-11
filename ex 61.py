""" Entrar com a razão de uma PG e o valor do 1 2 termo. Calcular e imprimir o 5 termo
da série.
prog lea34
int quinto, razao, termo;
imprima "\nEntre com o lo termo:
leia termo;
imprima "\nEntre com a razao:
leia razao;
quinto <- termo' * razao A4;
imprima "\nO 5o termo desta P.G. e: , quinto;
imprima "\n";
fi mprog """

termo = int(input('\nEntrar com 1° termo: '))
razao = int(input('\nEntrar com a razao: '))
quinto = termo * razao ^4

print(f'\nO 5º termo desa P.G é: {quinto}')
print('\n')