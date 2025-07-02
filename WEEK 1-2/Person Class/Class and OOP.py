
class Person:
    def __init__(self, name, age, mood):
        self.name = name
        self.age = age
        self.mood = mood

    def greet(self):
       print("Hello, my name is " + self.name + " and I'm feeling " + self.mood + ".")

    def predict_future(self):
       future_age = self.age + 10
       print("In 10 years, I’ll be " + str(future_age) + " years old.")

# Ask user for input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_mood = input("How are you feeling today? ")

# Convert age to integer
user_age = int(user_age)

# Create a Person object
person1 = Person(user_name, user_age, user_mood)

# Call methods
print("--- Your Info ---")
person1.greet()
person1.predict_future()
