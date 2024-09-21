print('''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                       .-------------.
                   jgs/_______________\ ''')
import os
print("--- BLIND AUCTION ---")
list_buyers = []
buyers_names = []
buyers_bids = []
while(True):
    index =0
    print("Welcome to the secret auction event..")
    name = input("What is your name? Ans: ")
    bid = int(input("What is your bid? Ans: "))

    buyers_names.append( name)
    buyers_bids.append( bid)

    other_bid = input("Are there any other biders(yes or no)? Ans: ").lower()
    if other_bid == "yes":
        index+=1
        os.system('cls')#this clears the terminal

    else:# finding the highest bidder
        
        # print(buyers_bids)
        # print(buyers_names)
        name_index = 0
        max_bid =0
        for key in buyers_bids:
            if max_bid < key:
                max_bid = key
        for x in buyers_bids:
            name_index+=1
            if max_bid == x:
                break
        # print(max_bid)
        # print(name_index)

        find_name=0
        for n_key in buyers_names:
            find_name+=1
            if find_name == name_index:
                print(f"Winner with highest bid of {max_bid}$ is {n_key}")
        break