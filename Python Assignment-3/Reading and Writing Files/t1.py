#write method
file = open("C:\\Users\\Diya Patil\\Desktop\\python\\core python\\6-1-25\\test.txt","w")
file.write("hello this write method ")
file.close

#read method
file = open("C:\\Users\\Diya Patil\\Desktop\\python\\core python\\6-1-25\\test.txt","r")
print(file.readline())
print(file.read())
file.close()