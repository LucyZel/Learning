#numbers + if, else

print ("hello, welcome to Lucy's Coffe")

name = input ("What is your name? \n")

if name == "Ben" or name == "Patricia" or name == "Loki":
   evil_status = input ("Are you evil?\n") 
   good_deeds = int(input("How many good deed have you done today?\n"))
   if evil_status == "Yes" and good_deeds < 4:
    print ("You're not welcome here " + name + " get out!")
    exit ()
   else:
    print("Oh, so you're one of those good " + name + ". Come on in!")
    
else:
    print ("Hello " + name + ", thank you so much for coming in today.\n\n")


#print ("Hello " + name + ", thank you so much for coming in today.\n\n")


menu = "Pumkin spice latte, Nutmeg Latte, Americano"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input ()

#whiped cream

if order == "Pumkin spice latte":
    whiped_cream = input ("Do you want whiped cream?\n")
    if whiped_cream == "Yes":
       price = 11
    else:
       price = 9

#Set the price for coffe
#if order == "Pumkin spice latte":
    #price = 13
       
elif order == "Nutmeg Late":
    price = 10
elif order == "Americano":
    price = 6
else:
    print("Sorry, We don't have that here.")
    price = 0
    exit ()

print("Okay, the price for one coffee is " + str(price) + "€")

quantity = input ("How many coffes would you like?\n")

total = price * int(quantity)

print ("Thank you, your total is: " + str(total) + "€")

#print ("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready in a moment.")