#cyklus while - určitá činnost, pokud je podmínka true

#x= 0 

#while x <= 10:
    #print(f"Já jsem {x} cyklus while")
    #x += 1
    
#print("Jedeme dál")

#hádací hra

import random

print("Vítejte v hádací hře Harry Potter")
characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albus"]
character = characters[random.randint(0, len(characters)-1)]
guess = ""
guess_count = 5

while character != guess:
    if guess_count != 0:
        guess = input("Uhodněte postavu z filmu Harry Potter\n")
        guess_count -= 1
    else:
        print("Počet pokusů k hádání je vyčerpán.")
        break
    if character == guess:
        print(f"Uhádli jste! Hádáné slovo bylo {character}.")