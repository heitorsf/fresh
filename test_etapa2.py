from class_etapa2 import Products

ovo = Products("Ovos", "12 ovos de galinha branco.", 12.80, "ovo.png",
        "Apenas ovos.", "2 semanas")

leite = Products.interactive_create()

print(ovo)
ovo.update('name', "Ovos brancos.")
print(ovo.read('name'))