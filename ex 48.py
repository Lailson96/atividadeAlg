""" Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabendo-
se que 100 quilowatts de energia custa um sétimo do salário mínimo,
fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts
gasta por uma residência e calcule. Imprima:
o valor em reais de cada quilowatt
m o valor em reais a ser pago
o novo valor a ser pago por essa residência com um desconto de 10%.
prog lea2l
real sm, qtdade, preco, vp, vd;
imprima "\nentre com o salário mínimo:
leia sm;
imprima "\nentre com a quantidade em quilowatt:
leia qtdade;
# divide por 7 para achar o preço de 100 Kw e por 100 para achar de 1 Kw
preco <- sm 1700;
vp <- preco * qtdade;
vd <- vp * 0.9;
441 imprima "\npreço do quilowatt: , preco, "\n valor a ser pago: ", vp,
" \n valor com desconto: ", vd;
imprima u\n; """

import math as m

sm = float(input('\n Entre com o salário mínimo: '))

quantidade = float(input('\nEntre com a quantidade de quilowatt: '))
preco = sm / 700
vp = preco * quantidade
vd = vp * 0.9

print(f'\nPreço do quilowatt: {preco}\nValor a ser pago: {vp}\nValor com desconto: {vd} ')
print('\n')
