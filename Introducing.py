

class Student:
    roll = ""
    gpa = ""

    def set(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa


    def display(self):
        print(f"Saikat's Roll is {self.roll}, and gpa is {self.gpa} ")



saikat = Student()
saikat.set(7,3.25)
saikat.display()

Riyad = Student()
Riyad.set(5,3.50)
Riyad.display()

Shuvo = Student()
Shuvo.set(3,3.75)
Shuvo.display()

