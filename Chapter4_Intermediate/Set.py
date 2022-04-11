# Set ,auf Deutsch: (mathematisches Konstrukt einer) Menge
# in einem Set sind die Elemente einzigartig
# usecases vom set sind vergleiche von mengen

l1 = ("a", "b", "a", "c")
print(l1)

s1 = set(l1)  # man kann statt einer liste auch andere interierbare objekte übergeben
# zb tuples oder arrays
print(s1)

s2 = set(("a", "d"))
print(s2)
# sets werden durcheinander ausgegeben (wie sie aus dem hash gelesen werden,
# also nichtmal in der reihenfolge in der über sie iteriert wurde)

# Intersection = Schnittmenge
# a
# Union = beide Mengen zusammen (merged)
# abcd
# Difference = Unterschied
# bc
print("")
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
