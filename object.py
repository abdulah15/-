class student:
    def __init__(self,username):
        self.username=username

    def display(self):
        print("welcome"+self.username)

username=input("enter you name")

obj1=student(username)
obj1.display()