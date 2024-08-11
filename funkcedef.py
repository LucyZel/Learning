#předpřipravené funkce
#def my_function():
   #if 5 == 5:
       #print("Je to číslo pět")
   #else:
       #print("není to číslo pět")
    
#my_function()

#funkce s parametrem
#def greet():
    #print("Ahoj")
    #print("Já jsem Lucy")
    #print("Na shledanou")
    
#def greet_name(name): #name - proměnná - parametr
    #print(f"Ahoj, já jsem {name}")
    
#greet_name("Lucy") #argument
#greet_name("Harry")

#funkce s více parametry
#def greet(name, location):
    #print(f"Ahoj, já jsem {name} a pocházím z města {location}")

#positional arguments    
#greet("Lucy", "Praha") #záleží na pořadí

#keyword argument
#greet(name="Lucy", location="Praha") #nezáleží na pořadí

#kalkulátor natírací plochy
#1 plechovka barvy pokryje 5m2 - zaokrouhlit nahoru

#import math

#wall_1=int(input("Výška zdi: "))
#wall_2=int(input("Šířka zdi: "))

#coverage = 5

#def paint_calculator(width, height, cover):
    #wall_total=width*height
    #paint_total=math.ceil (wall_total/coverage)
    #print(f"Budete potřebovat {paint_total} plechovek barvy.")
    
#paint_calculator(width=wall_2, height=wall_1, cover=coverage)
    
#prvočíslo - procvičování
#dělitelná bezezbytku 1 a samosebou

n=int(input("Zadejte prosím číslo: "))

def prime_number(number):
    result = "Je to prvočíslo"
    for one_number in range (2, number):#rozsah se bere podle toho, kolik někdo zadá (13 - 12)
        if number % one_number == 0: #== 0: bezezbytku
            result = "Není to prvočíslo."
    print(result)
    
prime_number(n)
