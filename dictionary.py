# #key - value aka slovník a překlad

# it_dictionary = {
#     "String": "Text",
#     "Integer": "Celé číslo",
#     "Float": "Desetinné číslo",
#     "Boolean": "Pravda nepravda"
# }

# # print(it_dictionary["String"])
# # print(it_dictionary["Integer"])

# #zde nezáleží na pořadí

# it_dictionary_2 = {
#     0: "Celé číslo",
#     1: "Text",
#     2: "Desetinné číslo",
#     3: "Pravda nepravda"
# }
# print(it_dictionary_2)
# # print(it_dictionary_2[0])
# # print(it_dictionary_2[0])
# # print(it_dictionary_2[0])
# # print(it_dictionary_2[0])

# # print(it_dictionary_2[0])
# # print(it_dictionary_2[0])
# # print(it_dictionary_2[2])
# # print(it_dictionary_2[1])

# #přidání hotnod do dictionary
# it_dictionary_2[4] = "Uložení více hodnot"
# print(it_dictionary_2)

# #nastavení prázdného dictionary
# empty_dictiornary = {}

# #vyprázdnit dictionary
# #it_dictionary_2 = {}

# #měníme hodnoty v dictionary
# it_dictionary_2[1] = "Testová hodnota" #nejedná se o indexy!!
# print(it_dictionary_2)

# #dictionary cyklus
# it_dictionary = {
#     "Integer": "Celé číslo",
#     "String": "Text",
#     "Float": "Desetinné číslo",
#     "Boolean": "Pravda nepravda"
# }

# for key in it_dictionary:
#     # print(key)
#     print(it_dictionary[key])

students_results = {
    "Harry": 85,
    "Ron": 71,
    "Hermione": 98,
    "Draco": 69
}

# stupnice
# 91 až  100 = "Excelentní"
# 81 až 90 = "Vynikající"
# 71 až 80 = "Splněno"
# méně jak 71 = "Nespleněno"

final_score = {}

for key in students_results:
    score = students_results[key] #první slovo aka key v dictionary students_results
    if score > 90:
        final_score[key] = "Excelentní" 
    elif score > 80:
        final_score[key] = "Vynikající"
    elif score >70:
        final_score[key] = "Splněno"
    else:
        final_score[key] = "Nesplněno"
    
print(final_score)
