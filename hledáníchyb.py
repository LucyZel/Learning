#debuggingj

# Popiš problém
# def test_function():
#     for number in range(1, 11): #byla tam 10
#         # print(number) - důležité často kód testovat!!
#         if number == 10:
#          print("Vše je správně")
# test_function()

# # # Občas funguje a občas ne
# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
# # dice_number = 1
# dice_number = random.randint(0, 5)  - bylo zde 1, 6
# print(all_dice_numbers[dice_number])

# # Mysli jako počítač
# year = int(input("Jaký je váš rok narození? "))
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
# elif year >= 1994: bylo pouze >
#   print("Jste generace Z. ")
  
  
# Oprav hned chyby
# age = int(input("Kolik je vám let?")) - bez int
# if age > 18:
#     print(f"Ve věku {age} můžete kupovat alkohol.") špatné odsazení, chybělo f

