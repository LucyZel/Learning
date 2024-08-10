#podmínky
#pokud je odpověď jako text, musí se použít string!! ""
#!= - nerovná se
# .lower() - používat, aby se nemuselo spoléhat na správnost přepisu, text se automaticky převede na malá písmena
#normal, smart, extrasmart
#type = input("Jaký chcete typ mobilního telefonu? Možnosti: Normal, smart, extrasmart.\n")

#if type != "normal":
    #print(f"Cena telefonu typu {type} je 25.000 Kč\n")
#else:
    #print(f"Cena telefonu typu {type} je 15.000 Kč\n")
#elif
print("Vítejte na horské dráze")
height = int(input ("Jaká je vaše výška v cm?\n"))
bill = 0

if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaký je váš věk?\n"))
    if age < 12:
        bill = 50
        print("Cena vašeho lístku je 50 Kč.")
    elif age >= 12 and age < 18:
        bill = 100
        print("Cena vašeho lístku je 100 Kč.")
    elif age >= 40 and age <=50:
        bill = 0
    else:
        bill = 150
        print("Cena vašeho lístku je 150 Kč.")

    photo = input("Chcete během jízdy vyfotit? Ano nebo ne?\n")
    if photo == "ano":
        bill = bill + 40
        #bill += 40

    print(f"Vaše cena je {bill} Kč")

else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")



#age = int(input("Zadejte svůj věk.\n"))

#if age >= 18:
    #print("Jste dospělý.")

#else:
    #print("Nejste dospělý.")

#occupation = input("Vítejte na této stránce k zakoupení lístků na horskou dráhu. Jste student? Odpovězte ano nebo ne.\n")

#if occupation == "ano":
   # print("Cena lístku je 120 Kč.")
#else:
    #print ("Cena lístku je 150 Kč.")