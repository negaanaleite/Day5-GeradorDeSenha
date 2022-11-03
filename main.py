# Projeto de gerador de senhas fortes
import random
letra =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numero = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
simbolo = ['!','#','$', '%','&','(',')','*','+']

print("---------------------------------------------")
print(" G E R A D O R  DE  S E N H A S  F O R T E")
print("----------------------------------------------")
letra2   =  int(input("Com quantas letras você deseja a sua senha: \n"))
numero2  =  int(input(f"Quantos números você gostaria: \n"))         
simbolo2 =  int(input(f"Quantos Simbolos você gostaria: \n"))

#facil
# Senha =" "
# for caracter in range(1,letra2 +1):
#     Senha += random.choice(letra)

# for caracter in range(1,numero2 +1):
#     Senha += random.choice(numero)

# for caracter in range(1,simbolo2+1):
#     Senha += random.choice(simbolo)
  #print(Senha)

Senha_forte = ""
for caracter in range(1,letra2 +1):
  Senha_forte += random.choice(letra)

for caracter in range(1,numero2 +1):
  Senha_forte += random.choice(numero)

for caracter in range(1,simbolo2+1):
  Senha_forte += random.choice(simbolo)
    
senha = ""
for caracter in Senha_forte:
  senha += caracter

print(f"Sua nove senha é: {senha}")
