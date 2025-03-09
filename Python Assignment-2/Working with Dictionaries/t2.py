# Two lists
keys = ["name", "age", "city"]
values = ["Diya", 20, "Ahmedabad"]

# Merging into a dictionary using a loop
merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged Dictionary:", merged_dict)
