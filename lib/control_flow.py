#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    
    

# dog = "cuddly"

# dict_map = {
#     "hungry": "Refilling food bowl.",
#     "thirsty": "Refilling water bowl.",
#     "playful": "Playing tug-of-war.",
#     "cuddly": "Snuggling.",
# }

# # Remember that a dictionary's .get() method lets us set a default value!
# owner = dict_map.get(dog, "Reading newspaper.")



# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
#     finally:
#         print("Isn't division fun?")
# divide(10,2)

# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")




# dog = "cuddly"
# if dog == "hungry":
#     owner = "Refilling for bowl."
# elif dog == "thirsty":
#     owner = "refilling water bowl."
# elif dog =="playful":
#     owner ="Playing tug-of-war."
# elif dog == "cuddly":
#     owner = "snuggling"
# else:
#     owner = "reading newspaper"

# def control_flow(value):
#     if value:
#         print("yep!")
#     else:
#         print('nope!')

# control_flow(False)
# control_flow(None)
# control_flow(True)
# control_flow("")
# control_flow(0)
# control_flow("0")