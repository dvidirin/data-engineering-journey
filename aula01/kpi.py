VALOR_CONSTANTE = 1000
# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o valor do seu sálario: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o valor do bônus: "))
# 4) Calcule o valor do bônus final
bonus_final = VALOR_CONSTANTE + salario_usuario * bonus_usuario
# 5) Imprime a mensagem personalizada incluindo o nome do usuário e bônus
print(f"Olá {nome_usuario}, o seu bônus foi de {bonus_final}.")