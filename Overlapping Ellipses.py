'''
Overlapping Ellipses
- Build a pseudo-random number generator
- Explain how randomness can be used to solve complex problems.
- Design an accept-reject algorithm to solve geometry problems.

Jesse Renteria III
Week 7 - 05/09/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:

https://youtu.be/odxQdcmc-kU
'''
### Questions to Ask
# - Do you know how to work with Turtle for the visualization?
# - How do you fix my object year when calling __repr__ for P1/P2 in Ellipse?

# I think area is figured out by the number of darts
# Need to fix random still - but closer because it is 0.46.....

from cmath import sqrt
import random
import math
import turtle

############################# START OF A701 - NEED THIS TO GENERATE DARTS #############################

class WarAndPeacePseudoRandomNumberGenerator:
    'Generates a Pseudo Random Number based on War & Peace txt file'   
    def __init__(self,seed=1000):
        'set up class in order for all the functions within can run properly'
        self.seed = seed
        self.step = 100
        self.final = 0
        self.restart = 1 #used if you have reached the end of the doc so you can restart
        self.characters = []

    def createLst(self):
        'return self.characters -- list of 64 characters'
        with open('/Users/jrent/OneDrive/Documents/DSC_430_Gemmell/war-and-peace.txt') as wnp:
            count = 0
            while True:
                if count == 64:
                    break
                else:
                    wnp.seek(self.seed-1) 
                    char = wnp.read(1)
                    self.seed += (self.step) # sets a new cursor location
                    if char == '': # you reached the end of doc & need to start from beginning
                        self.seed = self.restart
                        self.restart += 1
                    if count//2 != 0: # means that its odd & doesnt need to be compared
                        self.characters.append(char)
                        count += 1
                    elif count//2 == 0: # means that its even & needs to be compared
                        if count == 0 or count == 1:
                            self.characters.append(char)
                            count += 1
                        elif char != self.characters[-1]:
                            self.characters.append(char)
                            count += 1
            return self.characters

    def random(self):
        'return self.final -- pseudo number'
        charlst = self.createLst()
        for n in range(1,33):
            if charlst[n-1] > charlst[n]:
                self.final += 1/(2**n)
        return self.final
    
    def getSeed(self):
        'return self.seed'
        return self.seed

############################################# END OF A701 #############################################

def computeOverlapOfEllipses(e1,e2): #takes two ellipses and returns the area of the overlap
    'return overlap'
    numDarts = 10000
    xValues = gatherXs(e1,e2)
    yValues = gatherYs(e1,e2)
    mWidth = maxW(e1,e2)

    leftB = determineMinB(xValues,mWidth)
    rightB = determineMaxB(xValues,mWidth)
    bottomB = determineMinB(yValues,mWidth)
    topB = determineMaxB(yValues,mWidth)
    
    boxA = boxArea(leftB,rightB,bottomB,topB)
    hits = dartThrows(numDarts,leftB,rightB,bottomB,topB,e1,e2)
    areas = ellipseAreas(numDarts,boxA,hits)
    printResults(e1,e2,numDarts,hits,areas) #area1,area2,
    #return areas[0] #overlap

def gatherXs(e1,e2): # stand alone
    'return xValues'
    xValues = []
    xValues.append(e1.getP1().getX())
    xValues.append(e1.getP2().getX())
    xValues.append(e2.getP1().getX())
    xValues.append(e2.getP2().getX())
    return xValues

def gatherYs(e1,e2): # stand alone
    'return yValues'
    yValues = []
    yValues.append(e1.getP1().getY())
    yValues.append(e1.getP2().getY())
    yValues.append(e2.getP1().getY())
    yValues.append(e2.getP2().getY())
    return yValues

def maxW(e1,e2): # stand alone # determine max width of ellipses
    'return max(wValues) -- determine max width'
    wValues = []
    wValues.append(e1.getWidth())
    wValues.append(e2.getWidth())
    return max(wValues)

def determineMaxB(xyValues,mWidth): # stand alone & determine right/top boundary
    'return maxBoundary'
    maxBoundary = max(xyValues) + mWidth
    return maxBoundary

def determineMinB(xyValues,mWidth): # stand alone # determine left/bottom boundary
    'return minBoundary'
    minBoundary = min(xyValues) - mWidth
    return minBoundary

def determineDart(lowBoundary,highBoundary,num): # will be used in dartThrows function #scale and shift #keeps x in the box
    'return dartValue'
    diff = highBoundary - lowBoundary
    dartValue = diff * num + lowBoundary
    return dartValue

def pointDistance(ellipse,ptX,ptY): # will be used in dartThrows function #figures out A + B = D
    'return distance -- distance between two points'
    p1x = ellipse.getP1().getX()
    p2x = ellipse.getP2().getX()
    p1y = ellipse.getP1().getY()
    p2y = ellipse.getP2().getY()
    d1 = math.sqrt((ptX-p1x)**2 +(ptY-p1y)**2) 
    d2 = math.sqrt((ptX-p2x)**2 +(ptY-p2y)**2) 
    distance = d1 + d2
    return distance # will be used to see if it is <= width of specific ellipse


### This works but I want to try the visual
def dartThrows(numDarts,leftB,rightB,bottomB,topB,e1,e2): # feed number of darts to throw
    'return inEllipses'
    inEllipses = 0 #number of times, it hits with the overlapping area
    inE1 = 0 #number of times, it hits with the E1 area
    inE2 = 0 #number of times, it hits with the E2 area   
    width1 = e1.getWidth()    
    width2 = e2.getWidth()
    newSeed = 1000  
    for n in range(numDarts):
        nums = []
        for i in range(2):
            prng = WarAndPeacePseudoRandomNumberGenerator(newSeed)
            r = prng.random()
            nums.append(r)
            newSeed = prng.getSeed()
        x = determineDart(leftB,rightB,nums[0]) # between leftB and rightB (point in the box)
        y = determineDart(bottomB,topB,nums[1]) # between bottomB and topB (point in the box)
        
        de1 = pointDistance(e1,x,y) # feeds (x,y) into function to see what A + B is for E1
        de2 = pointDistance(e2,x,y) # feeds (x,y) into function to see what A & B is for E2

        if de1 <= width1 and de2 <= width2:
            inEllipses += 1
            inE1 += 1
            inE2 += 1
        elif de1 <= width1:
            inE1 += 1
        elif de2 <= width2:
            inE2 += 1
    hits = [inEllipses,inE1,inE2]
    return hits

def ellipseAreas(numDarts,boxA,hits): # not completely confident on the calculation
    'return area'
    areaBoth = (hits[0]/numDarts) * boxA
    areaE1 = (hits[1]/numDarts) * boxA
    areaE2 = (hits[2]/numDarts) * boxA
    areas = [areaBoth,areaE1,areaE2]
    return areas

def boxArea(leftB,rightB,bottomB,topB):
    'return boxA'
    width = rightB - leftB
    length = topB - bottomB
    boxA = width * length
    return boxA

def printResults(e1,e2,numDarts,hits,areas): #area1,area2,
    'prints the results from the running the code.'
    print(f'{e1.__repr__()} has area {areas[1]}.') # need to fix the repr
    print(f'{e2.__repr__()} has area {areas[2]}.') # need to fix the repr
    print(f'{hits[0]} out of {numDarts} generated points are in both ellipses.') #inEllipses
    print(f'The overlap of the two has area {areas[0]}.') #overlap

class Point:
    'Allows user to abstract the x and y'
    def __init__(self,x,y):
        'feeds x and y into point so users will can abstract later'
        self.x = x
        self.y = y
    
    def __repr__(self):
        ''
        return f'Point({self.x},{self.y})'
    
    def getX(self):
        'return self.x'
        return self.x

    def getY(self):
        'return self.y'
        return self.y

class Ellipse(Point): 
    'Allows user to abstract the p1, p2 and width. Also calculate the area'
    def __init__(self,p1,p2,width): # p1 & p2 will be points i.e. (x,y)
        'feeds p1, p2 and width into point so users will can abstract later'
        self.p1 = p1
        self.p2 = p2
        self.width = width
        self.p1x = self.p1.getX()
        self.p2x = self.p2.getX()
        self.p1y = self.p1.getY()
        self.p2y = self.p2.getY()
    
    def __repr__(self): # need to figure out how to fix this
        "return f'Ellipse({self.getP1()},{self.getP2()},{self.width})'"
        return f'Ellipse({self.getP1()},{self.getP2()},{self.width})'
      
    def getP1(self):
        'return self.p1'
        return self.p1

    def getP2(self):
        'return self.p2'
        return self.p2

    def getWidth(self):
        'return self.width'
        return self.width
    
    def getArea(self): #calculation is incorrect, need to fix
        'return area'       
        midptX = (self.p1x + self.p2x)/2
        midptY = (self.p1y + self.p2y)/2
        
        a = self.width/2
        c = math.sqrt((midptX-self.p1x)**2 +(midptY-self.p1y)**2)
        b = math.sqrt(a**2 - c**2)
               
        area = math.pi*a*b
        return area


p1 = Point(0,0)
p2 = Point(0,0)
e1 = Ellipse(p1,p2,2)
e2 = Ellipse(p1,p2,4)
computeOverlapOfEllipses(e1,e2)


p1 = Point(3,2)
p2 = Point(-2,2)
p3 = Point(-1,-3)
p4 = Point(1,3)
e1 = Ellipse(p1,p2,7)
e2 = Ellipse(p3,p4,8)
computeOverlapOfEllipses(e1,e2)


#e1.__repr__()
#e2.getP1().getX()
#e1.getArea()
#e1.getP1() # this woorks


'''

    #area1 = e1.getArea()
    #area2 = e2.getArea()
## Tried doing the visual but didnt understand turtle enough

def dartThrows(numDarts,leftB,rightB,bottomB,topB,e1,e2): # feed number of darts to throw
    'return inEllipses'
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    
    wn.setworldcoordinates(leftB,bottomB,rightB,topB)

    #not sure what the two below sections need    
    drawingT.up()
    drawingT.goto(leftB,0)
    drawingT.down()
    drawingT.goto(rightB,0)
    
    drawingT.up()
    drawingT.goto(0,topB)
    drawingT.down()
    drawingT.goto(0,bottomB)  

    width1 = e1.getWidth()    
    width2 = e2.getWidth()  
    inEllipses = 0 #number of times, it hits with the overlapping area  
    newSeed = 1000

    drawingT.up()
        
    for n in range(numDarts):
        nums = []
        for i in range(2):
            prng = WarAndPeacePseudoRandomNumberGenerator(newSeed)
            r = prng.random()
            nums.append(r)
            newSeed = prng.getSeed()
        x = determineDart(leftB,rightB,nums[0]) # between leftB and rightB (point in the box)
        y = determineDart(bottomB,topB,nums[1]) # between bottomB and topB (point in the box)
        
        drawingT.goto(x,y) # (x,y) is the location of the dart
        
        de1 = pointDistance(e1,x,y) # what is the d = d1 + d2 for e1 (d should be <= to width1)
        de2 = pointDistance(e2,x,y) # what is the d = d1 + d2 for e2 (d should be <= to width2)

        if de1 <= width1 and de2 <= width2:
            inEllipses += 1
            drawingT.color("blue")
        elif de1 <= width1:
            drawingT.color("green")
        elif de2 <= width2:
            drawingT.color("red")
        else:
            drawingT.color("yellow") 
    
    wn.exitonclick()
    return inEllipses
'''







'''
## REduced from these 4 down to 2 functions
def determineLeft(xValues,mWidth): # stand alone # determine left boundary
    'return leftB -- determine left boundary'
    leftB = min(xValues) - mWidth
    return leftB

def determineRight(xValues,mWidth): # stand alone # determine right boundary
    'return rightB -- determine right boundary'
    rightB = max(xValues) + mWidth
    return rightB

def determineBottom(yValues,mWidth): # stand alone # determine bottom boundary
    'return bottomB -- determine bottom boundary'
    bottomB = min(yValues) - mWidth
    return bottomB

def determineTop(yValues,mWidth): # stand alone # determine top boundary
    'return topB -- determine top boundary'
    topB = max(yValues) + mWidth
    return topB

'''

'''
### Trial of trying for the visualization

def dartX(leftB,rightB,num): # will be used in dartThrows function #scale and shift #keeps x in the box
    'return dartXvalue'
    prng = WarAndPeacePseudoRandomNumberGenerator()
    r = prng.random()
    diff = rightB-leftB
    dartXvalue = diff * num + leftB
    return dartXvalue

def dartY(bottomB,topB,num): ##scale and shift #keeps y in the box
    'return dartYvalue'
    diff = topB-bottomB
    dartYvalue = diff * num + bottomB
    return dartYvalue

        x = dartX(leftB,rightB,nums[0]) # between leftB and rightB (ensures x stays between x boundaries)
        y = dartY(bottomB,topB,nums[1]) # between bottomB and topB (ensures y stays between y boundaries)



def dartThrows(numDarts,leftB,rightB,bottomB,topB,e1,e2): # feed number of darts to throw
    'return inEllipses'
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    
    wn.setworldcoordinates(leftB,bottomB,rightB,topB)

    #not sure what the two below sections need    
    drawingT.up()
    drawingT.goto(leftB,0)
    drawingT.down()
    drawingT.goto(rightB,0)
    
    drawingT.up()
    drawingT.goto(0,topB)
    drawingT.down()
    drawingT.goto(0,bottomB)  

    inEllipses = 0 #number of times, it hits with the overlapping area  
    drawingT.up()
    
    width1 = e1.getWidth()    
    width2 = e2.getWidth()  
    for n in range(numDarts):
        newSeed = 1000
        nums = []
        for i in range(2):
            prng = WarAndPeacePseudoRandomNumberGenerator(newSeed)
            r = prng.random()
            nums.append(r)
            newSeed = prng.getSeed()
        x = dartX(leftB,rightB,nums[0]) # between leftB and rightB (point in the box)
        y = dartY(bottomB,topB,nums[1]) # between bottomB and topB (point in the box)
        drawingT.goto(x,y)
        # (x,y) is the location of the dart
        de1 = pointDistance(e1,x,y) # what is the d = d1 + d2 for e1 (d should be <= to width1)
        de2 = pointDistance(e2,x,y) # what is the d = d1 + d2 for e2 (d should be <= to width2)

        if de1 <= width1 and de2 <= width2:
            inEllipses += 1
            drawingT.color("blue")
        elif de1 <= width1:
            drawingT.color("green")
        elif de2 <= width2:
            drawingT.color("red")
        else:
            drawingT.color("yellow") 
    
    wn.exitonclick()
    return inEllipses


'''



'''
# this is the equation I am not confident on 
        d = math.sqrt(x**2 + y**2) 

        # below will work if d is calculated right
        if d <= width1 and d <= width2:
            inEllipses += 1
            drawingT.color("blue")
        elif d <= width1:
            drawingT.color("green")
        elif d <= width2:
            drawingT.color("red")
        else:
            drawingT.color("yellow") 

'''


'''
def dartThrows(numDarts,leftB,rightB,bottomB,topB,e1,e2): # feed number of darts to throw
    'return inEllipses'
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    
    wn.setworldcoordinates(leftB,bottomB,rightB,topB)
        
    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)
    
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)  

    inEllipses = 0 #number of times, it hits with the overlapping area  
    drawingT.up()
    
    width1 = e1.getWidth()    
    width2 = e2.getWidth()  
    for n in range(numDarts):
        newSeed = 1000
        nums = []
        for i in range(2):
            prng = WarAndPeacePseudoRandomNumberGenerator(newSeed)
            r = prng.random()
            nums.append(r)
            newSeed = prng.getSeed()
        x = dartX(leftB,rightB,nums[0]) # between leftB and rightB (point in the box)
        y = dartY(bottomB,topB,nums[1]) # between bottomB and topB (point in the box)
        drawingT.goto(x,y)
        d = math.sqrt(x**2 + y**2)
        if d <= width1 and d <= width2:
            inEllipses += 1
            drawingT.color("blue")
        else:
            drawingT.color("red") 
    wn.exitonclick()
    return inEllipses


def dartThrows(numDarts,leftB,rightB,bottomB,topB,e1,e2): # feed number of darts to throw
    'return inEllipses'
    inEllipses = 0 #number of times, pie shape wedge is hit   
    width1 = e1.getWidth()    
    width2 = e2.getWidth()  
    for n in range(numDarts):
        newSeed = 1000
        nums = []
        for i in range(2):
            prng = WarAndPeacePseudoRandomNumberGenerator(newSeed)
            r = prng.random()
            nums.append(r)
            newSeed = prng.getSeed()
        x = dartX(leftB,rightB,nums[0]) # between leftB and rightB (point in the box)
        y = dartY(bottomB,topB,nums[1]) # between bottomB and topB (point in the box)
        d = math.sqrt(x**2 + y**2)
        if d <= width1 and d <= width2:
            inEllipses += 1
    return inEllipses

def dartX(leftB,rightB): ##scale and shift #keeps x in the box
    'return dartXvalue'
    prng = WarAndPeacePseudoRandomNumberGenerator()
    r = prng.random()
    diff = rightB-leftB
    dartXvalue = diff * r + leftB
    return dartXvalue

def dartY(bottomB,topB): ##scale and shift #keeps y in the box
    'return dartYvalue'
    prng = WarAndPeacePseudoRandomNumberGenerator()
    r = prng.random()
    diff = topB-bottomB
    dartYvalue = diff * r + bottomB
    return dartYvalue


        #now how to determine if they are in either ellipse
        #based on the width of both ellipse??
        #something to this effect


# think this would be housed under Ellipse    
def centerPt(e): # not sure if this is really needed
    ''    
    xp1 = e.getP1().getX()
    xp2 = e.getP2().getX()
    yp1 = e.getP1().getY()
    yp2 = e.getP2().getY()

    centerX = (max(xp1,xp2) - min(xp1,xp2))/2
    centerY = (max(yp1,yp2) - min(yp1,yp2))/2
    return (centerX,centerY)
'''


'''
        xp1 = e2.getP1().getX()
        xp2 = e2.getP2().getX()
        yp1 = e2.getP1().getY()
        yp2 = e2.getP2().getY()


        e2.getP1().getX()
        e2.getP2().getX()
        e2.getP1().getY()
        e2.getP2().getY()
'''

'''

e1.getP1().getX() # this woorks
'''

#cross over ellipse
# 1 AREA put a box around the ellipses figure out l r t b
 # get all 4 x values then get min of those 4 it will get you the furtherest left
 # then get max w and go left whatever max w is (same logic for all the others)
# 2 N Place random points inside the box - create point -random x and y based off the prng
# 3 keep count of the number of hits 
# 4 calculate the area of the overlap

## Use to figure out if it is in the ellipse or not a + b = w
'''def montePi(numDarts): # feed number of darts to throw
    'return pi'
    inCircle = 0 #number of times, pie shape wedge is hit       
    for i in range(numDarts):
        x = random.random() # between 0 and 1 (point in the wedge)
        y = random.random() # between 0 and 1 (point in the wedge)
        d = math.sqrt(x**2 + y**2)   
        if d <= 1: # determines if it is inside the circle
            inCircle += 1
    pi = inCircle/numDarts * 4 # hits/num of darts = % we ended up inside and times 4 will be the whole pi
    return pi'''

'''
score = 90.0 * random() + 10.0
#the range of this variable is [10.0,100.0)

## functions to determine borders
def boxArea(xValues,yValues,mWidth):
    ''
    topB = max(yValues) + mWidth
    bottomB = min(yValues) - mWidth
    leftB = min(xValues) - mWidth
    rightB = max(xValues) + mWidth
    # need to figure out how to implement this

'''

## This is for graphing/visualization
def showMontePi(numDarts):
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    
    wn.setworldcoordinates(-2,-2,2,2)
    
    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)
    
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)
    
    circle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(x,y)
        if d <= 1:
            circle += 1
            drawingT.color("blue")
        else:
            drawingT.color("red")    
        drawingT.dot()
    pi = circle/numDarts * 4
    wn.exitonclick()
    return pi



