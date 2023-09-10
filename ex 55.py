""" Criar um algoritmo que calcule e imprima a área de um losango.
prog 1ea28
real diagmaior, diagmenor, area;
imprima "\nmedida da diagonal maior:
leia diagmaior;
imprima "\nmedida da diagonal menor:
leia diagmenor;
area <- (diagmaior * diagmenor)/2;
imprima "\narea =", area;
imprima "\n"; """

diagmaior=float(input('\nMedida da diagonal maior: '))
diagmenor=float(input('\zMedida da diagonal menor '))
area = (diagmaior * diagmenor) / 2

print(f'\nÁrea: {area:.2f} ')
print('\n')