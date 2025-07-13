import re

text = "Python is powerful"
pattern = "Python"

# Match the word at the beginning of the string
match = re.match(pattern, text)

if match:
    print("Match found at the beginning")
else:
    print("No match at the beginning")
