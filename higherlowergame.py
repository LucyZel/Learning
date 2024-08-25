from lowerhighergamedata import data
import random

def account_generator(all_accounts):
    data_lenght = len(data)
    random_number = random.randint(0, data_lenght - 1)
    return all_accounts[random_number]


def printing_options(acc1, acc2):
    print(f"Porovnejte A: {acc1['name']}, {acc1['description']}, {acc1['country']}")
    print(f"Porovnejte B: {acc2['name']}, {acc2['description']}, {acc2['country']}")
   

def game ():
    account_1 = account_generator(data)
    account_2 = account_generator(data)
    if account_1 != account_2:
        right_answer = ""
        score = 0
        lets_continue = True

        while lets_continue:
            # #testování
            # print(f"Testovácí výpis - účet je {account_1 ['follower_count']}")
            # print(f"Testovácí výpis - účet je {account_2 ['follower_count']}")
            printing_options(account_1, account_2)
            user_answer = input("Kdo má více sledujících na instagramu? Napište A nebo B. ")

            if account_1["follower_count"] > account_2["follower_count"]:
                right_answer = "A"
                account1 = account_2
            else:
                right_answer = "B"
                account1 = account_2
            
            if right_answer == user_answer:
                score += 1
                print(f"Uhádli jste. Vaše skóre je {score}")
                account_2 = account_generator(data)
            else:
                print(f"To je špatně. Vaše konečné skóre je {score}")
                lets_continue = False

game()
