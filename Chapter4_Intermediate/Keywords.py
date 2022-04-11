# break, continue, pass, none

l1 = [1, 2, 3, 4, 5]

for val in l1:
    if val > 3:
        break # beendet die funktion wenn erfüllt
    print(val)

print("")

for val in l1:
    if val % 2 == 0:
        continue # beendet den aktuellen durchlauf der funktion
    print(val)


def print_list(l1):
    pass # interpreter überspringt


print_val = none # platzhalter für variabeln
