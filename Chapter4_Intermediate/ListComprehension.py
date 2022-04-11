# List Comprehension, list comp
# Liste einfacher und besser lesbar mit Werten initialisierbar

list_a = []  # wenn in der list zb 100 mal die 5 stehen soll, entweder einzeln eingeben
# oder besser
# for i in range (100):
#   list_a.append(5)
# aber noch besser mit list comprehension

list_b = [5 for i in range(100)]
# list comp im gegensatz zur for funktion rückwärts
# man kann alles machen, was man auch in einer for schleife schreiben kann
# effizeinter als  for schleife weil speicher vorher belegt wird usw

list_c = [i ** 2 for i in range(100)]
print(list_c)
