import numpy as np  # "as np" - as definiert ein alias, hier np für numpy. danach kann man immer np

# statt numpy schreiben
# numpy bietet eine menge an vorgefertigten funktionen
list1 = np.array([-2, 1, 2, -10, 22, -10])
print(np.max(list1))
print(np.min(list1))

list2 = np.array([-20, 123, 112, -10, 22, -120])
print(np.(list2))
print(np.min(list2))

# durch das np.array() wird die liste "schneller" wegen der C implementierung

# numpy.org doku anschauen was es alle in der numpy bibliothek / library gibt'

print(np.mean(list1))
print(np.mean(list2))

print(np.median(list1))
print(np.median(list2))
