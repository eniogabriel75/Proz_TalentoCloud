def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

while True:
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break
    elif opcao not in ("1", "2", "3", "4"):
        print("Essa opção não existe")
        continue

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if opcao == "1":
        resultado = soma(valor1, valor2)
    elif opcao == "2":
        resultado = subtracao(valor1, valor2)
    elif opcao == "3":
        resultado = multiplicacao(valor1, valor2)
    elif opcao == "4":
        resultado = divisao(valor1, valor2)

    print(f"Resultado: {resultado}")