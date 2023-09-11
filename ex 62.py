""" Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
vendas oferecendo desconto. Faça um algoritmo que possa entrar com o valor de
um produto e imprima o novo valor tendo em vista que o desconto foi de 9%.
prog lea35
real preco, npreco;
imprima "\ndigite valor do produto:
leia preco;
npreco <-preco * 0.91;
imprima "\npreco com desconto: ",npreco;
imprima "\n";
fi mprog """

preco = float(input('\nDigite o valor do produto: '))
npreco = preco * 0.91

print(f'\nPreco com desconto: {npreco}')
print('\n')