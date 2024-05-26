### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome é vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode ser vazio!")
    # verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números!")
    else:
        print("Nome válido: ", nome)
except ValueError as e:
    print(e) 

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o valor do seu sálario: "))
    if salario_usuario < 0:
        print("Valor do salário não pode ser negativo!")
except ValueError:
    print("ERRO. Entrada Inválida. Digite um número!")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario = float(input("Digite o valor do bônus recebido: "))
    if bonus_usuario < 0:
        print("Valor do bônus não pode ser negativo!")
except ValueError:
    print("ERRO. Entrada Inválida. Digite um número!")

# 4) Calcule o valor do bônus final
VALOR_CONSTANTE = 1000

bonus_final = VALOR_CONSTANTE + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e bônus
print(f"Olá {nome}, o seu bônus foi de {bonus_final}.")