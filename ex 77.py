""" Ler dois números reais e imprimir o quadrado da diferença do primeiro valor pelo
segundo e a diferença dos quadrados.
prog lea5O
real a, b, d, q;
imprima °\ndigite 1 numero: fl;
leia a;
imprima "\ndigite 2 numero:
leia b;
d <- (a - b)**2 ;
q <_a**2 - b**2 ;
imprima "\no quadrado da diferenca =",d , "\ndiferenca dos quadrados 􀀀q;
imprima "\n";
fi mprog """

a = float(input('\nDigite um número: '))
b = float(input('\nDigite outro número: '))
d = (a - b) ** 2
q = a**2 - b**2

print(f'\nO quadrado da diferenca {d} \nDiferenca dos quadrados: {q}')
print('\n')