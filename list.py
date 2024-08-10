#employees = ["Lucy", "Harry", "Ron"]
#print(employees[0])
#print(employees[1])

#mění položku
#employees[1] = "Hermiona"
#print(employees)

#přidáváme obsah
#employees.append("Harry")
#print(employees)

#přidat více položek
#employees.extend(["Crabbe, Goyle"])
#print(employees)

#odstranit
#employees.remove("Ron")
#print(employees)

#indexerror
#gryffindor = ["Ron", "Harry", "Hermione"]
#slytherin = ["Lucy", "Draco", "Tom"]

#number = len(gryffindor)
#print(gryffindor[number])

#nested list
#students = [gryffindor, slytherin]
#print(students[0][1])

set1 = ["😺", "😼", "😾"]
set2 = ["😺", "😼", "😾"]
set3 = ["😺", "😼", "😾"]
all_sets = [set1, set2, set3]
print(f"{set1}\n{set2}\n{set3}")
position = input("Zadejte souřadnice ")

num1 = int(position[0])
num2 = int(position[1])

all_sets[num1][num2] = "X"
print(f"{set1}\n{set2}\n{set3}")