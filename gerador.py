import random
import string

def gerar_senha(comprimento, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    if comprimento <= 0:
        return "Comprimento inválido!"

    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Nenhuma opção selecionada!"

    return ''.join(random.choice(caracteres) for _ in range(comprimento))
