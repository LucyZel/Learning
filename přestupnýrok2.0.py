def cycle(users_year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days(users_year, users_months):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cycle_result = cycle(users_year)
    if cycle_result and users_months == 2:
        return 29
    else:
        return days_in_month [users_months -1]
    
year = int(input("Zadejte rok, který chcete zkontrolovat "))
month = int(input("Zadejte měsíc "))

result = days(year, month)

print(f"Počet dní ve zvoleném měsíci je {result}")