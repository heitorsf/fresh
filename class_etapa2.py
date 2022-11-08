"""
Etapa 2.
Descreve uma classe Products para ser usada para criar e interagir com um
banco de dados em MongoDB.
"""

from pymongo import MongoClient

class Products():
    # Initiallyzes MongoDB for all products
    client = MongoClient()
    db = client.products_db

    def __init__(self, name, description, price, image, ingredients, expiration):
        """Constructor class.
        
        Defines initial attributes for new instances."""
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.ingredients = ingredients
        self.expiration = expiration
        # Add to database as a document "food"
        self.id = self.db.food.insert_one(self.to_dict()).inserted_id

    def __repr__(self):
        """When called, print a line that could be used to recreate the object."""
        return f"Product(name='{self.name}', description='{self.description}', "\
            f"price={self.price}, image='{self.image}', ingredients='{self.ingredients}', "\
            f"expiration='{self.expiration}')"
    
    def __str__(self):
        """Formatted output of instance values."""
        return f"""
        Informações do produto:
            Nome: {self.name}
            Preço: R${self.price}
            Descrição: {self.description}
            Ingredientes: {self.ingredients}
            Validade: {self.expiration}"""
    
    def read(self, attribute):
        """Print attribute."""
        return getattr(self, attribute)
    
    def update(self, attribute, new_value, show_change=True):
        """Update the value of an attribute."""
        old_value = getattr(self, attribute)
        # To honor variable names, first update the database
        self.db.food.update_one({"_id": old_value}, {"$set": {attribute: new_value}})
        # Then, update the class attribute
        setattr(self, attribute, new_value)
        if show_change:
            print("Attribute '{}' updated from '{}' to '{}'".format(attribute, old_value, new_value))

    def show_price(self):
        """Example of utility function."""
        print(f"Preço do produto '{self.name}': R$ {self.price}")
    
    def to_dict(self):
        """Translate the object into a dictionary for possible saving purposed."""
        return vars(self)
    
    @staticmethod
    def interactive_create():
        """Interactively creates new instance."""
        print("Parar adicionar um novo produto, informe os seguintes campos:")
        name = input("Nome do produto: ")
        description = input("Descrição do produto: ")
        price = input("Preço em R$ (exemplo: 10,50): ")
        price = float(price.replace(',', '.'))
        image = input("Nome do arquivo com a imagem do produto: ")
        ingredients = input("Ingredientes (separados por vírgulas): ")
        expiration = input("Prazo de validade (exemplo: 2 meses): ")
        return Products(name, description, price, image, ingredients, expiration)

    @staticmethod
    def delete(instance):
        instance.db.food.delete_one({"_id": instance.id})