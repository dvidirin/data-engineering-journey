# 16-Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

lista = [1, 2, 3, 4]
def lista_somada(lista: list) -> int:
    return sum(lista)

total = lista_somada(lista)
print(f"A soma dos números da lista é: {total}")

# 17-Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def descobre_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
    
number = 100
resultado = descobre_primo(number)
print(f"O número {number} é Primo? R: {resultado}.")

# 18-Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def string_revertida(palavras: str) -> str:
    return palavras[::-1]

texto_original = "Hello World!"
texto_revertido = string_revertida(texto_original)
print(texto_revertido)

# 19-Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def encontrar_pares(lista, numero):
    pares = []
    vistos = {}
    for valor in lista:
        complemento = numero - valor
        if complemento in vistos:
            pares.append((complemento, valor))
        vistos[valor] = True
    return pares

lista_numeros = [2, 4, 3, 3, 5, 7, 8, -2]
numero = 6
resultado = encontrar_pares(lista_numeros, numero)
print(f"Pares que somam {numero}: {resultado}")

# 20-Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

def ordenar_chaves(dicionario):
    return sorted(dicionario.keys())

meu_dicionario = {'banana': 3, 'maçã': 5, 'laranja': 2, 'uva': 4}
chaves_ordenadas = ordenar_chaves(meu_dicionario)
print(chaves_ordenadas)