'''
Happy Primes
- Select an appropriate loop pattern for a given task.
- Choose a Python list or dictionary for a given task.
- Explain encapsulation.
- Catch and handle errors in Python code.
- Develop solutions for solving mathematical problems using appropriate patterns and data structures.

Jesse Renteria III
Week 3 - 04/11/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/srSHsJ9MbLY

'''

def happyPrimes(): #main code that user will have to type out
    'request a positive integer, determines (prime or not) & (happy or sad), & prints results'
    greeting() #greets user and tells them the purpose of the code
    while True:
        number = requestNumber()#asks the user for number
        prime = primeCheck(number)#checks to see if number is a prime number
        mood = determineMood(number)#checks to see if number is a happy number
        result(number,prime,mood)#prints out whether it is a happy prime, sad prime, happy non-prime, or sad non-prime
        if exitCode(): #asks the user whether or not they want to exit the code
            break

def greeting(): #introduces the code
    'prints a greeting and introduces what the code will do'
    print('Howdy User!\n')
    print('Given the input, the code will print out whether it is a happy prime, sad prime, happy non-prime, or sad non-prime.\n')


def requestNumber():#gets number to feed other functions
    'return number (number user enters)'
    while True: #repeats until user enters in a positive integer
        try:
            number = input('Please enter a positive integer: ')
            response = int(number)
            break
        except:
            print('Enter a positive integer using digits 0-9.')
    return number

def primeCheck(number): #if true then it is a prime number
    'return result%number == 0 (Prime or not)'
    #Using Fermat's Theorem
    number = int(number) #converting it now b/c need string version
    result = (2**number)-2
    return result%number == 0

def splitDigits(number): #splits digits of the number
    'return digits (lists of digits in the number)'
    number = str(number)#Will be important when you doing the code more than once
    digits = []
    for i in range(len(number)):
        digits.append(int(number[i]))#convert to number to feed the equation properly
    return digits

def determineMood(number):#determines whether number is happy or sad
    'return new == 1 (If true then number is happy)'
    resultDict = {} #need to keep a dict of previous results & dict faster than lst
    while True:
        result = 0
        digits = splitDigits(number)
        for i in range(len(digits)):
            result += digits[i]**2
        if result != 1:
            if result not in resultDict:
                resultDict[result] = 1
                number = result
            elif result in resultDict:
                break
        else:
            break
    return result == 1

def result(number, prime, mood): #prints out the all results of the number
    "print(number + ' is a happy/sad prime/non-prime')"
    if prime:
        if mood:
            print(number + ' is a happy prime')
        else:
            print(number + ' is a sad prime')
    if not prime:
        if mood:
            print(number + ' is a happy non-prime')
        else:
            print(number + ' is a sad non-prime')

def exitCode(): #determines whether or not to exit the code
    'returns True or False'
    response = input('\nAre you ready to exit the code? (Yes or No): ')
    return response.strip().upper() == 'YES'




