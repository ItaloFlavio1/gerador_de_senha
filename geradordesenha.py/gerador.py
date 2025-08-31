import random
import string   

def gerar_senha (comprimento , usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres= ''
    if usar_letras: 
        caracteres += string.ascii_letters
    if usar_numeros:    
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Nenhum tipo de caractere Selecionado. Não foi possível gerar a senha"

    senha = ''.join(random.choice(caracteres)for _ in range (comprimento))
    return senha

def main ():
    print ("--- GERADOR DE SENHAS ---")
    print ("--By : Italo Augusto--")
    print ("-Feito em Python e utilizando bibliotecas Random,String-")
    print ()

    try:
        comprimeto = int(input("Qual o comprimento da senha desejada? (ex: 12):"))
    except ValueError:
        print("Entrada invalida. Por favor, insira um número inteiro.")
        return
    usar_simbolos_imput = input("Incluir simbolos? (s/n):").lower()
    usar_simbolos = usar_simbolos_imput == 's'

    usar_numeros_imput = input ("Incluir números? (s/n):").lower()
    usar_numeros = usar_numeros_imput == 's'

    usar_letras_input = input("Incluir letras?(s/n):").lower()
    usar_letras = usar_letras_input == 's'

    if comprimeto <= 0:
        print ("O Cumprimento deve ser um Número positivo.")
        return
    gerar_gerada = gerar_senha(comprimeto, usar_letras, usar_numeros, usar_simbolos)
    print(f"\nSua senha gerada é: {gerar_gerada}")
if __name__ == "__main__":
    main()

