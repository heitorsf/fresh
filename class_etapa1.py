"""
Etapa 1.
Este arquivo descreve uma classe Product no contexto de POO,
sem levar em conta associação com bancos de dados.
"""

class Product:
    """Base class for creating a product.
    
    Attributes
    ----------
    name : str
        Complete name of the product.
    description : str
        Detailed information on the product.
    price : float > 0
        Value in R$ (BRL) of the product.
    image : str
        Name of the file containing the image of the product.
    ingredients : str
        Written list of the ingredients in the product.
    expiration : str
        Expiration time in months.
    
    Methods
    -------
    __init__(self)
    __repr__(self)
    __str__(self)
    read(self)
    update(self, attribute, new_value)
    show_price(self)
    create() is a static method
    """

    def __init__(self, name, description, price, image, ingredients, expiration):
        """Constructor class.
        
        Defines initial attributes for new instances."""
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.ingredients = ingredients
        self.expiration = expiration
        print(vars(self))

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
        """Calls method __str__."""
        return getattr(self, attribute)
    
    def update(self, attribute, new_value, show_change=True):
        """Update the value of an attribute."""
        old_value = getattr(self, attribute)
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
    def create():
        """Interactively creates new instance."""
        print("Parar adicionar um novo produto, informe os seguintes campos:")
        name = input("Nome do produto: ")
        description = input("Descrição do produto: ")
        price = input("Preço em R$ (exemplo: 10,50): ")
        price = float(price.replace(',', '.'))
        image = input("Nome do arquivo com a imagem do produto: ")
        ingredients = input("Ingredientes (separados por vírgulas): ")
        expiration = input("Prazo de validade (exemplo: 2 meses): ")
        return Product(name, description, price, image, ingredients, expiration)