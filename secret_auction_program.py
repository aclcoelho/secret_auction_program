import os
from art import logo

print(logo)
bids = {}
answer = "yes"

while answer == "yes":
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid 
  answer = (input("Are there any other bidders? Type 'yes' or 'no'. ")).lower()
  os.system("clear")
else:
  print(bids)
  max_bid = max(bids.values())
  max_key = max(bids, key=bids.get)
  print(f"The winner is {max_key} with a bid of ${max_bid}")
