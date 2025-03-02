from art import logo

print(logo)


continue_bidding = True

bid_list = {}

def determine_highest_bidder(bidding_list):
    highest_bidder = ""
    highest_bid_value = 0
    for bidder in bidding_list:
        if bidding_list[bidder] > highest_bid_value:
            highest_bidder = bidder
            highest_bid_value = bidding_list[bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid_value}")

while continue_bidding:
    name = input("What's your name?:")
    bid = int(input("What's your bid?: $"))
    bid_list[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_bid.lower() == 'yes':
        print("\n" * 20)
        continue_bidding = True
    else:
        print("\n" * 20)
        determine_highest_bidder(bid_list)
        continue_bidding = False



