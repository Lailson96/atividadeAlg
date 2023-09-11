""" Criar um algoritmo que receba um número real, calcular e imprimir:
m a parte inteira do número
m a parte fracionária do número
m o número arredondado
prog lea46
real num, numfrac;
int numi,numa;
imprima "\nentre com um numero com parte fracionaria:
leia num;
numi <- realint((num - 0.5));
numfrac <- num - numi;
numa <- realint(num + 0.00001);
imprima ' 1 \nparte inteira: ",numi;
imprima "\nparte fracionaria: ",formatar((numfrac + 0.00001) ,3);
imprima "\nnumero arredondado: ", numa;
imprima "\n;
fi mprog """

num = float (input('\nEntre com um número com parte fracionária: '))
numi = float (int(num - 0.5))
numfrac = num - numi
numa = float(int(num + 0.00001))

print(f'\nParte inteira: {numi}')
print(f'\nParte fracionária: {(numfrac + 0.00001):.3f}')
print(f'\nParte arredondado: {numa}')

print('\n')