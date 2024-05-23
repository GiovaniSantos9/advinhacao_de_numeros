#Jogo de adivinhar numeros feito pelo Giovani Dos Santos

import random
import math

#Tratamento de erros caso o usuário introduza qualquer coisa além de um numero
def numero_valido(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

#Difinir o limite de numeros apartir do input do usuário
print("\nSelecione o interavalo de números")
limite_inferior = numero_valido("Digite o número do limite inferior: ")
limite_superior = numero_valido("Digite o número do limite superior: ")

#Tratamento de erro caso o usuário introduza um limite superior menor que o limite inferior
while limite_inferior > limite_superior:
    print("\nO limite superior deve ser maior que o limite inferior.\n")
    limite_superior = numero_valido("Digite o número do limite superior novamente: ")

numero_secreto = random.randint(limite_inferior, limite_superior ) #O programa escolhe um numero aleatorio dentro do limite de numeros

total_de_tentativas = int(math.log2(limite_superior - limite_inferior)+ 1) #Formula para definir o numero de tetativas dependendo do limite de numeros

print("\nVocê tem um total de",total_de_tentativas,"tentativas\n") #Mostrar o numero de tentativas ao usuario

#loop até o total de tentativas
for tentativa in range(1, total_de_tentativas + 1):   
    print(f"Tentativas {tentativa} de {total_de_tentativas}") #Informar o numero de tentativas atual e restantes
    numero_escolhido = numero_valido("Digite um número: ") #Chute um numero

    #Definir um limite dentro do intervalo
    if numero_escolhido < limite_inferior or numero_escolhido > limite_superior:
        print("\nNúmero inválido. O numero deve estar entre",limite_inferior,"e",limite_superior,"\n")
        continue

    if numero_escolhido == numero_secreto:                  #condição de vitória
        print("\nParabéns! Você acertou o número!\n")
        break
    elif numero_escolhido > numero_secreto:
        print("Tente novamente! Seu palpite foi alto demais.\n")    #DICAS
    else:
        print("Tente novamente! Seu palpite foi baixo demais.\n")

    if tentativa == total_de_tentativas:
        print("Você perdeu. Tente novamente.\n")     #informar ao usuário caso ele perca   

print("O número secreto era",numero_secreto)     
print("Fim do Jogo")



