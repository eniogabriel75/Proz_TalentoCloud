#Exercicio de aula
def mostrar():
  print("Insira um número ai: ")
  algoValido = False

  while (algoValido == False):
    try:
      algo = int(input("Insira oS num: "))
      if (algo %2 == 0):
        print(f"{algo} não é um número válido")
      else:
        inform = print(f"O que você escreveu: {algo}")
        algoValido == True
        return inform
    except:
      print ("Vocë deve inserir apenas números ímpares")

mostrar()