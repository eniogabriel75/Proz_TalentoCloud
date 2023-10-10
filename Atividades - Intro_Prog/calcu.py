def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
print("1 - SOMA --- 2 - Subtração --- 3 - Multiplicação --- 4 - Divisão" )
operacao = int(input("Insira uma opção: \n"))

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)