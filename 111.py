class Person:
    def __init__(self, fn, ln, city):
        self.firstname = fn
        self.lastname = ln
        self.city = city

    def talk(self):
        print(f"Hello my name is {self.firstname} {self.lastname} and I live in {self.city}")


pedram = Person("Pedram", "Azizi", "Yazd")
arshia = Person("Arshia", "Yar Mohammadi", "Tehran")
arshia.talk()
print(pedram.city)
