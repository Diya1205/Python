import re

text = "Welcome to Python programming"
pattern = "Python"

# Search for the word in the string
match = re.search(pattern, text)

if match:
    print("Word found at position:", match.start())
else:
    print("Word not found")
