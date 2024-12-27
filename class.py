class Student:
    grade=10
    name="mohammad"
    def intro(self) :
        print("hi i am student")
    def display(self):
        print("the class variables are", self.grade, self.name)

obj1=Student()
obj1.intro()
obj1. display()