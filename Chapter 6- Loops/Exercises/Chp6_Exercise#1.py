# Messages & User Input...
PapaJohns = "\nWhat Pizza toppings would you like on your Pizza?"
PapaJohns += "\n Input 'quit' when finished: "

# Loop...
while True:
    Toppings = input(PapaJohns)
    if Toppings != 'quit':
        print("\n I'll add " + Toppings + " to your pizza.") # Print the message...
    else:
        break
