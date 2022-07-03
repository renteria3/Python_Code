'''
Game of Life
- Contrast NumPy arrays to standard Python lists.
- Create data visualizations.
- Manage a Pandas dataframe.


Jesse Renteria III
Week 9 - 05/23/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/8pbAe4zz5Co

'''

#from curses.panel import bottom_panel, top_panel
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import colors 
from matplotlib.pyplot import figure, draw, pause
import math

def main():
    'displays the Conway Board(s)'
    greeting()
    s = sizeQ()
    p = probabilityQ()
    t = iterationQ()
    response = boardQ() # show all iterations or only last
    board = conway(s, p)
    allboard = advance(board,t) # keeps all boards
    display(allboard,s,t,response) # function will determine whether or not to show all or just final board

def greeting():
    'print greeting'
    print('Howdy User! \n\nWe will be playing the Game of Life.')
    
def sizeQ(): # Ask what the user wants the size to be?
    'return response'
    response = int(input('\nWhat size would you like the array to be?: '))
    return response

def probabilityQ(): # Ask what the user wants the probability to be?
    'return response'
    print('\nPlease enter a decimal number between 0 and 1: ') 
    response = float(input('What would you like the probability to be ?: '))
    return response

def iterationQ(): # Ask how many iterations wants to do?
    'return response'
    response = int(input('\nHow many iterations would you like the board to undergo?: '))
    return response

def boardQ(): # Ask user if they want to see all the board versions
    "return response == 'YES'" # True or False
    print('\nPlease answer will yes or no to the following question: ')
    response = input('Would you like to see all of the different board version?: ')
    return response.upper() == 'YES'

def conway(s, p): # s = size of the array & p = probability of alive cells on board
    'return board'
    alive = round(p*s) # need to round just in case if it is a decimal
    dead = s-alive
    dimensions = int(math.sqrt(s)) # if s=100 then it will be 10 by 10 # convert to int from float
    board = np.array([1]*alive + [0]*dead)
    np.random.shuffle(board)
    board.shape = (dimensions,dimensions)    
    return board

def advance(b,t): # curious if there is a faster way or not 
    'return b -- new version based on t times'
    dim = b.shape
    size = dim[0]
    maxD = dim[0]-1
    allBoards = [] # put all arrays (versions of the boards) in here
    for round in range(1,t+1): 
        newB = []
        for y in range(size):
            upper = upperORleftN(y,maxD)
            lower = lowerORrightN(y,maxD)
            for x in range(size):
                left = upperORleftN(x,maxD)
                right = lowerORrightN(x,maxD)
                allNs = neighbors(b,x,y,upper,lower,right,left) # max would be 8
                loc = b[y,x]
                if loc == 1:
                    if allNs < 2:
                        newB.append(0) # becomes 0 (die by underpopulation)
                    elif allNs == 2 or allNs == 3:
                        newB.append(1) # stays 1 (lives on to next gen)
                    elif allNs > 3:
                        newB.append(0) # becoms 0 (die by overpopulation)
                elif loc == 0:
                    if allNs == 3:
                        newB.append(1) # becomes 1 (lives by reproduction)
                    else:
                        newB.append(loc)
        allBoards.append(newB)
        b = np.array(newB) # allows for the new version of the board to be created
        b.shape = dim # sets up the board properly
    return allBoards 

def neighbors(b,x,y,upper,lower,right,left):
    'return allNs'
    n1 = b[upper,left] 
    n2 = b[upper,x] 
    n3 = b[upper,right] 
    n4 = b[y,left] 
    n5 = b[y,right] 
    n6 = b[lower,left] 
    n7 = b[lower,x] 
    n8 = b[lower,right] 
    allNs = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    return allNs

def upperORleftN(xy,maxD): # to figure out the uppper/left value
    'return upperORleft'
    if xy == 0: 
        upperORleft = maxD
    else:
        upperORleft = xy-1
    return upperORleft

def lowerORrightN(xy,maxD): # to figure out the lower/right value
    'return lowerORright'
    if xy == maxD: 
        lowerORright = 0
    else:
        lowerORright = xy+1 
    return lowerORright 

def display(allBoards,size,round,response):
    'plt.show()'
    dim = int(size**(1/2))
    if int(response) == 1: # shows all boards
        while True:
            length = len(allBoards)
            fg = figure()
            ax = fg.gca()

            newboard = np.array(allBoards[0])
            newboard.shape = (dim,dim)
            colormap = colors.ListedColormap(['white', 'black']) # white is 0 black is 1
            h = ax.imshow(newboard, cmap=colormap)
        
            for n in range(1,length+1):
                nboard = np.array(allBoards[n-1])
                nboard.shape = (dim,dim)
                h.set_data(nboard)
                plt.title(f'{dim}x{dim} Conway Board at T={n}')
                draw(), pause(1)
            if not exitCode():
                break

    else: # shows only final board
        newBoard = np.array(allBoards[-1])
        newBoard.shape = (dim,dim)
        colormap = colors.ListedColormap(['white', 'black']) # white is 0 black is 1
        plt.imshow(newBoard,cmap=colormap)
        plt.title(f'{dim}x{dim} Conway Board at T={round}') 
        plt.show()


def exitCode(): #determines whether or not to exit the code
    'returns True or False'
    response = input('\nWould you like to see the different board versions again? (Yes or No): ')
    return response.strip().upper() == 'YES'

main()

