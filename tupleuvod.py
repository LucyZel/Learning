my_tuple = (1, 5, 8)
print (my_tuple[0])
print (my_tuple[1])
print (my_tuple[2])

#vyhodí chybu
#my_tuple[0] = 12

#tuple změníme na list
tuple_to_list = list(my_tuple)
print(tuple_to_list)
tuple_to_list[0] = 12
print(tuple_to_list)
