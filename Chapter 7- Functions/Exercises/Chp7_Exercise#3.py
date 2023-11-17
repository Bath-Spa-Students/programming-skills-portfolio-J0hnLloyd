# Use def to define make_shirt... 
def make_shirt(size, message):
    print(f"Making a {size}-sized shirt with a message on the front that displays: '{message}'.")

# Call the function...
print("\n")
make_shirt("Medium", "print (NICE_SHIRT!)")
# Call the function using keyword arguments...
print("\n")
make_shirt(size="Large", message="I really love cheese they're just too good like too GOOOoooooood")
print("\n")
make_shirt(size="Small", message="I Hate cheese, it gets everywhere >:(")