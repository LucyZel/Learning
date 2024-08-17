#něco v něčem

# cities = {
#     "Spain": "Madrid",
#     "France": "Paris"
    
# }

# print(cities["Spain"])

# list v dictionary
# travel_diary = {
#     "Spain": ["Madrid", "Leon", "Valencia"],
#     "France": ["Paris", "Nice", "Rennes"]
# }

# print(travel_diary["France"][0])

#dictionary v dictionary
# travel_diary = {
#     "Spain": {"visted_cities": ["Madrid", "Leon", "Valencia"], "visits": 5},
#     "France": {"visited_cities": ["Paris", "Nice", "Rennes"], "visits": 3}
# }
# print(travel_diary["France"]["visited_cities"][1])

#dictionary v listu

travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    },
]

def new_country (country_name, country_cities, number_of_visits):
    new_diary = {}
    new_diary ["country"] = country_name
    new_diary ["visited_cities"] = country_cities
    new_diary ["visits"] = number_of_visits
    travel_diary.append(new_diary)
    
new_country("Italy", ["Bergamo", "Milano", "Venice"],8)
    
print(travel_diary)
print(travel_diary[2]["visits"])
    