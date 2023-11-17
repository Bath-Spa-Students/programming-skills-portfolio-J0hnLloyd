# List of Three Ordered sandwiches...
sandwich_orders = ["Pastrami", "ChikaChicken", "Pastrami", 
                   "TaraTurkey", "Ham and Cheese" "Pastrami",]

# Empty list for finished sandwiches...
finished_sandwiches = []

# No Pastrami Message & Removal of Pastrami in the List... (Loop)
print("We've ran out of Pastrami today, apologies.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Print new/current list [Pastrami removed from list]... (Loop)
print("\n")
while sandwich_orders:
    newlist = sandwich_orders.pop()
    print(newlist + " Sandwich queued...")
    finished_sandwiches.append(newlist)

# Print Finished Sandwiches... 
print("\n")
for sandwich in finished_sandwiches:
    print(sandwich + " is Finished.")
