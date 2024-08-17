# Tento cyklus je jedním z nejběžnějších a nejdůležitějších prvků Pythonu, který se používá pro iteraci (procházení) přes sekvence, jako jsou seznamy, n-tice, řetězce, slovníky a další iterovatelné objekty.

# proměnná: Toto je jméno proměnné, která v každé iteraci cyklu přijímá hodnotu z sekvence. Tento název může být jakýkoli platný identifikátor, který si vybereš.
# •	sekvence: Toto je sekvenční objekt (například seznam, n-tice, řetězec, atd.), přes který cyklus prochází. Cyklus for prochází každý prvek v této sekvenci, a v každé iteraci přiřazuje aktuální prvek proměnné proměnná.
# •	Blok kódu: Kód uvnitř cyklu, který se vykonává pro každý prvek v sekvenci.

# animals = ['cat', 'dog', 'bird']

# for animal in animals:
# print(animal)
    
# V tomto příkladu:

# 	•	animals je seznam, který obsahuje tři prvky: 'cat', 'dog' a 'bird'.
# 	•	for animal in animals znamená, že cyklus projde každý prvek v seznamu animals.
# 	•	print(animal) vytiskne aktuální prvek na obrazovku.
# výstup:
# cat
# dog
# bird


# word = "hello"

# for letter in word:
#     print(letter)


# V tomto příkladu:

# 	•	word je řetězec "hello".
# 	•	for letter in word znamená, že cyklus projde každý znak v řetězci word.
# 	•	print(letter) vytiskne každý znak na obrazovku.
 
#  výstup:
# h
# e
# l
# l
# o

#ovoce = ["jablko", "hruška", "pomeranč", "jahoda"]

#for jedno_ovoce in ovoce:
    #print(jedno_ovoce)
    #print(f"Nezapomeň koupit {jedno_ovoce}")

#print("Pokračujeme dále.")

#height = input("Vložte výšky lidí oddělené mezerou:\n")

#heights_list = height.split (", ")
#suma = 0

#for all_hight in heights_list:
    #suma = suma + int(all_hight)

#average_height = suma / len(heights_list)

#print(f"Průměrná výška je: {average_height}")


#nejvyšší skóre
#score = [98, 50, 25, 78, 92]
#print(mas(score))
#print(min(score))

#score = input("Zadejte skóre jednotlivých studentů oddělené čárkou a mezerou\n")
#score_list = score.split(", ")
#score_list_number = []
#maximum = 0

#for index in range(0, len(score_list)):
    #score_list_number.append(int(score_list[index]))

#for one_number in score_list_number:
    #if one_number > maximum:
        #maximum = one_number
#print(f"Maximum je {maximum}.")


#range
#for one_number in range (1,5):
    #print(one_number)

#range s kroky
#for one_number in range (1,11,2):
    #print(one_number)

#suma čísel
#suma = 0

#for one_number in range (1, 101):
    #suma = suma + one_number
    #suma += one_number

#print(suma)

#suma = 0
#for one_number in range (1, 101):
    #if one_number % 2 == 0:
        #suma += one_number

#print (suma)

#číslo dělitelné 3 = Fizz
#číslo dělitené 5 = Buzz
#číslo dělitelné 3 a 5 = FizzBuzz
#jinak vypsat běžné číslo


#for one_number in range(1, 101):
    #if one_number % 3 == 0 and one_number % 5 == 0:
        #print("FizzBuzz")
    #elif one_number % 5 == 0:
        #print("Buzz")
    #elif one_number % 3 == 0:
        #print("Fizz")
    #else:
        #print(one_number)

#myName = "Lucy"
#myList = [5, 8, 10, True]

#for one_letter in myName:
    #print(one_letter)

#for one_character in myList:
    #print(one_character)