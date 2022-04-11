list_a = [1, 2, 3]

list_a.append(4)

print(list_a)

# Tuple

tuple_a = (1, 2, 3)  # Tuple hat runde klammern - formal. kann aber auch 1, 2, 3
# aussehen, man erkennt tuples daran, dass werte durch ein komma ausgezählt sind
tuple_b = (1, True, "hello")  # ein tuple kann gemischte datentypen beinhalten
tuple_a.count(2)  # count und index sind eigentlich erstmal alle wichtigen
tuple_a.index(2)  # tuple funktionen !
# die länge eines erstellten tuples steht fest

# tuple empfehlen sich bei festen anzahlen von werten, zb bei der
# definition von einem quader , aber listen haben mehr usecases

print(tuple_a.count(1))
