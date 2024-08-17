# student1 = "Harry"

# #lokální scope - v definici
# def test():
#     student1 = "Lucy"
#     print(student1)
#     return student1
    
# result = test()
# print(result) #print(student1)  bez return - globální scope viz řádek 1


#block scope

number1 = 5

#def create_number():
if number1 < 10:
    new_number = 30
    
print(new_number)