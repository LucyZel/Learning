class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

#3 objekty
dog1 = Dog("Harry", 3)
dog2 = Dog("Garry", 4)
dog3 = Dog("Lily", 6)

#funkce, která určí nejstaršího psa

def oldest(*args):
    return max(args)

result = oldest(dog1.age, dog2.age, dog3.age)
# dogs = [dog1, dog2, dog3]

# def oldest_dog(all_dogs):
#     oldest_age = 0
#     oldest_dog_name = ()
    
#     for one_dog in all_dogs:
#         if one_dog.age > oldest_age:
#             oldest_age = one_dog.age
            
#     return oldest_age

# result = oldest_dog(dogs)

print(f"Věk nejstaršího psa je: {result}.")
#result = oldest_dog(dogs)

    

