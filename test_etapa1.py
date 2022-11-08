from class_etapa1 import Product

ovo = Product("Ovo", "12 ovos de galinha branco.", 12.80, "ovo.png", "Ovos.", "2 semanas")
leite = Product.create()

ovo.update('name', "Dúzia de ovos")
print(ovo)
print(leite)