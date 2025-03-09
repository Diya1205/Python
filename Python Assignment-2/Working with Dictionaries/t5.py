text = "hello world"

# Dictionary to store character counts
char_count = {}

# Counting occurrences of each character
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Frequency:", char_count)
