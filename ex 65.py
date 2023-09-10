""" Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:
volume = 3.14159 * R2 * altura.
prog lea38
real volume, altura, raio;
imprima "\ndigite a altura da lata:
leia altura;
imprima "\ndigite o raio da lata:
leia raio;
volume <- pi *raio ** 2 *alt u ra ;
imprima "\no volume da lata e = ", volume;
imprima "\n";
fimprog """

altura = float(input('\nDigite a altura da lata: '))
raio = float(input('\nDigite o raio da lata: '))
volume = 3.14 * raio ** 2 * altura
print(f'\nO volume da lata é: {volume}')
print('\n')