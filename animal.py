class Animal():
    """
    Base class representing a generic animal.
    """
    all_animal = []
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects
    def __init__(self, name, species, breed):
        self.name = name
        self.species = species
        self.breed = breed 

        Animal.all_animal.append(self)

        def __str__(self):
            return f"animal: {self.name}, species {self.species}, breed {self.breed}"

            @classmethod
            def get_all_animals(cls):
                return cls.all_animal

    # TODO create the initializer for Animal with name and species as attributs

    # TODO: Add a method to make a generic sound 
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""

    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute' 
