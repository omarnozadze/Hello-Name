import random


Gretting = ["Hello", "Hi", "Nice day to you", "Welcome", "Wats up bro","Hey Hey Hey"]
randomGreeting = Gretting[random.randrange(0,5)] 

print(randomGreeting, input("What is your name?").title())

