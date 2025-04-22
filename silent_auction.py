print("Weclome to the secret auction!")


bids = {}
bidders = True


def place_bid():
    name = input("What's your name? ")
    bid = int(input("Place your bid: $ "))
    bids[name] = bid



def find_highest_bidder():

    greatest_bid = 0
    for bid in bids:
        if (bids[bid] > greatest_bid):
            greatest_bid = bids[bid]

    print(f"The greatest bid is {bid}'s at $ {greatest_bid}")

while (bidders):
    place_bid()

    more_bidders = input("Anyone else wants to bid? Y/N ")
    if (more_bidders == 'N'):
        bidders = False
        find_highest_bidder()
    else:
        continue
