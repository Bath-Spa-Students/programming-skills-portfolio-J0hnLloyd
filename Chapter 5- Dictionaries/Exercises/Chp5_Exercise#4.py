# Glossary...
rivers = {
    'Nile': 'Egypt',
    'Colorado River': 'Mexico',
    'Amazon River' : 'Brazil & Pero',
    'Mississippi': 'United States',
    }

for river, country in rivers.items():
    print("The " + river.title() + " Flows through " + country.title() + ".")

print("\Included Rivers:")
for river in rivers.keys():
    print("- " + river.title())

print("\nCountries included:")
for country in rivers.values():
    print("- " + country.title())