#moduly

import math
import random
#generování náhodného celého čísla z rozsahu
#print(random.randint(10, 18))

#generování náhodného desetinného čísla mezi 0 a 1
#print(random.random())

#generování náhodného čísla z rozmezzí + krok
#print(random.randrange(15, 25, 2))

#print(math.ceil(5.1)) #6 - zakohrouhlení nahoru
#print(math.floor(5.8)) #6 - zakokrouhlení dolů

#print(math.ceil(random.random() *6))
#print(math.ceil(random.random() *6))
#print(math.ceil(random.random() *6))
#print(math.ceil(random.random() *6))
#print(math.ceil(random.random() *6))
#print(math.ceil(random.random() *6))
#print(math.ceil(random.random() *6))

#side_coin = random.randint (0, 1)

#if side_coin == 0:
    #print("Hlava")
#else:
    #print ("Orel")

#import random
#name = input("Napiš mi jména všech, ale oddělené čárkou\n")

#list_people = name.split(", ")
#random_number = random.randint (0, len(list_people)-1)

#print(f"{list_people[random_number]} bude dnes platit účet.")

import random
rock = '''
_______
---' ____)
     (_____)
     (_____)
      (____)
---.__(___)
'''
paper = '''
_______
---' ____)____
          ______)
            _______)
           _______)
---.__________)
'''
scissors = '''
_______
---' ____)____
          ______)
        __________)
      (____)
---.__(___)
'''

all_list = [rock, paper, scissors]
users_choice = int(input("Co si vyberete? Napište 0 pro kámen, 1 pro nůžky a 2 pro papír.\n"))
users_picture = all_list [users_choice]

computers_choice = random.randint (0, 2)
computers_picture = all_list [computers_choice]

print(f"Uživatel si vybral:\n {users_picture}")
print(f"Počítač si vybral:\n {computers_picture}")

if users_choice == computers_choice:
    print("Je to remíza")
elif  users_choice == 0 and computers_choice == 1:
    print("Prohrál jsi. Počítač vyhrál.")
elif users_choice == 0 and computers_choice == 2:
    print("Vyhrál jsi. Počítač prohrál.")
elif users_choice == 1 and computers_choice == 0:
    print("Vyhrál jsi. Počítač prohál.")
elif users_choice == 1 and computers_choice == 2:
    print("Prohál jsi. Počítač vyhrál.")
elif users_choice == 2 and computers_choice == 0:
    print ("Prohrál jsi. Počítač vyhrál.")
elif users_choice == 2 and computers_choice == 1:
    print ("Vyhrál jsi. Počítač prohrál.")