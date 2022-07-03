'''
Cups & Dice Game
- Design Python classes.
- Implement Python operators for a class.
- Inheritance

Jesse Renteria III
Week 5 - 04/25/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/MTnXIUwk2pM

'''
import random

def game():
    'has user play a dice game and returns the results of if there roll matches the goal or is close to the goal'
    name = greeting() #greeting
    if not playGame(name): #ask if they want to play
        return goodBye(name) #goodbye message
    run = 0 #keeps count of number of times played
    results = [] #keeps track of totals of each round
    while True:
        run += 1
        goal = ranNumber() #creates random number i.e. goal
        bet = placeBet(run,results) #asks for the bet
        balance = bankBalance(bet,run,results) #removes bet from balance
        six = sixDice() #ask for how many six sided dice
        ten = tenDice() #ask for how many ten sided dice
        twenty = twentyDice() #ask for how many twenty sided dice
        outcome = rollCup(six,ten,twenty,bet,goal,balance) #rolls dice and displays results #rollAmount
        reportResults(name, outcome,results) #displays the total rolled and updated balance
        if autoEnd(outcome,name): #ends game if balance is 0
            break
        if not repeatGame(): #asks if they want to play again
            goodBye(name) #goodbye message
            break       

def greeting(): # Greet the user and ask their name.
    'prints a greeting and introduces what the code will do'
    print('Howdy User!\nThis game if you choose to play is all about seeing if the dice you roll will add up to the goal. ')
    print('You will be allowed to bet any amount as long as it is not greater than your balance.')
    print('Your beginning balance will be 100. Good Luck!')
    name = input('What is your name? ')
    return name

def playGame(name): # Ask them if they would like to play a game.
    "return response == 'Yes'"
    print(f'Thank you {name}!')
    response = input('Would you like to play a game? ')
    return response.upper() == 'YES'

def ranNumber():# Generate a random number between 1 and 100. This number will be called the goal.
    'return goal -- a random number between 1 and 100'
    goal = random.randrange(1,101)
    return goal

def placeBet(run, results): # Ask the user how much they would like to bet. This money is deducted from their account.
    'return bet -- amount user would like to bet'
    bet = int(input('How much would you like to bet? ')) #needs to be a positive number
    while bet < 0 or (run > 1 and results[run-2] < bet):
        if bet < 0:
            print('Your bet cannot be a negative amount. Please enter a positive amount using digits 0-9.')
            bet = int(input('How much would you like to bet? ')) #needs to be a positive number
        elif run > 1 and results[run-2] < bet:
            print('You cannot bet more than your balance amount. Please enter a smaller amount.')
            bet = int(input('How much would you like to bet? ')) 
    return bet

def bankBalance(bet,run,results):
    'return balance'
    if run > 1:
        balance = results[run-2] - bet
    else:
        balance = 100-bet
    return balance

def sixDice(): # Ask the user how many of each die they would like to roll.
    'return six -- amount of six sided die'
    six = int(input('How many six sided die would you like to roll? '))
    return six

def tenDice():
    'return ten -- amount of ten sided die'
    ten = int(input('How many ten sided die would you like to roll? '))
    return ten

def twentyDice():
    'return twenty -- amount of twenty sided die'
    twenty = int(input('How many twenty sided die would you like to roll? '))
    return twenty

# Create a cup filled with dice according to the user’s input.

def rollCup(six,ten,twenty,bet,goal,balance):# Roll the cup and display the results.
    'return amount -- the amount from all the dice rolled'
    amount = Cup(six,ten,twenty)
    amount = amount.roll()
    if amount == goal: # If the roll exactly matches the goal, the user receives 10x bet added to their balance.
        balance += 10*bet
        print(f'\nYou rolled {amount}. Your roll exactly matches the goal!')
    elif amount < goal:
        if amount >= goal-3: # Otherwise, if the roll is within 3 of the goal but not over, the user receives 5x bet added to their balance.
            balance += 5*bet
            print(f'\nYou rolled {amount}. Your roll is within 3 of the goal!')
        elif amount >= goal-10: # Otherwise, if the roll is within 10 of the goal but not over, the user receives 2x bet added to their balance.
            balance += 2*bet
            print(f'\nYou rolled {amount}. Your roll is within 10 of the goal!')
        else:
            print(f'\nYou rolled {amount}. Your roll did not meet the goal.')
    else:
        print(f'\nYou rolled {amount}. Your roll did not meet the goal.')
    outcome = (amount,balance)
    return outcome 

def reportResults(name,outcome,results): # Report the results to the user. The message should include their name and updated balance.
    "return f'{name}, you rolled a total of {outcome[0]}. Your updated balance is {outcome[1]}.'"
    results.append(outcome[1])
    print(f'\n{name}, you rolled a total of {outcome[0]}. Your updated balance is {outcome[1]}.')

def autoEnd(outcome,name):
    'return outcome[1] == 0'
    if outcome[1] == 0:
        print(f'\nTough Luck!\nLooks like you do not have any more money to bet.\n\nThank you for playing {name}, we will see you next time!')
    return outcome[1] == 0 

def repeatGame(): # Ask if they would like to play again. If so, go to step 4.
    "return answer.upper() == 'YES'"
    answer = input('\nWould you like to play the game again? ')
    return answer.upper() == 'YES'

def goodBye(name):
    "print('Thank you {name}! Have an incredible day!')"
    print(f'Thank you {name}! Have an incredible day!')


### Assignment 0501 -- Need it for 0502 to run properly 

class SixSidedDie:
    'represents rolling a six sided die'
    def __repr__(self,side='Six'): # only returns the format
        'return f"SixSidedDie({self.n})"'
        self.side = side
        return f"{self.side}SidedDie({self.n})"

    def roll(self, n=6): #rolls the die
        'return random.randrange(1,n+1)'
        self.n = random.randrange(1,n+1)
        return self.n 
    
    def getFaceValue(self):
        'return face value of the die'
        return self.n

class TenSidedDie(SixSidedDie):
    'represents rolling a ten sided die'
    def __repr__(self): # only returns the format
        "return super().__repr__('Ten')"
        return super().__repr__('Ten')
    def roll(self):
        'return super().roll(10)'
        return super().roll(10)


class TwentySidedDie(SixSidedDie):
    'represents rolling a twenty sided die'
    def __repr__(self): # only returns the format
        "return super().__repr__('Twenty')"
        return super().__repr__('Twenty')
    def roll(self):
        'return super().roll(20)'
        return super().roll(20)

class Cup: 
    'represents rolling six/ten/twenty sided dice from a cup'
    def __init__(self,six=1,ten=1,twenty=1): #cup defaults to have 1 of each type die
        'initialize count of each the six, ten, twenty dice'
        self.six = six
        self.ten = ten
        self.twenty = twenty
        self.total = 0
        self.complete = []

    def getSum(self): #receive the total, similiar to getFaceValue
        'return self.total -- sum of all the dice'
        return self.total
    
    def __repr__(self): #print out all the rolls formally
        'return f"Cup{self.final}"'        
        self.final = str(self.complete).replace('[','(').replace(']',')')
        return f"Cup{self.final}"

    def roll(self): #rolls the die -- Needs to feed to each type of die, loop maybe
        'return self.total -- total of all dice values'
        if self.six > 0: #this is good 
            for n in range(self.six):
                self.run = SixSidedDie()
                self.total += self.run.roll()
                self.complete.append(self.run)
        if self.ten > 0:
            for n in range(self.ten):
                self.run = TenSidedDie()
                self.total += self.run.roll()
                self.complete.append(self.run)
        if self.twenty > 0:
            for n in range(self.twenty):
                self.run = TwentySidedDie()
                self.total += self.run.roll()
                self.complete.append(self.run)
        #print(str(self.complete))
        return self.total
