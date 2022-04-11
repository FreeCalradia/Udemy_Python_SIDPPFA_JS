list_a = [100, 200, -10]  # in dem beispiel kontostände von 3 personen
list_b = [False, False, True]  # idB Bool ob die Person pleite ist

for idx in range(len(list_a)):  # for index im bereich länge der liste_a
    print(idx, list_a[idx], list_b[idx])  # gebe aus(indexzahl, list_a anstelle von index), "b

print("")

for val_a, val_b in zip(list_a, list_b):  # zip = reissverschlussverfahren indexweise, 0vona, 0vonb, 1vona usw
    # gibt je iteration 2 werte aus (als tuple, returned tuples). bei drei listen 3 werte usw
    print(val_a, val_b)

print("")

# zip, values for multiple iterables
# funktion wird benutzt wenn man mehr als eine liste gleichzeitig übergeben will, denn zb
for val in list_a:
    print(val)
# funktioniert nur mit einer liste
# mit zip kann man nicht nur listen verarbeiten, sondern alle iterables zb dicts, tuples usw
print("")

# Enumerate, index und value

for idx, val in enumerate(list_a):
    print(idx, val)

print("")

# kombination von zip und enumerate
# index and values for  multiple iterables

for idx, (val_a, val_b) in enumerate(zip(list_a, list_b)):
    print(val_a, val_b)

# das zip muss dann aber die innere funktion sein
# die zip wird an enumerate übergeben
