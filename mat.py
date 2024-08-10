#print ("ahoj" [3])
#integer
#print (5 + 15) 
#print (123456)
#print (123_456)

#float - desetinné číslo
#print (3.14)
#print (0.25)

#boolean
#True 
#False

#age = 40
#print ("Ahoj, já jsem Lucy a je mi " + str(age) + " let")

#number = input("Napište dvoumístné číslo\n")
#number1 = int (number[0])
#number2 = int (number [1])
#print (number1 + number2)


#()
#**
#*
#*/
#+-

#BMI výpočet
# BMI = váha v kg / (výška v m)na2

#height = input("Zadejte svou výšku  v metrech:\n")
#weight = input("Zadejte svou váhu v kg:\n")

#bmi = int(weight) / float(height)**2
#bmi = int(bmi)

#print("Vaše BMI je: " + str(bmi))

#zaokrouhlení
#print (8//3)

#print(round(8/3))
#print (5/2)
#print (round(5.002/2)) - zaokrouhlení ,5

#print(round(8/3,2)) - desetinné číslo

#x = 1
#x = x + 1
#x += 1 - zkrácený zápis

#x = x * 2
#x *= 2
#print(x)

#F-string

#x = 5
#print(f"Proměnná x má hodnotu:{x}")

#name = "Lucy"
#age = 28
#print(f"Jmenuje se {name} a je jí {age} let.")

#procvičování
#average_age = 90
#age = input("Kolik Vám je let?\n")
#years = int(average_age) - int(age)
#months = int(years) * 12
#days = int(years) * 365
#print(f"Do {average_age} let Vám zbývá {years} let, {months} měsíců a {days} dnů.")

print("Vítejte v kalkulátoru na výpočet plateb")

total_price = int(input("Kolik máte celkem zaplatit? "))
change = int(input("Kolik chcete dát spropitného (v %)? "))

people = int(input ("Mezi kolik lidí se má rozdělit částka? "))

final_price = (total_price +(total_price * change / 100)) / people

#payment = round(final_price / people ,2) -zaokrouhlední

final_payment = "{:.2f}".format(final_price)
#payment = (total_price + (total_price * change / 100)) / people
print(f"Každý člověk by měl zaplatit {final_payment} Kč")
