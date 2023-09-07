""" Entrar com dois numeros reais e imprimir a media aritmética com a mensagem
media antes do resultado
prog leal2
real notal, nota2, media;
imprima "\ndigite la nota:,
leia notal;
imprima "\ndigite 2a nota: U;
leia nota2;
media <- ( notal + nota2)/2;
imprima "\nmedia ", media,
imprima "\n";  """

Nota1= int (input('\ndigite la nota:'))
Nota2= int (input('\ndigite 2a nota:'))

print(f'\nNota1: {Nota1}')
print(f'\nNota2: {Nota2}')

Media=((Nota1+Nota2)/2)
print(f"\nmedia: {Media} ")