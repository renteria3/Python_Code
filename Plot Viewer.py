'''
Plot Viewer
- Define the SOLID principles.
- Identify the importance of requirements elicitation.
- Implement the model-view-controller pattern.

Jesse Renteria III
Week 8 - 05/16/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/wLuIRIw3rOw

'''

import random

class PlotViewer:
    'It will serve as the view and the controller for the plot generator classes'
    def registerPlotGenerator(self,pg):
        'sets up self.pg & runs the rpv'
        self.pg = pg
        self.pg.registerPlotViewer(self)

    def generate(self): # this way would make me rewrite all the functions in the same manner
        'return self.pg.generate()'
        return self.pg.generate()
    
    def queryUser(self,str):
        'return input(str)'
        return input(str)

    def getInfo(self,filename='plot_names',times=1): # might be a better way to get info randomly
        'return plotDict or lst[ranN]'
        path = '/Users/jrent/OneDrive/Documents/DSC_430_Gemmell/' + filename + '.txt'
        with open(path) as infile:
            lst = infile.read().strip().split('\n') 
            length = len(lst)
            plotDict = {} # puts options into a dictionary -- makes it easy for the viewer to decide and for the controller call the option easier
            for n in range(times):
                ranN = random.randrange(length)
                if times == 1:
                    return lst[ranN].strip() # used strip again to ensure no extra spaces
                else:
                    plotDict[n+1] = lst[ranN].strip() # gives a number to each plot detail/info & used strip again to ensure no extra spaces
            return plotDict
    
    def getTxtNames(self):
        'return textFileNames'
        textFileNames = ['plot_names','plot_adjectives','plot_profesions','plot_verbs','plot_adjectives_evil','plot_villian_job','plot_villains']
        return textFileNames

    def display(self, dict):
        'print(dict)'
        print(dict)

class SimplePlotGenerator:
    "When queried for a plot returns 'Something happens'"
    def registerPlotViewer(self,rpv):
        'sets up self.rpv'
        self.rpv = rpv   
        
    def generate(self):
        "return f'Something happens'"
        return f'Something happens'

class RandomPlotGenerator(SimplePlotGenerator): # must extend SimplePlotGenerator
    'when queried for a plot returns a random plot produced from the seven files'
    def generate(self):
        "return f'{self.pn}, a {self.pa} {self.pp}, must {self.pv} the {self.pae} {self.pvj}, {self.pv}.'"
        textFileNames = self.rpv.getTxtNames()
        plotAnswer = []
        for q in textFileNames:
            plotAnswer.append(self.rpv.getInfo(q))
        return f'{plotAnswer[0]}, a {plotAnswer[1]} {plotAnswer[2]}, must {plotAnswer[3]} the {plotAnswer[4]} {plotAnswer[5]}, {plotAnswer[6]}.'

class InteractivePlotGenerator(SimplePlotGenerator): # must extend SimplePlotGenerator
    'when queried for a plot offers the user a list of five random plot_names'
    def generate(self):
        "return f'{final[0]}, a {final[1]} {final[2]}, must {final[3]} the {final[4]} {final[5]}, {final[6]}.'"
        textFileNames = self.rpv.getTxtNames()
        text = ['name','adjective','profession','action','adjective','job','name']
        character = ['Hero','Hero','Hero','Hero','Villian','Villian','Villian']
        final = []

        for n in range(7):
            options = self.rpv.getInfo(textFileNames[n],5) # 5 because you need 5 options
            self.rpv.display(options)  # the five options for the user to select from 
            phrase = f'Enter the number of the {text[n]} for the {character[n]} you would like to use: '
            response = self.rpv.queryUser(phrase) 
            final.append(options[int(response)]) # looks at the dict and puts it into final
        return f'{final[0]}, a {final[1]} {final[2]}, must {final[3]} the {final[4]} {final[5]}, {final[6]}.'

    

pv = PlotViewer()

## 1st Case
pv.registerPlotGenerator( SimplePlotGenerator() )
pv.generate()

## 2nd Case
pv.registerPlotGenerator( RandomPlotGenerator() )
pv.generate()

## 3rd Case
pv.registerPlotGenerator( InteractivePlotGenerator() )
pv.generate()


