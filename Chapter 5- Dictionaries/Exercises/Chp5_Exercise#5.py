# Empty List...
Pets = []

# Dictionaries of Pet Infos...
PetInfo = {'Animal': 'Cat',
    'Owner': 'John Lloyd',
    'Pet Name': 'Aslan',}

Pets.append(PetInfo)

PetInfo = {'Animal': 'Dog',
    'Owner': 'Joselle',
    'Pet Name': 'Astra',}

Pets.append(PetInfo)

PetInfo = {'Animal': 'Rat',
    'Owner': 'Linguini',
    'Pet Name': 'Remmy',}

Pets.append(PetInfo)

# Runnign/Executing the program...
for PetInfo in Pets:
    print ("\n Info of " + PetInfo['Pet Name'].title() + ":\n")
    for key, value in PetInfo.items():
        print("\t" + key + ": " + str(value))