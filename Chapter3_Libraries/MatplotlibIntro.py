import matplotlib.pyplot as plt


grades_jan = [56, 64, 78, 100]
grades_ben = [86, 94, 98, 90]

# plot
plt.plot(range(len(grades_jan)), grades_jan, color="blue")  # plot verbindet die punkte, range ist der bereich
plt.plot(range(len(grades_ben)), grades_ben, color="red")
# der abgebildet werden soll, len und liste der bereich, color farbe im graph
plt.legend(["Jan", "Ben"])  # fügt Legende hinzu, dafür eine liste schreiben oder verknüpfen, bzw frei
# gewählt
plt.xlabel("course")  # beschriftung der x achse
plt.ylabel("Grade in %")  # beschriftung der y achse
plt.title("Jan vs Ben")  # überschrift der grafik
plt.show()  # zeigt die grafik an

# scatter , graph ohne verdundene punkte (nur punkte)
plt.scatter(range(len(grades_jan)), grades_jan, color="blue")
plt.scatter(range(len(grades_ben)), grades_ben, color="red")
plt.legend(["Jan", "Ben"])
plt.xlabel("course")
plt.ylabel("Grade in %")
plt.title("Jan vs Ben")
plt.show()
