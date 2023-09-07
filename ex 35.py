""" Ler nome, endereço e telefone e imprimi-los. 
prog lea8 
string nome, endereco, telefone; 
imprima "\nentre com nome: 
leia nome; 
imprima "\nentre com endereco: 
leia endereco; 
imprima "\nentre com telefone: 
leia telefone; 
imprima "\n\n\n"; 
imprima "\nNome : ",nome; 
imprima "\nEndereco: ",endereco; 
imprima \nTelefone: ",telefone; 
imprima "\n"; """

name=str (input('\nentre com nome: ' ))
endereco=str (input('\nentre com endereco:  ' ))
phone= str (input ('\nentre com telefone  ' ))

print ("\n\n\n")
print (f'\n Nome:{name}' )
print (f'\n Endereco:{endereco}' )
print (f'\n Telefone:{phone}' )