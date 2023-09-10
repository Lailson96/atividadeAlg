""" Ler uma temperatura em graus centígrados e apresentá-la convertida em graus
. 􀀀, 􀀀 - , 􀀀9.c+160
Fahrenheit. A formula de conversão e:F =
􀀀
onde F e a temperatura em
Fahrenheit e C é a temperatura em centígrados.
prog 1ea37
real f, c;
imprima "\ndigite o valor da temperatura em graus centigrados:
leia c;
f<_ (9*c+160)15;
imprima "\no valor da temperatura em graus fahrenheit e =', f;
imprima "\n";
fimprog """

c = float(input('\nDigite o valor da temperatura em graus centigrados: '))
f = (9 * c + 160) / 5
print(f'\nO valor da temperatura em graus fahrenheit é: {f}')
print('\n')