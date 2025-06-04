


# nome = str(input("Qual seu nome?"))
# email = str(input("Digite seu email:"))

# arquivo = open("Teste.txt", "a")
# arquivo.write(nome + " | " + email)

# nome2 = str(input("Qual seu nome?"))
# email2 = str(input("Digite seu email:"))


# with open("Teste2.txt", "a") as arquivo:
#     arquivo.write(nome2 + " | " + email2 + "\n")
# arquivo.close()

nome_produto = str(input("Qual o nome do produto?"))
produto_valor = int(input("Valor do produto:"))
Quantidade_produto = int(input("Quantos vão ser comprados?"))

with open("Produto.txt", "a") as Produto:
    Produto.write(f"{nome_produto}  | {produto_valor} | {Quantidade_produto}" f"\n Preço total a pagar: {produto_valor * Quantidade_produto}")
Produto.close()