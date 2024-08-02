from module import welcome, goodbye

# Creating instances of the classes
welcome_message = welcome()
goodbye_message = goodbye()

# User input for name
user_name = input(" Enter your name: ")

# Printing personalized greetings
print(welcome_message.greet(user_name))
print(goodbye_message.bye(user_name))