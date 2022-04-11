students = {"Ben": 1, "Jan": 2, "Peter": 1, "Melissa": 4}  # Key ist Links, der Wert Rechts vom Doppelpunkt
print(students)

# read element
student1 = students["Ben"]
print(student1)

# write element
students["Ben"] = 6  # Faustregel, links vom = Zeichen ist Wert schreiben, rechts ist Wert lesen
print(students)

# add element (nicht formal richtig)
students["Julia"] = 1
# Wenn es den Wert den man verändern möchte in dem Dict noch nicht gibt, wird er mit dem Key hinzugefügt
print(students)

# remove element
students.pop("Julia")
print(students)

# über dictionaries iterieren
# keys
for student_name in students:
    print(student_name)

# values
for student_grade in students.values():
    print(student_grade)

# keys und values
for key, value in students.items():  # muss nicht key und value heißen
    print(key, value)
