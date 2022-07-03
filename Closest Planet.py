'''
Closet Planet

Jesse Renteria III
Week 10 - 05/30/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/D2Ww-q6hq24 

'''
import numpy as np
import matplotlib.pyplot as plt 
import math
import pandas as pd
import csv
import random

#### Assignment 1001 ####
class Planet:
    "Sets up planet location and figures out the planets's position"
    def __init__(self,radius, year):
        'return location - position of planet on a specific day'
        self.radius = radius
        self.year = year
    
    def position(self,day): # Returns the position of the planet on a specific day
        'return location - position of planet on a specific day'
        if day > self.year: # positive that is greater than the self.year
            times = day//self.year
            diff = day - (self.year*times)
            location = self.findXY(diff)
            return location
        elif self.year >= day and day >= 0: # if day is between 0 and self.year
            location = self.findXY(day)
            return location
                 
    def findXY(self,day): #### Figure out the X & Y function
        'return location'
        q1Year = self.year/4 # highest day in q1
        q2Year = self.year/2 # highest day in q2
        q3Year = q1Year + q2Year # highest day in q3
        if q1Year >= day: # both X & Y are postive
            if q1Year == day:
                x = 0
                y = self.radius
            else:
                x = self.findX(day,q1Year)
                y = self.findY(x)
        elif q2Year >= day: # X is negative & Y is postive
            if q2Year == day:
                x = -self.radius
                y = 0
            else:
                nday = q2Year - day 
                x = -(self.findX(nday,q1Year))
                y = self.findY(x)
        elif q3Year >= day: # both X & Y are negative
            if q3Year == day:
                x = 0
                y = -self.radius
            else:
                nday = q3Year - day 
                x = -(self.findX(nday,q1Year))
                y = -(self.findY(x))
        elif day >= q3Year: # X is postive & Y is negative
            if self.year == day:
                x = self.radius
                y = 0
            else:
                nday = self.year - day
                x = self.findX(nday,q1Year)
                y = -(self.findY(x))
        location = round(x,2),round(y,2)        
        return location
        #print(f'{round(x,2)}, {round(y,2)}')
    
    def findX(self,day,q1Year): #### Figure out the X & Y function
        'retturn xfinal'
        angle = (day/q1Year)*90 # angle depends on day number
        rad = math.radians(angle)
        value = math.cos(rad) # CAH H = radius
        x = value * self.radius
        return x 
        
    def findY(self,x):
        'return yfinal'
        y = math.sqrt((self.radius**2)-(x**2)) # x**2 + y**2 = r**2
        return y 

def distance(planet1,planet2,day): # return the distance between the planets on that day     
    'return distanceBtwn - the distance between the planets on that day'
    p1 = planet1.position(day)
    p2 = planet2.position(day)
    distanceBtwn = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return round(distanceBtwn,2)

#### End of Assignment 1001 #####

class Simulation(Planet):
    'Runs for 1000 Earth years. On each day, compute the distance between every pair of planets, keeping the average'
    def __init__(self):
        'sets up all the planets information'
        self.mercury = Planet(3.5,88)
        self.venus = Planet(6.7,225)
        self.earth = Planet(9.3,365)
        self.mars = Planet(14.2,687)
        self.jupiter = Planet(48.4,4333)
        self.saturn = Planet(88.9,10759)
        self.uranus = Planet(179,30687)
        self.neptune = Planet(288,60190)
        self.planets = np.array([self.mercury,self.venus,self.earth,self.mars,self.jupiter,self.saturn,self.uranus, self.neptune])
        self.headers = np.array(['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'])
    
    def avgD2P(self,p1,p2,runs=1000): # calculates average distance between two planets 
        'return avgD'
        totalDays = runs*365 #365 days is 1 Earth year
        testDays = int(totalDays * 0.2) # the test set of days - only 20% of the total
        random.seed(0) # not sure if I should keep this or not
        ranDays = random.sample(range(1,totalDays+1), testDays) # randomly selected days (total amount == testDays)
        totalPD = 0
        for day in ranDays:
            pd = distance(p1,p2,day)
            totalPD += pd 
        avgD = round(totalPD/testDays,2)
        return avgD

    def allPlanets(self): # All sets -- creates 8x8 for avg distance btwn Planets
        'return dValues'
        dValues = np.arange(64, dtype=float)
        dValues.shape = (8,8)
        for n in range(8):
            for num in range(n+1):
                if n == num:
                    dValues[n,num] = 0
                else:
                    value = self.avgD2P(self.planets[n],self.planets[num])
                    dValues[n,num] = value
                    dValues[num,n] = value
        return dValues

    def createChart(self): #displays 8x8 chart of the avg distances 
        'plt.show() -- displays 8x8 chart of avg distances'
        chart = self.allPlanets()
        fig, ax = plt.subplots() #define figure and axes

        fig.patch.set_visible(False) #hide the axes
        ax.axis('off')
        ax.axis('tight')

        rcolors = plt.cm.BuPu(np.full(len(self.headers),0.01)) 
        ccolors = plt.cm.BuPu(np.full(len(self.headers),0.01))

        plt.table(cellText=chart,
                            rowLabels=self.headers,
                            rowColours=rcolors,
                            rowLoc='right',
                            colColours=ccolors,
                            colLabels=self.headers,
                            loc='center')
        plt.show()
        
    def distancePerDay(self,days=1000): 
        'return distances'
        distances = [] 
        for n in range(1,days+1):
            myD = distance(self.earth, self.mercury, n)
            vsD = distance(self.earth, self.venus, n)
            msD = distance(self.earth, self.mars, n)
            distances.append([myD,vsD,msD])
        return distances

    def createDistanceFile(self): # create a csv file
        'creates the CSV file'
        header = ['mercury','venus','mars']
        distances = self.distancePerDay()
        with open('earthtoMyVsMs.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(distances)
    
    def createTimeSeries(self,planet='mercury'):
        'creates a timeseries'
        self.createDistanceFile()
        if planet == 'all':
            df = pd.read_csv('earthtoMyVsMs.csv')
            df.plot(figsize=(35,10)) 
            plt.title(f'Distance from Earth to Mercury, Venus & Mars over 1000 Days') 
            plt.xlabel('Days')
            plt.ylabel('Distance (1 CM = 1 Million Miles)')
            plt.show()       
        else:
            df = pd.read_csv('earthtoMyVsMs.csv',usecols=[planet]) 
            df.plot(figsize=(35,10)) 
            plt.title(f'Distance from Earth to {planet.capitalize()} over 1000 Days')
            plt.xlabel('Days')
            plt.ylabel('Distance (1 CM = 1 Million Miles)')
            plt.show()       

sim = Simulation()
sim.createTimeSeries('all')
sim.createTimeSeries('mercury') 


sim.allPlanets()
sim.createChart()
sim.createDistanceFile()
