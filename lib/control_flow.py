#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password = '12345':
        return 'Access Granted'
    else:
        return "Access Denied"   
    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out here"
    if (temperature>=40 and temperature<=65):
        return "It's a bit chilly out here"
    else:
        return "It's perfect out here"


def fizzbuzz(num):
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
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
        return "Invalid operation"