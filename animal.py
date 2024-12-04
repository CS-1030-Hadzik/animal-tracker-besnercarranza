class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    all_animals = []
    # TODO create a class-level attribute that is a list of all the Animal objects
    def __init__(self, name, species):
        self.name = name
        self.species = species 

        Animal.all_animals.append(self)

    def speak(self):
        print("The animal makes a noise")

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}' Species: '{self.species}'"

    @classmethod
    def get_all_animals(cls):
        return cls.all_animals

    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute' 
