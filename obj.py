class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


people1 = People("Alice", 25)
people2 = People("Bob", 30)
people3 = People("Charlie", 22)



print("1st Person :")
people1.display()

print("2nd Person :")
people2.display()

print("3rd Person :")
people3.display()

del people1
print("1st Person :")
people1.display()
