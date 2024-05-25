# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
print(f"O resultado da soma de {n1} + {n2} é {soma}.")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
n = int(input("Digite o número: "))
resto = n % 5
print(f"O resto da divisão de {n} dividido por 5 é {resto}.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
mult = n1 * n2
print(f"O resultado da multiplicação de {n1} vezes {n2} é {mult}.")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
divisao = n1 // n2
print(f"O resultado da divisão inteira de {n1} por {n2} é {divisao}.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
n = int(input("Digite o número: "))
quadrado = n ** 2
print(f"O quadrado de {n} é {quadrado}.")

#### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
soma = n1 + n2
print(f"O resultado da soma de {n1} + {n2} é {soma}.")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
media = (n1 + n2)/2 
print(f"A média é {media}.")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
n1 = float(input("Digite a base: "))
n2 = float(input("Digite o expoente: "))
resul = n1 ** n2 
print(f"A potência do número {n1} elevado a {n2} é {resul}.")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
cel = float(input("Digite a temperatura em Celsius: "))
fah = (cel * 1.8) + 32 
print(f"A temperatura de {cel}\u00B0C é igual a {fah}\u00B0F.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio do círculo: "))
area =  math.pi * raio ** 2
print(f"A área do círculo com raio {raio} é {area:.2f}.")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
s = input("Digite uma palavra: ")
print(f"A palavra em maiúscula será: {s.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
s = input("Digite o seu nome completo: ")
print(f"O seu nome em minúsculo será: {s.lower()}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
s = input("Digite uma frase: ")
print(f"A frase sem espaços em branco: {s.strip()}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
s = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = s.split("/")
print(f"O dia é {dia}")
print(f"O mês é {mes}")
print(f"O ano é {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
s1 = input("Digite a primeira frase: ")
s2 = input("Digite a segunda frase: ")
print(f"A frase concatenada é: {s1 + s2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
v1 = True 
v2 = False
print(f"O resultado de {v1} AND {v2} é {v1 and v2}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print(f"O resultado de {v1} OR {v2} é {v1 or v2}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print(f"O resultado invertido de {v1} é {not v1}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resul = n1 == n2
print(f"Os dois números são iguais? Resposta: {resul}.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
dife = n1 != n2
print(f"Os dois números são diferentes? Resposta: {dife}.")

# #### try-except e if

# 21: Conversor de Temperatura
try:
    cel = float(input("Digite a temperatura em Celsius: "))
    fah = (cel * 1.8) + 32 
    print(f"A temperatura de {cel}\u00B0C é igual a {fah}\u00B0F.")
except ValueError:
    print("Digite um número válido para a temperatura")

# 22: Verificador de Palíndromo
palavra = input("Digite uma palavra: ")
if isinstance(palavra, str):
    formatado = palavra.replace(" ","").lower()
    if formatado == formatado[::-1]:
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo")
else:
    print("Entrada Inválida!")

# 23: Calculadora Simples
try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador desejado (+, -, *, /): ")
    if operador == "+":
        resultado = n1 + n2
    elif operador == "-":
        resultado = n1 - n2
    elif operador == "*":
        resultado = n1 * n2
    elif operador == "/":
        resultado = n1 / n2
    else:
        print("Operador Inválido!")
    print(f"O resultado de {n1} {operador} {n2} = {resultado}.")
except ValueError:
    print("Erro. Entrada Inválida. Digite somente números.")

# 24: Classificador de Números
try:
    n = float(input("Digite um número: "))
    if n > 0:
        print(f"O número {n} é um número positivo.")
    elif n < 0:
        print(f"O número {n} é um número negativo.")
    else:
        print(f"O número {n} é igual a zero.")
    if n % 2 == 0:
        print(f"O número {n} é par.")
    else:
        print(f"O número {n} é ímpar.")
except ValueError:
    print("Erro. Entrada Inválida. Digite somente números.")

# 25: Conversão de Tipo com Validação
entrada = input("Digite uma lista de números separados por vírgula: ")
numstr = entrada.split(",")
numint = []
try:
    for num in numstr:
        numint.append(int(num.strip()))
    print("A lista de inteiros digitada é: ", numint)
except ValueError:
    print("Erro. Entrada Inválida. Digite somente números inteiros válidos!")