#Gerador de senha segura

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for x in range(tamanho))
    return senha

tamanho = int(input('Digite o tamanho da senha: '))
senha = gerar_senha(tamanho)
print('Sua senha é: ', senha)
