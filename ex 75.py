""" Criar um algoritmo que leia o peso de uma pessoa, só a parte inteira, calcular e
imprimir:
m o peso da pessoa em gramas
m novo peso em gramas se a pessoa engordar 12%
55
prog 1ea48
int peso, pesogramas, novopeso;
imprima "\nentre com seu peso, só a parte inteira: ;
leia peso;
pesogramas <- peso * 1000;
novopeso <- pesogramas * 1.12;
imprima "\npeso em gramas: ", pesogramas;
imprima "\nnovo peso: ", novopeso;
imprima fl\fl;
fi mprog """

peso = int(input('\nEntre com o seu peso, só a parte inteira: '))
pesogramas = peso * 1000
novopeso = pesogramas * 1.12
print(f'\nPeso em gramas : {pesogramas}')
print(f'\nNovo peso : {novopeso}')
print('\n')