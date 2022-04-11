list_a = [i for i in range(10)]

print(list_a)

list_b = [list_a[i] for i in range(3)]  # list comp erst lstb mit 1. 3 val aus lsta

# List Slicing
# start, stop, step
list_c = list_a[0:3:1]
print(list_c)
# das list slicing gibt einen gewünschten teil der liste als neue liste aus
