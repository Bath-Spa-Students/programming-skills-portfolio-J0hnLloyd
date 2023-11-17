# List of Three Ordered sandwiches...
sandwich_orders = ["ChikaChicken", "TaraTurkey", "Ham and Cheese"]

# Empty list for finished sandwiches...
finished_sandwiches = []

# Loop...
while sandwich_orders:
    current_order = sandwich_orders.pop(0) 
    print(f"I made your {current_order} Sandwich.")
    finished_sandwiches.append(current_order)

# Print the Finished Sandwiches
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())