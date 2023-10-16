'''Copie o array apresentado embaixo no seu editor de código, e imprima no terminal: a quantidade de elementos que ele
possui, o dado salvo no índice 2, o dado salvo no índice 9, e dado salvo no índice 14.'''

lista_musicos = [ 'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty',
'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] 

qtd = len(lista_musicos)
elementos = [2, 9, 14]
print(f"Quantidade de elementos do vetor: {qtd}")
print("Os mais aclamados pelo público: ")
for indice in elementos:
  print(lista_musicos[indice])