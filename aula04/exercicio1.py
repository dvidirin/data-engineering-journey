# 1-Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista_num: list = list(range(1,11))
for num in lista_num:
    print(num**2)

# 2-Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)

# 3-Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: dict = {
    "titulo": "Harry Potter",
    "autor": "Não Lembro",
    "ano": 2000
}
for key, value in livro.items():
    print(f"{key} : {value}")

# 4-Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

def contar(s):
    contagem={}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem
print(contar("Daniel Vidiri Neto"))

# 5-Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista = ["maçã", "banana", "cereja"]
dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(dicionario[item] for item in lista)
print(f"Preço Total da Lista é {total:.2f}")