try:
    file = open("test.txt", "r")
    print(file.read())
except Exception as e:
    print("Error:", e)
finally:
    file.close()
    print("File closed.")
