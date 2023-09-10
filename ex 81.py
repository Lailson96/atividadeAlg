""" Criar um algoritmo que, dado um número de conta corrente com três dígitos, retorne
o seu dígito verificador, o qual é calculado da seguinte maneira:
Exemplo: número da conta: 235
Somar o número da conta com o seu inverso: 235+ 532 = 767
multiplicar cada dígito pela sua ordem posicional e somar estes resultados: 767
7 􀀀6 7
Xl X2 X3
7 + 12 + 21 =40
o último dígito desse resultado é o dígito verificador da conta (40 -> 0).
prog 1ea54
int conta, mv, digito, dl, d2, d3,soma;
imprima "\nDigite conta de tres digitos:
leia conta;
dl <- conta div 100;
d2 <- conta % 100 div 10;
d3 <- conta % 100 % 10;
mv <- d3 *100 + d2 *10 +dl;
soma <- conta + mv;
dl <- (soma div 100) *
d2 <- (soma % 100 div 10) * 2;
d3 <- (soma % 100 % 10) *3;
digito <- (dl +d2 +d3) % 10;
imprima "\ndigito verificador: ", digito;
imprima " \n " ;
fimprog """

conta = int(input('\nDigite a conta de três dígitos: '))
d1 = int(conta / 100)
d2 = int(conta % 100 / 10)
d3 = int(conta % 100 % 10)
inv = int(d3 * 100 + d2 * 10 + d1)
soma = int(conta + inv)
d1 = int(soma / 100) * 1
d2 = int(soma % 100 / 10) * 2
d3 = int(soma % 100 % 10) * 3
digito = int(d1 + d2 + d3) % 10
print(f'\nDigito verificador: {digito}')
print('\n')