""" juros.
Calcular e imprimir o valor do rendimento e o valor total depois do rendimento.
prog 1ea45
real deposito, taxa, valor, total;
imprima "\nentre com depósito: ;
leia deposito;
imprima "\nentre coma taxa de juros: ";
leia taxa;
valor <- deposito*taxa/100 ;
total <- deposito + valor;
imprima "\nRendimentos: II valor, "\nTotal: ", total;
imprima "\n";
fi mprog """


deposito = float(input('\nEntre com deposito: '))
taxa = float(input('\nEntre com a taxa de juros: '))
valor = deposito * taxa / 100
total = deposito + valor
print(f'\nRendimento: {valor} \nTotal: {total}')
print('\n')