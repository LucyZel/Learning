#objektově orentované programování
#zapouzdření - encapsulation
#abstraction = dáváme přístup pouze k tomu, co je k zapotřebí

#atributy a metody
class WizardPlayer:
    wizard_club = True
    #constructor
    def __init__(self,name="anonym", age=0):
        if age >= 18:
            self._name = name #._ = nemělo by se měnit, v pythonu není možnost "private"
            self.age = age
        
    def attack(self):
        print("Útok!")
    
    def age_checker(self):
        
        if self.age >= 18:
            print("Můžute hrát.")
        else:
            print("Nemůžete hrát, váš věk je příliš nízký.")

#player1 = WizardPlayer("Lucy", 29)
#print(WizardPlayer.test_function(60, 100))
player1 = WizardPlayer("Lucy", 20)
player1._name = "Hermiona"
# player1.attack = ("Ahoj")
# print(player1.attack)
