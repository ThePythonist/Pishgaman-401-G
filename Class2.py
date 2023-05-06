# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()
#
# farzand.say_goodbye()
# farzand.say_hello()


class Father:
    def __init__(self, fname, address, eyecolor, job):
        self.familyname = fname
        self.address = address
        self.eyecolor = eyecolor
        self.job = job

    def say_hello(self):
        print("Hello")


class Child(Father):
    def __init__(self, fname, address, eyecolor, school):
        super().__init__(fname, address, eyecolor, job=None)
        self.school = school

    def say_goodbye(self):
        print("Goodbye")


pedar = Father("Ahmadi", "Ekbatan, Varzesh St", "Green", "Engineer")
farzand = Child("Ahmadi", "Ekbatan, Varzesh St", "Green", "Alborz")

print(pedar.job)
print(farzand.school)
