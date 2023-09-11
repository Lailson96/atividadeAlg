""" Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem,
sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo
gasto na viagem e a velocidade média.
Utilizar as seguintes fórmulas: 􀀀distância = tempo x velocidade.
litros usados = distância / 12.
O algoritmo deverá apresentar os valores da velocidade média, tempo gasto
na viagem, distância percorrida e a quantidade de litros utilizados na viagem.
51
prog 1ea39
real tempo, vel, dist, litros;
imprima "\ndigite o tempo gasto:
leia tempo;
imprima "\ndigite a velocidade media:
leia vel;
dist <- tempo * vel;
litros <- dist / 12;
imprima "\nvelocidade = ", vel, "\ntempo = , tempo, "\ndistancia =
dist, "\nlitros = ", litros;
imprima 11 \n";
fi mprog """

tempo = float (input('\nDigite o tempo gasto: '))
vel = float(input('\nDigite a velocidade média: '))
dist = tempo * vel
litros = dist / 12

print(f'\nVelocidade: {vel} \nTempo: {tempo} \nDistância: {dist} \nLitros: {litros}')
print('\n')