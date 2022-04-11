grades = [1, 2, 1, 4]

for grade in grades:
    print(grade)

print("")

for idx in range(len(grades)):
    print(grades[idx])  # idx oder i steht für Index

# range Funktin kann bis zu drei Werte entgegen nehmen
# start, stop und step Wert
for idx in range(0, 10, 1):  # fangen bei 0 an, gehen bis 10 und erhöhen in jeder Iteration (Durchgang) um 1
    print(idx)

# stop Wert  zB 10 Bedeutet nicht bis 10, sondern die Zahl vor der gestoppt wird
# For Schleife führt Code mehrmals aus. Das nach dem for definiert wie oft.
