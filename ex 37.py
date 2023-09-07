""" Ler dois números inteiros e imprimir o produto. 
prog lealO 
int numi, num2, prod; 
imprima "\n entre com um numero: 
leia numi; 
imprima "\n entre com outro numero: 
leia num2; 
prod <- numi * num2; 
imprima "\nproduto: ", prod; 
imprima "\n"; """


num1 = int (input('\nentre com um numero: '))
num2 = int (input('\nentre com outro numero: '))

print (f'\nnumero 1 :{num1}')
print (f'\nnumero 2 :{num2}')

prod= (num1*num2)

print(f"\nproduto:{prod} ")



