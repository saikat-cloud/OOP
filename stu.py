

class Student:
    roll = ""
    gpa = ""

saikat = Student()
saikat.roll = 7
saikat.gpa = 3.25
print(f"Saikat's Roll is {saikat.roll}, and gpa is {saikat.gpa} ")

Riyad = Student()
Riyad.roll = 5
Riyad.gpa = 3.50
print(f"Riyad's Roll is {Riyad.roll}, and gpa is {Riyad.gpa} ")

Shuvo = Student()
Shuvo.roll = 2
Shuvo.gpa = 3.73
print(f"Saikat's Roll is {Shuvo.roll}, and gpa is {Shuvo.gpa} ")




# class Fresh:
#     def __init__(self,name,age):
#         self.n = name
#         self.a = age

#     def show(self):
#         return self.n

# water = Fresh('fresh water','20')
# print(water.show())



class Student:
    def __init__(self) -> None:
        pass

    def show(self):
        print('This is a new git test')