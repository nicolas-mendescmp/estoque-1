from produto import Produto
#criação do produto 1
p1 = Produto()
p1.nome = "Macarrão parafuso"
p1.quantidade = 5
# criação do produto 2
p2 = Produto()
p2.nome = "Molho de tomate"
p2.quantidade = 7

print(f"{p1.nome}: {p1.quantidade} un")
print(f"{p2.nome}: {p2.quantidade} un")