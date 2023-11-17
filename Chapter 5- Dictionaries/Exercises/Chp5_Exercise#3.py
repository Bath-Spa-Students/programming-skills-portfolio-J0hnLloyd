#Glossary...
Programming_words = {'String': 'Stores Text & Characters',
    'Variable': 'Containers of Data Values',
    'Comment': 'Uses the Character # to comment',
    'Lists': 'Uses brackets to create lists', 
    'Else & if statements': 'Run only when a certain condition is met.',
    'float': 'Numbers with decimal values',
    'Integers': 'Numerical Values either Negative or Positive',
    'Dictionary': 'Stores paired key values',
    'Key': 'Analogues or Indexes of a list',
    'Tuple': 'An immutable ordered sequence of items',}

for word, definition in Programming_words.items():
    print("\n" + word.title() + ": " + definition)
             