""" Ler dois números inteiros e imprimir a soma. Antes do resultado, deverá aparecer 
a mensagem: Soma. 
prog lea9 
int numi, num2, soma; 
imprima "\n entre com um numero: ; 
leia numi; 
imprima "\n entre com outro numero: 
leia num2; 
soma <- numi + num2; 
imprima "\nSoma: ", soma; 
imprima "\n"; """

num1 =int  (input('\nentre com um numero: '))
num2 =int  (input('\nentre com outro numero: '))

print(f'\nnum1:{num1}')
print(f'\nnum2 {num2}')
soma= (num1+num2)
print(f'\nsoma: {soma}')

