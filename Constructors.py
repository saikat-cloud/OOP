

# class Empleyee:
#     no_of = 8

#     def informe(self):
#         return f"Name is {self.name} his salary is {self.salary} and his role is {self.role}"


# harry = Empleyee()
# ruhan = Empleyee()


# harry.name = "Harry"
# harry.salary = 555
# harry.role = "Intern"

# ruhan.name = "Ruhan"
# ruhan.salary = 444
# ruhan.role = "junior"

# print(harry.informe())

#...........................

class Empleyee:
    no_of = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        

    def informe(self):
        return f"Name is {self.name} his salary is {self.salary} and his role is {self.role}"


harry = Empleyee("Harry", 555, "Junior")
ruhan = Empleyee("Ruhan", 444, "junior")


# harry.name = "Harry"
# harry.salary = 555
# harry.role = "Intern"

# ruhan.name = "Ruhan"
# ruhan.salary = 444
# ruhan.role = "junior"

# print(harry.informe())

print(ruhan.salary)
print(harry.name)

