def test(
    param1, param2="hello", param3="byebye"
):  # wenn man neben dem default weitere parameter angeben will MÜSSEN diese vor dem default genannt werden
    print("Test function:", param1, " - ", param2, " - ", param3)


test("hello", param2="byebye", param3="end")
# der defaultwert, hier hello, wird nur ausgegeben, wenn für den parameter kein argument übergeben worden ist
# die argumente werden in der reihenfolge den parametern zugewiesen, da param2
# hier der default ist, verknüpft sich byebye mit param1
# 1. wenn default parameter alle mit default am ende
# 2. wenn mit keyword arguments angefangen dann muss es beibehalten werden


def list_max(input_list):  # input_list ist ein erstellter input parameter, der name frei wählbar
    max_value = input_list[0]  # der paramenter existiert nur innerhalb dieser funktion

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    return max_value  # return gibt den wert der funtkion zurück an die zeile, die die funktion aufgerufen hat.
    # in diesem beispiel zeile 27


list1 = [-2, 1, 2, -10, 22, -10]
list1_max = list_max(list1)
print(list1_max)
