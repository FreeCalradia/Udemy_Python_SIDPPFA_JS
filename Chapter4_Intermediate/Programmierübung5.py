"""Exercise 1:
1.)
Write a class Student that has the following member variables:
- Name (String)
- Lastname (String)
- Age (Integer)
- Id (Integer)
2.)
Write a method that print the information about the student.
E.g. for Student('Jan', 'Schaffranek', 27, 1080133228459) it will print:
'Jan Schaffranek is 27 years old and has the id 1080133228459'
"""


class Student:
    def __init__(self, Name, Lastname, Age, ID):
        self.Name = Name
        self.Lastname = Lastname
        self.Age = Age
        self.ID = ID

    def print_student(self):
        print(f"{self.Name} {self.Lastname} is {self.Age} years old and has the id {self.ID}")


def main():
    oskar = Student("Oskar", "Oskarson", 72, 9548223310801)
    oskar.print_student()
    jan = Student("Jan", "Schaffranek", 27, 1080133228459)
    jan.print_student()


if __name__ == "__main__":
    main()
