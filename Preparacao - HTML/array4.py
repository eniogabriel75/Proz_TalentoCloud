"""A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente!
Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo 
rímel ao invés de batons, e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores,
então precisam que você remova ele da lista de produtos. Imprima a nova lista no terminal para verificar 
que as alterações foram realizadas corretamente."""

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 
'sabonetes', 'delineadores'] 
lista_produtos[1] = "rímel"
lista_produtos[4] = "cremes hidratantes"
lista_produtos.pop()
print("Itens da loja: ")
for i in range(len(lista_produtos)):
  print("Temos o produto", lista_produtos[i], "à venda")