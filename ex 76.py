""" Criar um algoritmo que leia um número entre O e 60 e imprimir o seu sucessor, sabendo
que o sucessor de 60 é 0. Não pode ser utilizado nenhum comando de seleção
e nem de repetição.
prog leia49
int num;
imprima "\ndigite numero:
leia num;
imprima "\nsucessor: ", (num + 1) % 61;
imprima "\n";
fi mprog """

#Válido para números de 0 a 60

num = int(input('\nDigite um número: '))
print(f'\nSucessor : { (num + 1) % 61}')
print('\n')