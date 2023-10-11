def estoque(array):
  print("Controle de estoque, selecione a opção: ")
  print("1 - Verificar itens em estoque ")
  print("2 - Modificar item em estoque ")
  print("3 - Adicionar item em estoque ")
  print("4 - Encerrar ")
  op = False
  while op == False:
    escolha = int(input("Selecione a opção "))
    if escolha == 1:
      for i in range(len(array)):
        print(f"Prateleira: {i} - Produto - {array[i]}")
    elif escolha == 2:
      print("Deseja alterar qual produto de qual prateleira? ")
      prat = int(input())
      print("Qual novo produto: ")
      novo_prod = input()
      array[prat] = novo_prod
      print(f"O produto {novo_prod} foi alterado para a prateleira {prat} ")

    elif escolha == 3:
      print("Digite o nome do produto que deseja adicionar ao estoque:")
      novo_prod = input()
      array.append(novo_prod)
      print(f"O produto {novo_prod} fo adicionado no estoque")

    elif escolha == 4:
      print("Programa encerrado ")
      break

lotes = ["leite", "pão", "chocolate", "bolacha"]
estoque(lotes)
