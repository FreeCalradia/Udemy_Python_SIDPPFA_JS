# == (Equal) Gleichheitsvergleich (ein = Zeichen in Programmiersprachen immer Wertezuweisung)
# < (Less than) kleiner als
# > (Greater than) größer als
# != (Not Equal) nicht gleich
# <= (Less or equal than) Kleiner/Gleich
# >= (Greater or equal than) Größer/Gleich

i_am_broke = True

if i_am_broke:
    print("I am broke.")
else:
    print("I am not broke.")

my_bank_account = 1000

if my_bank_account <= 0:
    print("I am broke.")
else:
    print("I am not broke.")

my_age = 36

if my_age < 18:
    print("You are a child.")
elif my_age < 66:
    print("You are an adult.")
else:
    print("You are a pensioner.")
