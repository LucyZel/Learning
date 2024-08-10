#rok = int(input("Zadejte rok.\n"))
#if rok %4 == 0 %100 == 0 %400 == 0:
    #print("Jedná se o přestupý rok.")

#else:
    #print("Nejedná se o přestupný rok.") 

#objednání pizzy

pizza_size=input("Vítejte v aplikaci na objednání pizzy. Jakou velikost pizzy chcete? S, L nebo M?\n")

topping1 =input("Chcete feferonky? Ano nebo ne?")

topping2 = input("Chcete sýr navíc? Ano nebo ne?\n")

if pizza_size == "S":
    basic_price = 100
    if topping1 == "Ano":
        basic_price = 100 + 20
    elif topping2 == "Ano":
        basic_price = 120 + 15
    else:
        basic_price = 100
print(f"Částka k zaplacení je {basic_price} Kč.")

