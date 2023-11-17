# Use def to define make_shirt but default Large size messages "Ï LoVE PytHOn"... 
def make_shirt(size='Large' , message='I LOVE PYTHON'):
    print(f"Making a {size}-sized shirt with a message on the front that displays: '{message}'.")

# Call the function...
print("\n")
make_shirt(size='Large')
# Call the function using keyword arguments...
print("\n")
make_shirt(size="Medium", message="I Love Python")
print("\n")
make_shirt(size="Small", message="Not a Large or Medium T-Shirt... :(")