import pyttsx3
import math

engine = pyttsx3.init()

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def addition():
    one = int(input('What is your first number? '))
    speak(one)
    two = int(input('what is your second number? '))
    speak(two)
    sum = one + two
    print(sum)
    speak(str(sum))

def Subtraction():
    one = int(input('What is your first number ? '))
    speak(one)
    two = int(input('what is your second number? '))
    speak(two)
    ans = one - two
    print(ans)
    speak(str(ans))

def Multiplication():
    one = int(input('What is your first number ? '))
    speak(one)
    two = int(input('what is your second number? '))
    speak(two)
    product = one * two
    print(product)
    speak(str(product))


def Division():
    one = int(input('What is your first number? '))
    speak(one)
    two = int(input('What is your first number? '))
    speak(two)
    quotiont = one / two
    print(quotiont)
    speak(str(quotiont))
    
def Modulo():
    one = int(input('What is your first number? '))
    speak(one)
    two = int(input('what is your second number? '))
    speak(two)
    remainder = one % two
    print(remainder)
    speak(str(remainder))

calc_on = 1

def quit():
    print("Thanks for using this app")
    speak("Thanks for using this app")
    global calc_on
    calc_on = 0


def calc_run():
    op = input("Enter function: ")
    speak(f"You chose {op}")
    print(f"You chose {op}")
    if op == 'add':
        addition()
    elif op == 'subtract':
        Subtraction() 
    elif op == 'multiply':
        Multiplication() 
    elif op == 'divide':
        Division()
    elif op == 'modulo':
        Modulo()  
    elif op=='quit':
        quit()


speak("Do you want to add,subtract,multiply,divide, modulo or quit. ")
print('Do you want to add,subtract,multiply,divide, modulo or quit. ')

while calc_on == 1: 
    calc_run()
