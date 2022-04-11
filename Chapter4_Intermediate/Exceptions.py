d = {"Jan": 27, "Peter": 33}
l = [1, 2, 3]


try:
    print("Yann")
except:
    print("Yann key does not exist")


try:
    print(l[3])
except KeyError as e:
    print(e)  # e ist die Fehlermeldung error
except IndexError as e:
    print(e)
