# Bidding In an Auction

bids = {}

# Adding name and bid into dictionary

is_bidding = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} which is at ${highest_bid}")


while is_bidding:
    username = input("What is your name?\t")
    price = int(input("What's your bid? $"))
    bids[username] = price

    questionnaire = input("Are there any bidders? Type 'yes or 'no'\t")
    if questionnaire == 'no':
        is_bidding = False
        find_highest_bidder(bids)