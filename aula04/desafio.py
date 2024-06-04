#Refatorar o código do desafio anterior usando Type Hint e Funcões.

# Usando função para calcular o bônus
def calculo_bonus(salary: float, bonus: float) -> float:
    VALOR_CONSTANTE = 1000
    bonus_final: float = VALOR_CONSTANTE + salary * bonus
    return bonus_final

# 1) Solicita ao usuário que digite seu nome
nome_valido: bool = False
while not nome_valido:
    try:
        nome: str = input("Digite seu nome: ")

        # Verifica se o nome é vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode ser vazio!")
        # verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números!")
        else:
            print("Nome válido: ", nome)
            nome_valido = True
    except ValueError as e:
        print(e) 

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_valido: bool = False
while not salario_valido:
    try:
        salario_usuario: float = float(input("Digite o valor do seu sálario: "))
        if salario_usuario < 0:
            print("Valor do salário não pode ser negativo!")
        else:
            salario_valido = True
    except ValueError:
        print("ERRO. Entrada Inválida. Digite um número!")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_valido: bool = False
while not bonus_valido:
    try:
        bonus_usuario: float = float(input("Digite o valor do bônus recebido: "))
        if bonus_usuario < 0:
            print("Valor do bônus não pode ser negativo!")
        else:
            bonus_valido = True
    except ValueError:
        print("ERRO. Entrada Inválida. Digite um número!")

# 4) Chamando a função para calcular o bônus
bonus_recebido = calculo_bonus(salario_usuario, bonus_usuario)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, o salário e bônus
print(f"Olá {nome}, seu salário é R${salario_usuario:.2f} e o seu bônus final é R${bonus_recebido:.2f}.")