from sympy import list2numpy


def list_max(input_list):  # input_list ist ein erstellter input parameter, der name frei wählbar
    max_value = input_list[0]  # der paramenter existiert nur innerhalb dieser funktion

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    print(max_value)


list1 = [-2, 1, 2, -10, 22, -10]
list_max(list1)
list2 = [-20, 123, 112, -10, 22, -120]
list_max(list2)
