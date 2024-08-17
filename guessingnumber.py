import random
import os
from guessingnumberlogo import logo

print(logo)
print("Vítejte ve hře guess secret number. Porazte počítač.")
print("Myslím si číslo od 1 do 100")


#příprava hry


def difficulty ():
    difficulty = input("Vyberte obtížnost. Napiště 'easy' nebo 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
     
#počet pokusu
def guessing_game():
    
    secret_number = random.randint(1, 100)
    print(f"Hádané číslo je {secret_number}")
    
    attemps = difficulty()
  

    another_game = ""
                
    while attemps > 0:
        print(f"Váš počet zbývajících pokusů je {attemps}")
        guess = int(input("Typněte si číslo: "))
        
        if guess < secret_number:
            print("Příliž nížské")
            attemps -= 1
        elif guess > secret_number:
            print("Příliž vysoké")
            attemps -= 1
        else:
            print("Vyhráli jste. Počítač byl poražen!")
            another_game = input("Napište 'yes', pokud chcete pokračovat. Napište 'no, pokud chcete hru ukončit ")
        
        if attemps == 0:
            print("Prohráli jste. Počítač vyhrál!")
            another_game = input("Napište 'yes', pokud chcete pokračovat. Napište 'no, pokud chcete hru ukončit ")
            
        if another_game == "yes":
            os.system("clear")
            guessing_game()
        elif another_game == "no":
            os.system("clear")
            break

guessing_game()
    