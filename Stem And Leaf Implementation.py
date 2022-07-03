'''
Stem And Leaf Implementation
- Describe pseudorandom numbers and their application in simple Monte Carlo simulations.
- Apply top-down-design to solve complex problems.
- Systematically debug modestly sized programs with well-designed unit tests.
- Contrast the advantages and disadvantages of top-down-design, prototyping, and spiral development.
- Design and implement a program to display a stem-and-leaf plot.

Jesse Renteria III
Week 2 - 04/04/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/HBQ0dbzRRqU

'''

def main(): #runs through all the functions before displaying the stem leaf plot
    'prints plot and continues until exitCode() == True'
    greeting()
    while True:
        numLst = numberAsk()
        tree = stemLeaves(numLst)
        orderedStem = formatStems(tree)
        displayPlot(tree,orderedStem)
        if exitCode():
            break

def greeting(): #greeting for the code
    'prints greeting'
    print('Howdy User!\n')
    print('This code will read the appropriate datafile (given the input) and displays a stem-and-leaf plot.')
    print('Enjoy running the code! \n')

def numberAsk(): #collects the file name
    'returns numberFile'
    response = input('Please type in 1, 2, or 3: ')
    numberFile = 'StemAndLeaf' + response.strip() + '.txt'
    numLst = getFile(numberFile)
    return numLst

def getFile(numberFile): #reads, closes, and produces list
    'return numLst'
    with open(numberFile) as infile:
        numLst = infile.read().replace('\n',',').split(',')
    return numLst

def plotLine(numLst): #determines where the line for the plot will go
    'return line (line to divide the numbers'
    lgthCount = []
    for num in numLst:
        lgth = len(num)
        if lgth not in lgthCount:
            lgthCount.append(lgth)
    line = min(lgthCount)//2
    return line
        
def stemLeaves(numLst): #purpose is to connect leaves with stems
    'return tree (leaves and stems)'
    tree = {} #dictionary format to make it easy
    line = plotLine(numLst)
    for num in numLst:
        length = len(num)
        if int(num[:length-line]) not in tree:
            tree[int(num[:length-line])] = num[-line]
        elif int(num[:length-line]) in tree:
            tree[int(num[:length-line])] += num[-line]
    return tree

def formatStems(tree): #figure out the range of the stems
    'return bStem, tStem (stem range)'
    stemLgth = []
    for s in tree:
        stemLgth.append(s)#int()
    tStem = max(stemLgth)
    bStem = min(stemLgth)
    orderedStem = organizedStem(bStem, tStem)
    return orderedStem

def organizedStem(bStem, tStem): #orders stems in desc order
    'return orderedStem'
    orderedStem = []
    for n in range(bStem,tStem+1):
        orderedStem.append(n)
    orderedStem.sort(reverse=True)
    return orderedStem

def displayPlot(tree,orderedStem): #displays the stem and leaf plot
    "print( str(n) + '|' + tree[n] (ie prints out the stems and leaves)"
    for n in orderedStem:
        if n in tree:
            if len(str(n)) == len(str(orderedStem[0])):
                print( str(n) + '|' + tree[n])
            else:
                print( ' ' + str(n) + '|' + tree[n])
        elif n not in tree:
            if len(str(n)) == len(str(orderedStem[0])):
                print( str(n) + '|')
            else:
                print( ' ' + str(n) + '|')

def exitCode(): #determines whether or not to exit the code
    'returns True or False'
    response = input('\nAre you ready to exit the code? (Yes or No): ')
    return response.strip().upper() == 'YES'

