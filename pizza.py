pizza_size=input("Vítejte v aplikaci na objednání pizzy. Jakou velikost pizzy chcete? S, L nebo M?\n")

if pizza_size == "S":
    basic_price = 100
    topping_1 = input("Chcete feferonky? Ano nebo ne?\n")
    if topping_1 == "Ano":
        price = 20
    else:
        price = 0
elif pizza_size == "M":
    basic_price = 150
    topping_1 = input("Chcete feferonky? Ano nebo ne?\n")
    if topping_1 == "Ano":
        price = 30
    else:
        price = 0
elif pizza_size == "L":
    basic_price = 200
    topping_1 = input("Chcete feferonky? Ano nebo ne?\n")
    if topping_1 == "Ano":
        price = 30
    else:
        price = 0
topping_2 = input ("Chcete extra sýr? Ano nebo ne?\n")
if topping_2 == "Ano":
    add_price = 15
else:
    add_price = 0

total = basic_price + price + add_price

print(f"Částka k zaplacení: {total} Kč.")