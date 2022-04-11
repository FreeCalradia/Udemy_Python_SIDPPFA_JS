grade_ben = 1
grade_jan = 2
grade_peter = 1

grades = [1, 2, 1]

grade_melissa = 4
print(grades)

grades.append(4)  # hinzufügen eines wertes in eine Liste
print(grades)

grades.pop()  # entfernen des letzten Wertes einer Liste, über Indexzahl auch andere Werte/Values löschbar
print(grades)

print("Ben's grade: ", grades[0])  # 0 ist die Stelle des Index an der die Note von Ben in der Liste steht
print("Jan's grade: ", grades[1])
print("Peter's grade: ", grades[2])

grades[0] = 3  # 0 wieder Stelle des Index
print(grades)

grades.pop(1)  # 1 ist wieder die Indexzahl
print(grades)
