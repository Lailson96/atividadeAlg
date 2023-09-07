""" Ler um número inteiro e imprimir seu sucessor e seu antecessor. 
prog lea7 
int numero, suc, ant; 
imprima " \n entre com um numero: 
leia numero; 
ant <- numero —1; 
suc <- numero +1; 
imprima " \no sucessor e 1", suc,"b o antecessor e b", ant; 
imprima " \n " ; """

entrada=int (input('entre com um numero:' ))

ant= int(entrada-1)
suc=int(entrada+1)

print(f'\no antecessor e:{ant}')
print(f'\no sucessor e:{suc}')