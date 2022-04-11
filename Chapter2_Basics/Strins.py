name = "Jan Schaffranek"


result = name.find("Peter")

if result == -1:
    print("not found")
else:
    print("found at index: ", result)

name2 = name.replace("Jan", "Yann")
print(name2)

name3 = name.upper()
print(name3)

name4 = name.lower()
print(name4)

name5 = name.split(" ")
print(name5)

name6 = name.count("an")
print(name6)
