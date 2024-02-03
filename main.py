import os
import time
import art


print(art.logo)
stock_biders=[]

other_biders=True
while other_biders:
    name=input("What is your name please ?  ")
    money=float(input("What is your bide ?  "))
    bider_dict={"name":name, "bid":money}
    stock_biders.append(bider_dict)
    should_continue=input ("Are there other bidder ? Type \"yes\" or \"no\" . ")
    if should_continue=='no':
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
        other_biders=False
        high_bid=0
        for bider in stock_biders:
            if bider["bid"] > high_bid:
                high_bid=bider["bid"]
                position=stock_biders.index(bider)
        print(f"The winner is {stock_biders[position]["name"]} with a bid of {stock_biders[position]["bid"]} dollar\n\n\n")
    else :
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
    