#generování náhodného slova
import random
from hangmanhra2 import stages

#uvítání hry

print("Vítejte ve hře hádání postav z filmu Harryho Pottera. Vaším úkolem je uhodnout písmeno z náhodně vybraného jména. Maximální počet pokusů je 6.")

words = ["harry", "ronald", "draco", "hermiona", "albus", "severus", "petunia", "minerva", "hagrid", "dobby", "lenka", "nevil", "dean", "remus","sirius", "peter", "james", "lily", "voldemort"]
random_word = words[random.randint(0, 18)]


#generování podtržítek

hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")

#počet životů

lives = 6
print(stages[lives])
#vypsáná slova do stringu

printedword = ""
for one_letter in hidden_word:
     printedword += one_letter
print(printedword)

while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess
      
#kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}.")
    if lives == 0:
        print("Prohráli jste.")
        break
        
        

#vypsání slova z listu do stringu

    printedword = ""
    for one_letter in hidden_word:
        printedword += one_letter
    print(printedword)
    

#kontrola vítězství
    if "_" not in hidden_word:
        print("Vyhráli jste!")