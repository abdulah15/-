class Library:
    def __init__(self):
        self.books = ["Python", "Rich Dad Poor Dad", "Harry Potter", "C++ Basics", "Algorithms by CLRS"]
    
    def display_books(self):
        print("We have the following books in our library:")
        for book in self.books:
            print(book)

def main():
    print("Welcome to our library! Please enter your name:")
    user_name = input("Your name: ")
    print(f"Hello {user_name}, welcome to the Let's Upskill library. Please choose an option:")
    
    while True:
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Quit")
        
        choice = int(input("Enter your choice to continue: "))
        
       
        if choice == 5:
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break
        else:
            print("Feature not implemented yet. Please try another option.")

