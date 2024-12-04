from animal import Animal
from dog import Dog

if __name__ == "__main__":
    
    my_animal = Animal("jacob", "canine")
    print(my_animal)
    my_animal.speak()
    
    my_dog = Dog("Rex", "canine", "wolf")
    print(my_dog)
    my_dog.speak()
    

    all_animals = Animal.get_all_animals()
    for animal in all_animals:
        print(animal)

