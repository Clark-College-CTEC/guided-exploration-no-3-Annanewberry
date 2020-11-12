# Guided Exploration No. 3
# Annalise Newberry

# Import the Python random library
import random
# Create an empty list that will store the rap names
possible_names = []
# Open a new file called rap-names-output.txt for write
outputFile = open('rap-names-output.txt', 'w')
# Open the rap-names.txt for read and assign a "handle” to the file “dataFile”
with open('rap-names.txt', 'r') as dataFile:
    # Loops through the names in the file
    for name in dataFile:
        # Append names to the possible_names list and strip the line feed from each line
        possible_names.append(name.rstrip())
# Get the number of rap names to create from the user
count = int(input('How many rap names would you like to create? '))
# Ask the user how many parts the names should have
parts = int(input('How many parts should the name contain? '))
# Use a counted loop to create the number of rap names the user wants
for i in range(count):
    # Create a new list that will hold the rap name parts
    name_parts = []
    # Create a counted loop that will loop for the number of parts that the user wants in the names
    for j in range(parts):
        # Randomly select a name from the possible_names list and append it to the name_parts list
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])
        # Write the names to the rap-names-output.txt file and take the name_parts list items and join them together with a space between
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Print the names out
    print(f"{' '.join(name_parts)}")
# Close the output file
outputFile.close()
