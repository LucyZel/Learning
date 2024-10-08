from source_data import MENU
from source_data import resources

# Základní nastavení
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# Funkce
def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mléko: {data['milk']}")
    print(f"Káva: {data['coffee']}")

def coins():
    print("Prosím vložte mince 1, 2, 5, 10, 20, 50")
    kc1 = int(input("kolik 1 Kč chcete vložit?: "))
    kc2 = int(input("Kolik 2 Kč chcete vložit?: ")) * 2
    kc3 = int(input("Kolik 5 Kč chcete vložit?: ")) * 5
    kc4 = int(input("Kolik 10 Kč chcete vložit?: ")) * 10
    kc5 = int(input("Kolik 20 Kč chcete vložit?: ")) * 20
    kc6 = int(input("Kolik 50 Kč chcete vložit?: ")) * 50
    
    suma = kc1 + kc2 + kc3 + kc4 + kc5 + kc6
    print(f"Celkem jste vložili: {suma} Kč")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Nápoj se připravuje")
        if refund > 0:
            print(f"Zde jsou peníze zpět: {refund} Kč")
    else:
        print(f"Nevhodili jste dostatek peněz. Ještě je zapotřebí vložit {price - user_sum_coins} Kč")
    
def fill_in_ingredients():
    return resources
   
   
def consumption_ingredients(name_of_drink, ingredients):
        rest_of_ingredience["water"] = ingredients["water"] - MENU [name_of_drink] ["ingredients"]["water"]
        rest_of_ingredience["milk"] = ingredients["milk"] - MENU [name_of_drink] ["ingredients"]["milk"]
        rest_of_ingredience["coffee"] = ingredients["coffee"] - MENU [name_of_drink] ["ingredients"]["coffee"]
        print(f"Zbylé ingredience:{rest_of_ingredience}")
def calculate_ingredients(drink_name):
    if drink_name == "espresso":
        consumption_ingredients(drink_name, rest_of_ingredience)
    elif drink_name == "latte":
        consumption_ingredients(drink_name, rest_of_ingredience)
    elif drink_name == "cappuccino":
      consumption_ingredients(drink_name, rest_of_ingredience)
        
def ingredients_check(in_water, in_milk, in_coffee):
    if in_water < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj.")
        return False
    elif in_milk < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj.")
        return False
    elif in_coffee < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj.")
        return False
    else:
        print("Na váš nápoj máme dostatek ingrediencí")
        return True
#Kód automatu

#původní množství ingrediencí
rest_of_ingredience = fill_in_ingredients()

let_continue = True
while(let_continue):
    #volba uživatele - jaký chce nápoj
    user_choice = input("Co byste si dal/a? (espresso/latte/cappuccino): ")

    #vypočítá kolik zbývá ingrediencí
    calculate_ingredients(user_choice)
    
     #kontrola, zda máme dostatek ingrediencí
    if user_choice != "report":
        let_continue = ingredients_check(rest_of_ingredience["water"], rest_of_ingredience["milk"], rest_of_ingredience["coffee"])
        
    #Má kód dále pokračovat
    if let_continue == False:
        break
    #kontrolní report
    if user_choice == "report":
        report(rest_of_ingredience)
   
    #Nápoje - cena   
    if user_choice == "espresso":
        sum = coins()
        print(f"Cena espressa je: {espresso_price} Kč.")
        calculate_change(sum, espresso_price)
    elif user_choice == "latte":
        sum = coins()
        print(f"Cena espressa je: {latte_price} Kč.")
        calculate_change(sum, latte_price)
    elif user_choice == "capuccino":
        sum = coins ()
        print(f"Cena espressa je: {cappuccino_price} Kč.")
        calculate_change(sum, cappuccino_price)