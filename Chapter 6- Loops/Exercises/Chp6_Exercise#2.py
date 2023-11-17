# Messages & User Input... 
Cue = "How old are you?"
Cue += "\n Input 'quit' when finished: "

# Loop
while True:
    age = input(Cue)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in for free.")
    elif age < 13:
        print("  Your ticket price is $10.")
    else:
        print("  Your ticket price is $15.")