class Student:
    def __init__(self, f, l, e):
        self.firstName = f
        self.lastName = l
        self.email = e


stud = Student('Abhinav','P','abhinav.p@gmail.com')
print(stud.firstName)
print(stud.lastName)
print(stud.email)
