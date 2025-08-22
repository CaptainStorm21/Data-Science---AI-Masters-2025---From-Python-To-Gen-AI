from datetime import datetime
# Define the file name where data will be saved
text_file = "docs/flora_fauna.txt"

# Reading the file
# R = read
# W = write
# E = Execute
file = open(text_file, 'r')

# for line in file:
#     print(line)
    
# Read a file
print(file.read())

# Read specific # of characters
file = open(text_file, 'r')
print(file.read(10))

# Read specific line
file = open(text_file, 'r')
# will print only 20 character from 1st line
print(file.readline(20))
# will print only lines 3 to 5
print(file.readlines(3-5))

# Write to the file 
file = open(text_file, 'w')
file.write ('The wind howled across the deck, tugging at the sails as the ship cut through the darkened waves.')
file = open(text_file, 'r')
print(file.read())

# Open the file in read mode to read existing content
with open(text_file, 'r') as file:
    existing_content = file.read()

# New paragraphs to be added
top_paragraph = 'The wind howled across the deck, tugging at the sails as the ship cut through the darkened waves.'
bottom_paragraph = 'The crew, worn and weary, braced themselves as the storm’s fury threatened to tear the sails apart.'

# Open the file in write mode to overwrite with new content, including top and bottom paragraphs
with open(text_file, 'w') as file:
    file.write(top_paragraph + '\n')  # Write new paragraph at the top
    file.write(existing_content)      # Write the existing content in the middle
    file.write('\n' + bottom_paragraph)  # Append new paragraph at the bottom

# Check the result
with open(text_file, 'r') as file:
    print(file.read())
    
# Append operation 
file = open(text_file, 'a')
file.write ('The darkened waves slammed the shores')
file = open(text_file, 'r')
print(file.read())