input_filepath = "C:/Users/benut/Desktop/Kursmaterialien Schnelleinstieg in die Python Programmierung für Anfänger/UdemyPythonIntro_Template-master/Chapter4_Intermediate/test.py"
output_filepath = "C:/Users/benut/Desktop/Kursmaterialien Schnelleinstieg in die Python Programmierung für Anfänger/UdemyPythonIntro_Template-master/Chapter4_Intermediate/test2.py"


with open(input_filepath, "r") as f:
    content = f.readlines()


print(content)
print("")
content.append("Lieschen Ro\n")


with open(output_filepath, "w") as f:
    f.writelines(content)
