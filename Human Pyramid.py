'''
Human Pyramid
- Identify the asymptotic run time of an algorithm.
- Choose iterative or recursive methods based on program requirements.
- Compare the impact of asymptotic run times.
- Apply efficient design strategies to solving complex programming problems.

Jesse Renteria III
Week 4 - 04/18/2022

I have not given or received any unauthorized assistance on this assignment.

YouTube Link:
https://youtu.be/K_TFn66Mefc

'''
def humanPyramid(row,column): #recursive function to figure out how much weight the specific human is carrying
    'returns amount of weight carrying for specified position'
    #Note: 128 is the assumed weight for the humans in the pyramid
    if row < 1 and column < 1: # TOP: condition for the top of the pyramid
        return 0
    elif column == 0: # SIDE1: condition for the side of the pyramid where column is 0
        return (humanPyramid(row-1,column) + 128)//2
    elif row == column: # SIDE2: condition for the side of the pyramid where row and column are the same number
        return (humanPyramid(row-1,column-1) + 128)//2
    else: # MIDDLE: condition for the ones in the middle of the pyramid 
        return (humanPyramid(row-1,column-1) + humanPyramid(row-1,column) + 2*128)//2   
    
