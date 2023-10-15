import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

while True:
    nome = input("Digite seu nome completo: ")
    
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento (1922 a 2023): "))
    except ValueError:
        print("Ano de nascimento inválido. Por favor, insira um valor numérico.")
        continue

    if ano_nascimento > 1922 and ano_nascimento < 2023:
        idade = calcular_idade(ano_nascimento)
        print(f"Nome: {nome}")
        print(f"Idade em 2023: {idade} anos")
        break
    else:
        print("Ano de nascimento fora do intervalo válido (1922 a 2023). Tente novamente.")
