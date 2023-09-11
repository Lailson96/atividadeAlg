""" Dado um polígono convexo de n lados, podemos calcular o número de diagonais
diferentes (nd) desse polígono pela fórmula : nd = n (n —3)! 2. Fazer um algoritmo
que leia quantos lados tem o polígono, calcule e escreva o número de diagonais
diferentes (nd) do mesmo.
56
prog lea5l
real nd;
int n;
imprima "\ndigite o numero de lados do poligono II,
leia n,
nd<_n* (n-3) /2;
imprima "\nnumero de diagonais: ", nd;
imprima hI\H;
fi mprog """

n = int(input('\nDigite o numero de lados do poligono: '))
nd = float(n * ( n - 3) / 2)

print(f'\nNumero de diagonais: {nd}')
print('\n')