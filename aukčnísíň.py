from auctionLogo import auction_logo
import os

print(auction_logo)

print("Vítejte v programu pro tichou dražbu.")

bidders = {}

lets_continue = "ano"

while lets_continue == "ano":
    name = input("Jaké je vaše jméno? ")
    offer = int(input("Jaká je vaše nabídka v dolarech? "))
    lets_continue = input("Jsou další nabízející? Napište 'ano' nebo 'ne'. ")
    bidders[name] = offer
    
    if lets_continue == "ne":
         os.system("clear")
         
#kdo má nejvyšší nabídku

def highest_offer(bidders_dictionary):
    highest_offer = 0
    winner = ""
    for key in bidders_dictionary:
        if bidders_dictionary[key] > highest_offer:
            highest_offer = bidders_dictionary[key]
            winner = key
    return winner, highest_offer
    
winner, highest_offer = highest_offer(bidders)
            
print(f"Vítezem silent auction je {winner} s nabídkou {highest_offer} dolarů.")