class Animal:
    def __init__(self):
        self.Name = Name
        self.Lastname = Lastname
        self.Age = Age
        self.ID = ID

    def jump(self):
        print("Jump!")


def main():
    dog = Animal(35, 0.55)
    print(dog.weight)
    print(dog.height)
    dog.jump()

    cat = Animal(3, 0.3)
    print(cat.weight)
    print(cat.height)
    cat.jump()


if __name__ == "__main__":
    main()
