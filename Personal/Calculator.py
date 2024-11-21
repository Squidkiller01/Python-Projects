import math #import math will be used for every line of code that has "math.pi" in it. For those, those cannot be done normally or otherwise
import random #import random will be used for every line of code that starts with "random." For this program, it will be used for random messages
import statistics #import statistics will be used for every line of code that has "statistics." For this program, it will be used for the data analysis section

'''
Welcome to Squidkiller's Calculator Program made from scratch! This was program was made for fun and was later used in a competition for school which went on to win 3rd place.
If you don't know how to read code or want to read the code, just look at the comments next to the code or the orange text (on codehs) or green text (on visual studio) with a hashtag (#) before it!
Please let Squid know of any bugs you may find or of any additions or changes you'd add.
Thanks to Death (my online friend) I was able to make this program since he suggested it and I would have never have thought of it without him
'''
#Latest Change-log without all the print syntax and commands and the such.
'''
    Version 5 | 1/13/2022
    UPDATE NOTES
    - Updated Change Log
    ADDED:
    - Added Surface Area and Volume to Geometry section

    DEVELOPERS NOTE:
    Been inactive for a while but have likely updated the calculator in between change log dates because I completely forgot about the change log
    so some things may be missing from this update!
'''
messages = 0
def latest_log():
    print('''-------------------------------------------------------------
    Version 5 | 1/13/2022
    UPDATE NOTES
    - Updated Change Log
    ADDED:
    - Added Surface Area and Volume to Geometry section

    DEVELOPERS NOTE:
    Been inactive for a while but have likely updated the calculator in between change log dates because I completely forgot about the change log
    so some things may be missing from this update!
--------------------------------------------------------------''')
def change_log():
    print('''-------------------------------------------------------------
Version 5 | 1/13/2022
UPDATE NOTES
- Updated Change Log
ADDED:
- Added Surface Area and Volume to Geometry section

DEVELOPERS NOTE:
Been inactive for a while but have likely updated the calculator in between change log dates because I completely forgot about the change log
so some things may be missing from this update!
--------------------------------------------------------------
Version 4.5 | 11/30/2021
UPDATE NOTES
- Updated Change Log
ADDED:
- Updated and expanded the Pythagorean Theorem expression to support solving for variables a and b and not just c
--------------------------------------------------------------
Version 4.2 | 11/15/2021
UPDATE NOTES
- Updated Change Log
ADDED:
- Added Missing function preventing program from working properly
--------------------------------------------------------------
Version 4.1 | 11/11/2021
UPDATE NOTES
- Updated Change Log
ADDED:
- Optimized code
- Added Constant Variable for exiting the program
- Added Trnasformation formulas inside the Geometry section (rotation, dilation, reflection, translation)
--------------------------------------------------------------
Version 4.0 | 11/10/2021
UPDATE NOTES
- Code moved over to Visual Studio
- Backed up code to github
- Updated Change Log
ADDED:
- Added seperate shape area formulas
- Added Physics formualas (initial velocity and force)
CHANGED:
- Fixed multiple variable errors within code
- Fixed choice errors within program and output
- Fixed multiple formatting errors
- Fixed spacing errors within Change log due to code transfer
--------------------------------------------------------------
Version 3.5.4 | 9/9/2021
UPDATE NOTES
-bug fix for Distance formula
--------------------------------------------------------------
Version 3.5.3 | 9/8/2021
UPDATE NOTES
Reached more than 1000 lines of functioning code!!!
ADDED:
- Fixed and complete Distance Formula
- Added Process of equations and rounding to Distance Formula
- Added a bee movie reference easter egg to string inputs (some are in binary)
- Added Rick Roll
CHANGED:
- Fixed Distance Formula
--------------------------------------------------------------
Version 3.5.2 | 9/7/2021
UPDATE NOTES
ADDED
- Added Modulus under the Algebra category
CHANGED
- Fixed not being able to select the Linear Equations
- Fixed error with the leave messages
- Updated Change-Log
- Updated Change-Log to be more visually appealing while reading code
--------------------------------------------------------------
Version 3.5.1 | 9/5/2021
UPDATE NOTES
ADDED
- Added Subject Orientated Equation Organization
- Added Linear Equations under the Algebra category
CHANGED
- Updated Change-Log
- Leave message now always played when leaving the calculator
--------------------------------------------------------------
Version 3.5 | 9/3/2021
UPDATE NOTES
ADDED
- Added Geometry Midpoint and Endpoint equations
- Added process of equations to Midpoint if the user so wishes to see how to solve for it
- Added a new leave easter egg message that has a 1/100 of happening for a total of two in total
CHANGED
- Changed Pythagorean Theorem process of equations error code
--------------------------------------------------------------
Version 3.4.1 | 3/30/2021
UPDATE NOTES
ADDED
- Made it so you can enter as many numbers on the supported equation. Addition, Subtraction, Multiplication, Division
- Added comments back into the code
--------------------------------------------------------------
Version 3.4 | 3/29/2021
UPDATE NOTES
ADDED
- Added seperation for when choices are made or an error has been made to make it more readable
CHANGED:
- Changed choice lines to be shorter and more complex but still have the same output
--------------------------------------------------------------
Version 3.3 | 3/22/2021
UPDATE NOTES
ADDED
- Added seperation when the program restarts
CHANGED:
- Changed expression output code to be a little more complex but still output the same thing
- Fixed some spelling errors
- Fixed rounding error message
--------------------------------------------------------------
Version 3.2.3 | 3/19/2021
UPDATE NOTES
ADDED
Added randomly generated leave messages
--------------------------------------------------------------
Version 3.2.2 | 3/18/2021
UPDATE NOTES
CHANGED
-Fixed function misspell causing option 9 to not work
-Fixed some functions missing a line of code
-Removed where it printed your previous option if you chose  to repeat the program
--------------------------------------------------------------
Version 3.2.1 | 3/18/2021
UPDATE NOTES
CHANGED:
- Updated Code description
--------------------------------------------------------------
Version 3.2 | 3/18/2021
UPDATE NOTES
NEW:
- Added a process as to which it shows you the process (only supported on Pythagorean theorem and non-rounded equations)
- Added a process that tells the user when they made an invalid input
- Added a process that repeats the program until the user wants to exit
- Added comments to code so non-code users or non-advanced code users can still read what the program does
- Added a cotinue option after each equation
- Added a change-log
--------------------------------------------------------------''')
#Calculator Program

p = ' ' # p is a placeholder value for when a variable, function, or loop requires it

def addition(y,p): # function for addition equations
    numbers = [] # empty list statement that prints the equation when you are done
    y = 0 # placeholder variable for integers (numbers)
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    while p == "placeholder": # while loop that repeats the indented code afterwards forever
        try:
            x = float(input("Please enter a number to be added: "))
            if x != -999:
                y = x + y
                numbers.append(x) # adds the x variable to the list
                continue # continues with the current while loop
            elif x == -999:
                try: # checks to see if the following conditions are met. Conditions are set by the lines that have 'except' in them
                    rund = input("Would you like the answer to be rounded?") # gives the user a choice if they want to round their answer
                    if rund == "yes" or rund == "Yes": # checks if they want it to be rounded or not
                        values = int(input("How many values behind 0 would you like to round it to?"))
                        z = round(y,values) # rounds the answer and stores the rounded answer inside of a new variable
                        print(*numbers,sep=" + ",end='') # prints the list in correct formatting without brackets and seperates each value
                        print(" = " + str(z)) # outputs the rounded answer on the same line as the equation
                        break # breaks out of the loop ending the while loop and continuing on with the actual code
                    elif rund == "no" or rund == "No": # checks to see if the user doesn't want to round their answer
                        print(*numbers, sep=" + ",end='') 
                        print(" = " + str(y)) # outputs the non-rounded answer on the same line as the equation
                        break
                    elif rund == "bee" or rund == "Bee":
                        print("Ya like jazz?")
                    elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee": # checks to see if the user printed something other than 'yes' or 'no'
                        print("That's not a yes or no answer") # tells the user that they didn't put a yes or no answer
                except ValueError: # A ValueError is when it is required to have a certain type of something but it recieves the opposite. (ex. Gives a string but requires a number)
                    print("That's not a yes or no answer")
        except ValueError:
            print("That was not a number!")


def subtraction(p,y):
    numbers = []
    y = 0
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    try:
        y = float(input("Please enter a number to be subtracted: "))
        numbers.append(y)
        while p == p:
            try:
                x = float(input("Please enter a number to be subtracted: "))
                if x != -999:
                    y = y - x
                    numbers.append(x)
                    continue
                elif x == -999:
                    try:
                        rund = input("Would you like the answer to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = int(input("How many values behind 0 would you like to round it to?"))
                            z = round(y,values)
                            print(*numbers,sep=" - ",end='')
                            print(" = " + str(z))
                            break
                        elif rund == "no" or rund == "No":
                            print(*numbers, sep=" - ",end='')
                            print(" = " + str(y))
                            break
                        elif rund == "bee" or rund == "Bee":
                            print("Ya like yazz?")
                        elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee":
                            print("That's not a yes or no answer")
                    except ValueError:
                        print("That's not a yes or no answer")
            except ValueError:
                print("That was not a number!")
    except ValueError:
        print("That was not a number!")


def multiplication():
    numbers = []
    y = 0
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    try:
        y = float(input("Please enter a number to be mutliplied: "))
        numbers.append(y)
        while p == p:
            try:
                x = float(input("Please enter a number to be multiplied: "))
                if x != -999:
                    y = y * x
                    numbers.append(x)
                    continue
                elif x == -999:
                    try:
                        rund = input("Would you like the answer to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = int(input("How many values behind 0 would you like to round it to?"))
                            z = round(y,values)
                            print(*numbers,sep=" * ",end='')
                            print(" = " + str(z))
                            break
                        elif rund == "no" or rund == "No":
                            print(*numbers, sep=" * ",end='')
                            print(" = " + str(y))
                            break
                        elif rund == "bee" or rund == "Bee":
                            print("Ya like jazz?")
                        elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee":
                            print("That's not a yes or no answer")
                    except ValueError:
                        print("That's not a yes or no answer")
            except ValueError:
                print("That was not a number!")
    except ValueError:
        print("That was not a number!")


def division():
    numbers = []
    y = 0
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    try:
        y = float(input("Please enter a number to be divided: "))
        numbers.append(y)
        while p == p:
            try:
                x = float(input("Please enter a number to be divided: "))
                if x != -999:
                    y = y / x
                    numbers.append(x)
                    continue
                elif x == -999:
                    try:
                        rund = input("Would you like the answer to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = int(input("How many values behind 0 would you like to round it to?"))
                            z = round(y,values)
                            print(*numbers,sep=" / ",end='')
                            print(" = " + str(z))
                            break
                        elif rund == "no" or rund == "No":
                            print(*numbers, sep=" / ",end='')
                            print(" = " + str(y))
                            break
                        elif rund == "bee" or rund == "Bee":
                            print("Ya like yazz?")
                        elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee":
                            print("That's not a yes or no answer")
                    except ValueError:
                        print("That's not a yes or no answer")
            except ValueError:
                print("That was not a number!")
    except ValueError:
        print("That was not a number!")


def squaring():
    try:
        x = float(input("Please enter the number to be squared: "))
        try:
            y = x * x
            rund = "p"
            try:
                rund = input("Would you like your output to be rounded?")
                if rund == "yes" or rund == "Yes":
                    values = -1
                    while values < 0:
                        values = int(input("How many values behind 0 would you like it to be rounded to?"))
                        y = round(y,values)
                        print('{0}^2 = {1}'.format(x,y))
                elif rund == "no" or rund == "No":
                    print('{0}^2 = {1}'.format(x,y))
                elif rund == "bee" or rund == "Bee":
                    print("Ya like yazz?")
                elif rund != "no" or rund != "No" or rund != "yes" or rund != "Yes" or rund != "bee" or rund != "Bee":
                    print("it's a yes or no answer please try again with a proper answer")
            except ValueError:
                print("That wasn't an option, please try again")
        except ValueError:
            print("That wasn't an option, please try again")
    except ValueError:
        print("That wasn't an option, please try again")


def square_root():
    try:
        x = float(input("Please enter the number to square rooted: "))
        try:
            y = math.sqrt(x) # this is one equation that importing math at the very top allows you to do that you wouldn't be able to do normally. 
            rund = "p"
            try:
                rund = input("Would you like your output to be rounded?")
                if rund == "yes" or rund == "Yes":
                    values = -1
                    while values < 0:
                        values = int(input("How many values behind 0 would you like it to be rounded to?"))
                        y = round(y,values)
                        print('{0}^2 = {1}'.format(x,y))
                elif rund == "no" or rund == "No":
                    print('{0}^2 = {1}'.format(x,y))
                elif rund == "bee" or rund == "Bee":
                    print("01011001 01100001 00100000 01101100 01101001 01101011 01100101 00100000 01101010 01100001 01111010 01111010 00111111")
                elif rund != "no" or rund != "No" or rund != "yes" or rund != "Yes":
                    print("it's a yes or no answer please try again with a proper answer")
            except ValueError:
                print("That wasn't an option, please try again")
        except ValueError:
            print("That wasn't an option, please try again")
    except ValueError:
        print("That wasn't an option, please try again")


def exponential_equation():
    try:
        x = float(input("Please input your number: "))
        c = int(input("Please input your exponent: "))
        y = x ** c
        rund = "p"
        try:
            rund = input("Would you like your output to be rounded?")
            if rund == "yes" or rund == "Yes":
                values = -1
                while values < 0:
                    try:
                        values = int(input("How many values behind 0 would you like it to be rounded to?"))
                        y = round(y,values)
                        print('{0}^{1} = {2}'.format(x,c,y))
                    except ValueError:
                        print("invalid option, please restart program and try again")
            elif rund == "no" or rund == "No":
                print('{0}^{1} = {2}'.format(x,c,y))
            elif rund == "bee" or rund == "Bee":
                print("01011001 01100001 00100000 01101100 01101001 01101011 01100101 00100000 01101010 01100001 01111010 01111010 00111111")
            elif rund != "no" or rund != "No" or rund != "yes" or rund != "Yes" or rund != "bee" or rund != "Bee":
                    print("it's a yes or no answer please try again with a proper answer")
        except ValueError:
            print("That wasn't an option, please try again")
    except ValueError:
        print("That wasn't an option, please try again")


def pythagorean_theorem():
    try:
        print("a \nb \nc ")
        varr = input("What side are you trying to solve for? ")
        if varr == "c":
            try:
                a = float(input("Please enter the value for 'a': "))
                try:
                    b = float(input("Please enter the value for 'b': "))
                    aa = a*a
                    bb = b*b
                    ab = aa+bb
                    c = math.sqrt(ab) # another reason we had import math. You cannot squareroot an equation without it
                    rund = "p"
                    try:
                        rund = input("Would you like your output to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = -1
                            while values < 0:
                                values = int(input("How many values behind 0 would you like it to be rounded to?"))
                                c = round(c,values)
                                print('√({0}^2 + {1}^2) = {2}'.format(a,b,c))
                        elif rund == "no" or rund == "No":
                            print('√({0}^2 + {1}^2) = {2}'.format(a,b,c))
                            try:
                                solving = input("Would you like to see the process of equations?")
                                if solving == "Yes" or solving == "yes":
                                    print("a = " + str(a))
                                    print("b = " + str(b))
                                    print("To solve this, you need to square both your values and get: (" + str(a) + "^2 + " + str(b) + "^2) = (" + str(aa) + " + " + str(bb) + str(")"))
                                    print("Next add both the values together and get: " + "(" + str(aa) + " + " + str(bb) + ") = " + str(ab))
                                    print("Finally, you need to square root whatever value you got and get: √" + str(ab) + " = " + str(c))
                                if solving != "Yes" and solving != "yes" and solving != "No" and solving != "no":
                                    print("Invalid answer. It is a yes or no question, please try again")
                            except ValueError:
                                print("Invalid answer. It is a yes or no question, please try again")
                        elif rund == "bee" or rund == "Bee":
                            print("Ya like jazz?")
                        elif rund != "no" or rund != "No" or rund != "yes" or rund != "Yes" or rund != "bee" or rund != "Bee":
                            print("it's a yes or no answer please try again with a proper answer")
                    except ValueError:
                        print("That wasn't an option, please try again")
                except ValueError:
                    print("That wasn't an option, please try again")
            except ValueError:
                print("That wasn't an option, please try again")
        if varr == "b":
            try:
                a = float(input("Please enter the value for 'a': "))
                try:
                    c = float(input("Please enter the value for 'c': "))
                    aa = a*a
                    cc = c*c
                    ac = cc - aa
                    b = math.sqrt(ac) # another reason we had import math. You cannot squareroot an equation without it
                    rund = "p"
                    try:
                        rund = input("Would you like your output to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = -1
                            while values < 0:
                                values = int(input("How many values behind 0 would you like it to be rounded to?"))
                                bro = round(b,values)
                                print('√({0}^2 + b^2) = {1}'.format(a,c))
                                print("b = {0}".format(bro))
                        elif rund == "no" or rund == "No":
                            print('√({0}^2 + b^2) = {1}'.format(a,c))
                            print("b = {0}".format(b))
                        elif rund == "bee" or rund == "Bee":
                            print("Ya like jazz?")
                        elif rund != "no" or rund != "No" or rund != "yes" or rund != "Yes" or rund != "bee" or rund != "Bee":
                            print("it's a yes or no answer please try again with a proper answer")
                        try:
                            solving = input("Would you like to see the process of equations?")
                            if solving == "Yes" or solving == "yes":
                                print("a = " + str(a))
                                print("c = " + str(c))
                                print("To solve this, you need to square both your values and get: (" + str(a) + "^2 + " + str(c) + "^2) = (" + str(aa) + " + " + str(cc) + str(")"))
                                print("Next subtract your a value from both sides to get: (" + str(a) + " - " + str(c) + " = " + str(ac))
                                print("Finally, you need to square root whatever value you got and get: √" + str(ac) + " = " + str(b))
                            if solving != "Yes" and solving != "yes" and solving != "No" and solving != "no":
                                print("Invalid answer. It is a yes or no question, please try again")
                        except ValueError:
                            print("Invalid answer. It is a yes or no question, please try again")
                    except ValueError:
                        print("That wasn't an option, please try again")
                except ValueError:
                    print("That wasn't an option, please try again")
            except ValueError:
                print("That wasn't an option, please try again")
        if varr == "a":
            try:
                b = float(input("Please enter the value for 'b': "))
                try:
                    c = float(input("Please enter the value for 'c': "))
                    bb = b*b
                    cc = c*c
                    bc = cc - bb
                    a = math.sqrt(bc) # another reason we had import math. You cannot squareroot an equation without it
                    rund = "p"
                    try:
                        rund = input("Would you like your output to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = -1
                            while values < 0:
                                values = int(input("How many values behind 0 would you like it to be rounded to?"))
                                aro = round(a,values)
                                print('√(a^2 + {0}^2) = {1}'.format(b,c))
                                print("a = {0}".format(aro))
                        elif rund == "no" or rund == "No":
                            print('√(a^2 + {0}^2) = {1}'.format(a,c))
                            print("a = {0}".format(a))
                        elif rund == "bee" or rund == "Bee":
                            print("Ya like jazz?")
                        elif rund != "no" or rund != "No" or rund != "yes" or rund != "Yes" or rund != "bee" or rund != "Bee":
                            print("it's a yes or no answer please try again with a proper answer")
                        try:
                            solving = input("Would you like to see the process of equations?")
                            if solving == "Yes" or solving == "yes":
                                print("a = " + str(a))
                                print("c = " + str(c))
                                print("To solve this, you need to square both your values and get: (" + str(a) + "^2 + " + str(c) + "^2) = (" + str(aa) + " + " + str(cc) + str(")"))
                                print("Next subtract your a value from both sides to get: (" + str(a) + " - " + str(c) + " = " + str(ac))
                                print("Finally, you need to square root whatever value you got and get: √" + str(ac) + " = " + str(b))
                            if solving != "Yes" and solving != "yes" and solving != "No" and solving != "no":
                                print("Invalid answer. It is a yes or no question, please try again")
                        except ValueError:
                            print("Invalid answer. It is a yes or no question, please try again")
                    except ValueError:
                        print("That wasn't an option, please try again")
                except ValueError:
                    print("That wasn't an option, please try again")
            except ValueError:
                print("That wasn't an option, please try again")

    except ValueError:
        print("That wasn't an option, please try again")

def trigonomic_and_angular_functions():
    print("-----------------------------------------------------") #code to seperate main equation choices so to make it easier to focus on these
    print("1. sine \n2. cosine \n3. tangent \n4. radians \n5. degrees \n6. hypotenuse \n") #list of all the different supported trigonomic and angular equations. \n tells the program from that point on to print on a differnet line
    
    #code for all the side angles
    try:    
        a = int(input("Please enter the degree of a (opposite). (If there isn't one then put 1)"))
        a = math.pi/a
        try:
            b = int(input("Please enter the degree of b (adjacent). (If there isn't one then put 1)"))
            try:
                h = int(input("Please enter the degree of h (hypotenuse). (If there isn't one then put 1)"))
                try:
                    choice1 = int(input("What kind of Trigonomic function do you want? "))
                    
                    if choice1 == 1: #code for sine trigonomic functions
                        print ("The value of sine of pi/6 is : ", end="") 
                        print(math.sin(a)) #another reason we have import math as you cannot do this without it
                    
                    if choice1 == 2: #code for cosine trigonomic functions
                        print ("The value of cosine of pi/6 is : ", end="") 
                        print (math.cos(a)) #another reason we have import math as you cannot do this without it
                    
                    if choice1 == 3: #code for tangent trigonomic functions
                        print ("The value of tangent of pi/6 is : ", end="") 
                        print (math.tan(a)) #another reason we have import math as you cannot do this without it
                    
                    if choice1 == 4: #code for degree angular functions
                        print ("The converted value from radians to degrees is : ", end="") 
                        print (math.degrees(a)) #another reason we have import math as you cannot do this without it
                    
                    if choice1 == 5: #code for radians angular functions
                        print ("The converted value from degrees to radians is : ", end="") 
                        print (math.radians(b)) #another reason we have import math as you cannot do this without it
                    
                    if choice1 == 6: #code for hypotenuse trigonomic functions
                        print ("The value of hypotenuse of 3 and 4 is : ", end="") 
                        print (math.hypot(b,h)) #another reason we have import math as you cannot do this without it
                except ValueError:
                    print("That wasn't an option, please try again")
            except ValueError:
              print("That wasn't an option, please try again")
        except ValueError:
            print("That wasn't an option, please try again")
    except ValueError:
        print("That wasn't an option, please try again")
        
        
def midpoint():
    try:
        x = float(input("What is your first x value? "))
        try: 
            y = float(input("What is your first y value? "))
            try: 
                x2 = float(input("What is your second x value? "))
                try:
                    y2 = float(input("What is your second y value? "))
                    x3 = x + x2
                    y3 = y + y2
                    x4 = x3/2 
                    y4 = y3/2
                    print("The midpoint of the two coordinate pairs is: (" + str(x4) + " , " + str(y4) + ")")
                    try:
                        solving = input("Would you like to see the process of equations?")
                        if solving == "Yes" or solving == "yes":
                            print("-----------------------------------------------------") 
                            print("To solve for m point, you have the equation m = (x1 + x2) / 2 and (y1 + y2) / 2")
                            print("To solve for x, subsitute in your x values to get m = (" + str(x) + " + " + str(x2) + " ) /2")
                            print("Solving the x's subsituted equation, you would get: " + str(x3) + " /2")
                            print("Solving that would give you " + str(x4) + " for the x value of the midpoint!")
                            print("Solving for the y value would be the same process but instead of the x values, it would be the y values such as...")
                            print("To solve for y, subsitute in your y values to get m = (" + str(y) + " + " + str(y2) + " ) /2")
                            print("Solving the y's subsituted equation, you would get: " + str(y3) + " /2")
                            print("Solving that would give you " + str(y4) + " for the y value of the midpoint!")
                            print("Giving you the coordinate pair of (" + str(x4) + " , " + str(y4) + ") for your midpoint")
                            print("-----------------------------------------------------") 
                        elif solving == "bee" or solving == "Bee":
                            print("Ya like jazz?")
                        elif solving != "Yes" or solving != "yes" or solving != "No" or solving != "no" or solving != "bee" or solving != "Bee":
                            print("That isn't a valid option. It's a Yes or No question")
                    except ValueError:
                        print("That isn't a valid option. It's a Yes or No question")
                except ValueError:
                    print("That isn't a valid coordinate!")
            except ValueError:
                print("That isn't a valid coordinate!")
        except ValueError:
            print("That isn't a valid coordinate!")
    except ValueError:
        print("That isn't a valid coordinate!")
        
        
def distance():
    try:
        x = int(input("What is your given first x value? "))
        try:
            y = int(input("What is your given first y value? "))
            try:
                x1 = int(input("What is your given second x value? "))
                try:
                    y1 = int(input("What is your given second y value? "))
                    n1 = x1 - x
                    m1 = y1 - y
                    n2 = n1 ** 2
                    m2 = m1 ** 2
                    nm = n2 + m2
                    s = math.sqrt(nm)
                    try:
                        rund = input("Would you like your output to be rounded?")
                        if rund == "yes" or rund == "Yes":
                            values = -1
                            while values < 0:
                                values = int(input("How many values behind 0 would you like it to be rounded to?"))
                                c = round(s,values)
                                print('√({0}-{1}^2) + ({2}-{3}^2) = {4}'.format(x1,x,y1,y,c))
                                try:
                                    solving = input("Would you like to see the process of equations?")
                                    if solving == "Yes" or solving == "yes":
                                        print("-----------------------------------------------------") 
                                        print("First, you must subtract x2 from x1 so you'd get: {0} - {1} = {2}".format(x1,x,n1))
                                        print("Secondly, do the same process for the y values: {0} - {1} = {2}".format(y1,y,m1))
                                        print("Next, square both values: {0}^2 = {1} | {2}^2 = {3}".format(n1,n2,m1,m2))
                                        print("Afterwards, add both values: {0} + {1} = {2}".format(n2,m2,nm))
                                        print("Lastly, squareroot your value to get your answer: √{0} = {1}".format(nm,s))
                                        print("Putting it into your simplified form would give you: {0} = {1}".format(s,c))
                                        print("-----------------------------------------------------") 
                                    elif solving != "Yes" or solving != "yes" or solving != "No" or solving != "no":
                                        print("That isn't a valid option. It's a Yes or No question")
                                except ValueError:
                                    print("That isn't a valid option! It's a yes or no answer.")
                        elif rund == "no" or rund == "No":
                            print('√({0}-{1}^2) + ({2}-{3}^2) = {4}'.format(x1,x,y1,y,s))
                            print("The distance between the two objects is: " + str(s))
                            try:
                                solving = input("Would you like to see the process of equations?")
                                if solving == "Yes" or solving == "yes":
                                    print("-----------------------------------------------------") 
                                    print("First, you must subtract x2 from x1 so you'd get: {0} - {1} = {2}".format(x1,x,n1))
                                    print("Secondly, do the same process for the y values: {0} - {1} = {2}".format(y1,y,m1))
                                    print("Next, square both values: {0}^2 = {1} | {2}^2 = {3}".format(n1,n2,m1,m2))
                                    print("Afterwards, add both values: {0} + {1} = {2}".format(n2,m2,nm))
                                    print("Lastly, squareroot your value to get your answer: √{0} = {1}".format(nm,s))
                                    print("-----------------------------------------------------") 
                                elif solving != "Yes" or solving != "yes" or solving != "No" or solving != "no":
                                    print("That isn't a valid option. It's a Yes or No question")
                            except ValueError:
                                print("That isn't a valid option! It's a yes or no answer.")
                        elif rund == "bee" or rund == "Bee":
                            print("01011001 01100001 00100000 01101100 01101001 01101011 01100101 00100000 01101010 01100001 01111010 01111010 00111111")
                        elif rund!= "no" or rund != "No" or rund != "yes" or rund != "Yes" or rund != "bee" or rund != "Bee":
                            print("That isn't a valid option! It's a yes or no answer.")
                    except ValueError:
                        print("That isn't a valid option! It's a yes or no answer.")
                except ValueError:
                    print("That isn't a valid coordinate!")
            except ValueError:
                print("That isn't a valid coordinate!")
        except ValueError:
            print("That isn't a valid coordinate!")
    except ValueError:
        print("That isn't a valid coordinate!")
        
        
def endpoint():
    try:
        x = float(input("What is your given endpoint x value? "))
        try:
            y = float(input("What is your given endpoint y value? "))
            try:
                x1 = float(input("What is your given midpoint x value? "))
                try:
                    y1 = float(input("What is your given midpoint y value? "))
                    n1 = x1 * 2
                    x2 = x * -1
                    n2 = n1 + x2
                    m1 = y1 * 2
                    y2 = y * -1
                    m2 = n1 + y2
                    print("The endpoint's coordinates are: (" + str(n2) + " , " + str(m2) + " ) ")
                except ValueError:
                    print("That isn't a valid coordinate!")
            except ValueError:
                print("That isn't a valid coordinate!")
        except ValueError:
            print("That isn't a valid coordinate!")
    except ValueError:
        print("That isn't a valid coordinate!")
        
        
def Linear():
    try:
        a = float(input("What is your given 'a' value? "))
        try:
            b = float(input("What is your given 'b' value? "))
            try:
                c = float(input("What is your given 'c' value? "))
                a1 = a + b
                c1 = c - a1
                print("x = " + str(c1))
            except ValueError:
                print("That is not a number!")
        except ValueError:
            print("That is not a number!")
    except ValueError:
        print("That is not a number!")


def modulus():
    try:
        a = float(input("What is your first number? "))
        try:
            b = float(input("What is the number you would like to divide by? "))
            a1 = a % b
            a2 = a / b
            print("The remainder to the expression: " + str(a) + " % " + str(b) + " = "  + str(a1))
        except ValueError:
            print("That is not a number!")
    except ValueError:
        print("That is not a number!")
        
def mean():
    numbers = []
    v = 0
    y = 0
    p = "placeholder"
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    while p == "placeholder":
        try:
            x = float(input("Please enter a number to be added: "))
            if x != -999:
                y = x + y
                v = v + 1
                numbers.append(x)
            elif x == -999:
                try:
                    rund = input("Would you like the answer to be rounded?")
                    if rund == "yes" or rund == "Yes":
                        sorted(numbers)
                        l = statistics.mean(numbers)
                        try:
                            p = int(input("How many values behind 0 would you like to round to?"))
                            l = round(l,p)
                        except ValueError:
                            print("That was not a number!")
                        print(*numbers,sep=" + ",end='')
                        print(" = " + str(l))
                    elif rund == "no" or rund == "No":
                        sorted(numbers)
                        l = statistics.mean(numbers)
                        print(*numbers,sep=" + ",end='')
                        print(" = " + str(l))
                    elif rund == "bee" or rund == "Bee":
                        print("Ya like jazz?")
                    elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee":
                        print("That's not a yes or no answer")
                    p = "stop"
                except ValueError:
                    print("That's not a yes or no answer")
        except ValueError:
            print("That was not a number!")

def median():
    numbers = []
    v = 0
    y = 0
    p = "placeholder"
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    while p == "placeholder":
        try:
            x = float(input("Please enter a number to be added: "))
            if x != -999:
                y = x + y
                v = v + 1
                numbers.append(x)
            elif x == -999:
                try:
                    rund = input("Would you like the answer to be rounded?")
                    if rund == "yes" or rund == "Yes":
                        sorted(numbers)
                        l = statistics.median(numbers)
                        try:
                            p = int(input("How many values behind 0 would you like to round to?"))
                            l = round(l,p)
                        except ValueError:
                            print("That was not a number!")
                        print(*numbers,sep=" , ",end='')
                        print(" = " + str(l))
                    elif rund == "no" or rund == "No":
                        sorted(numbers)
                        l = statistics.median(numbers)
                        print(*numbers,sep=" , ",end='')
                        print(" = " + str(l))
                    elif rund == "bee" or rund == "Bee":
                        print("Ya like jazz?")
                    elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee":
                        print("That's not a yes or no answer")
                    p = "stop"
                except ValueError:
                    print("That's not a yes or no answer")
        except ValueError:
            print("That was not a number!")

def mode():
    numbers = []
    v = 0
    y = 0
    p = "placeholder"
    print("Please enter the number '-999' if you are finished including numbers to the process of equations")
    while p == "placeholder":
        try:
            x = float(input("Please enter a number to be added: "))
            if x != -999:
                y = x + y
                v = v + 1
                numbers.append(x)
            elif x == -999:
                try:
                    rund = input("Would you like the answer to be rounded?")
                    if rund == "yes" or rund == "Yes":
                        sorted(numbers)
                        l = statistics.mode(numbers)
                        try:
                            p = int(input("How many values behind 0 would you like to round to?"))
                            l = round(l,p)
                        except ValueError:
                            print("That was not a number!")
                        print(*numbers,sep=" , ",end='')
                        print(" = " + str(l))
                    elif rund == "no" or rund == "No":
                        sorted(numbers)
                        l = statistics.mode(numbers)
                        print(*numbers,sep=" , ",end='')
                        print(" = " + str(l))
                    elif rund == "bee" or rund == "Bee":
                        print("Ya like jazz?")
                    elif rund != "no" or rund != "No" or rund != "Yes" or rund != "yes" or rund != "bee" or rund != "Bee":
                        print("That's not a yes or no answer")
                    p = "stop"
                except ValueError:
                    print("That's not a yes or no answer")
        except ValueError:
            print("That was not a number!")

def circle():
    print("C=πr^2")
    print("π=3.14")
    try:
        radius=float(input("What is the radius of the circle? "))
        r = radius**2
        pr = r*3.14
        unit=input("What is the unit of measurement? ")
        print("C=πr^2")
        print("C=" + str(pr) + str(unit) + "^2")
    except ValueError:
        print("That was not a number!")

def paralellogram():
    print("Area of a paralellogram: A=bh")
    try:
        b = float(input("What is the base of the paralellogram? "))
        try:
            h = float(input("What is the height of the paralellogram? "))
            a = b*h
            print("A = " + str(b) + " x " + str(h) + " = " + str(a))
        except ValueError:
            print("That waqsn't a number!")
    except ValueError:
        print("That wasn't a number!")

def trapezium():
    print("Area of a trapezium: A = ((a+b)/2)h")
    try:
        a = float(input("What is the value of the top base of the trapezium? "))
        try:
            b = float(input("What is the value of the bottom base of the trapezium? "))
            try:
                h = float(input("What is the height of the trapezium? "))
                ab = a+b
                abc = ab / 2
                ar = abc * h
                print(str(ar) + " = ((" + str(a) + " + " + str(b) + ")/2)" + str(h))
            except ValueError:
                print("That wasn't a number!")
        except ValueError:
            print("That wasn't a number!")
    except ValueError:
        print("That wasn't a number!")

def ellipse():
    pi = 3.14
    print("Area of an ellipse: A = πab")
    try:
        a = float(input("What is your a value? "))
        try:
            b = float(input("What is your b value? "))
            ar = pi * a * b
            print(str(ar) + " = " + str(pi) + " * " + str(a) + " * " + str(b))
        except ValueError:
            print("That wasn't a number!")
    except ValueError:
        print("That wasn't a number!")

def triangle():
        print("Area of a triangle: A = (bh)/2")
        try:
            b = float(input("What is the base of the triangle? "))
            try:
                h = float(input("What is the height of the triangle? "))
                bh = b*h
                a = bh / 2
                print("A = (" + str(a) + " x " + str(h) + ")/2 = " + str(a))
            except ValueError:
                print("That wasn't a number!")
        except ValueError:
            print("That wasn't a number!")

def nrotation():
    try:
        direction = int(input("1. Counter-Clockwise rotation \n2. Clockwise rotaton "))
        if direction == 1:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = y * -1
                    coordinatey = x
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction == 2:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = y
                    coordinatey = x * -1
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction != 1 or direction != 2:
            print("Invalid option")
    except ValueError:
        print("That was not an option!")

def orotation():
    try:
        direction = int(input("1. Counter-Clockwise rotation \n2. Clockwise rotaton "))
        if direction == 1:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = x * -1
                    coordinatey = y * -1
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction == 2:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = x * -1
                    coordinatey = y * -1
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction != 1 or direction != 2:
            print("Invalid option")
    except ValueError:
        print("That was not an option!")

def twrotation():
    try:
        direction = int(input("1. Counter-Clockwise rotation \n2. Clockwise rotaton "))
        if direction == 1:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = y
                    coordinatey = x * -1
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction == 2:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = y * -1
                    coordinatey = x
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction != 1 or direction != 2:
            print("Invalid option")
    except ValueError:
        print("That was not an option!")

def throtation():
    try:
        direction = int(input("1. Counter-Clockwise rotation \n2. Clockwise rotaton "))
        if direction == 1:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = x
                    coordinatey = y
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction == 2:
            try:
                x = float(input("What is the position of the x value? "))
                try:
                    y = float(input("What is the position of the y value? "))
                    coordinatex = x
                    coordinatey = y
                    print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                except ValueError:
                    print("That was not a number!")
            except ValueError:
                print("That was not a number!")
        if direction != 1 or direction != 2:
            print("Invalid option")
    except ValueError:
        print("That was not an option!")

def xaxis():
    try:
        coordinatex = float(input("What is your x coordinate?"))
        try:
            y = float(input("What is your y coordinate?"))
            coordinatey = y * -1
            print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
        except ValueError:
            print("That isn't a number!")
    except ValueError:
        print("That isn't a number!")

def yaxis():
    try:
        x = float(input("What is your x coordinate?"))
        try:
            coordinatey = float(input("What is your y coordinate?"))
            coordinatex = x * -1
            print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
        except ValueError:
            print("That isn't a number!")
    except ValueError:
        print("That isn't a number!")

def yex():
    try:
        coordinatey = float(input("What is your x coordinate?"))
        try:
            coordinatex = float(input("What is your y coordinate?"))
            print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
        except ValueError:
            print("That isn't a number!")
    except ValueError:
        print("That isn't a number!")

def tto():
    try:
        x = float(input("What is your x coordinate?"))
        try:
            y = float(input("What is your y coordinate?"))
            coordinatey = y * -1
            coordinatex = y * -1
            print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
        except ValueError:
            print("That isn't a number!")
    except ValueError:
        print("That isn't a number!")


def initial_velocity():
    g = 9.81
    print("Vi = √(gx)/(sin(2θ))")
    #gravitational constant is always 9.81
    #x is the distance
    #θ or Theta is always the angle
    #Vi is always initial Velocity
    try:
        x = float(input("What is the distance of the object? "))
        try:
            th = float(input("What was the degree of your launch angle? "))
            gx = g * x
            t = th * 2
            st = math.sin(math.radians(t))
            sq = gx / st
            vi = math.sqrt(sq)
            print(str(vi) + " = " + "√(" + str(g) + "*" + str(x) + ")/(sin(2(" + str(th) + "))")
        except ValueError:
            print("That wasn't a number!")
    except ValueError:
        print("That wasn't a number!")

def dilation():
    try:
        decision = int(input("1. Shrink \n2. Grow"))
        if decision == 1:
            try:
                x = float(input("What is your x coordinate?"))
                try:
                    y = float(input("What is your y coordinate?"))
                    try:
                        shrink = float(input("How much is the shape shrinking by? "))
                        coordinatex = x / shrink
                        coordinatey = y / shrink
                        print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                    except ValueError:
                        print("That isn't a number!")
                except ValueError:
                    print("That isn't a number!")
            except ValueError:
                print("That isn't a number!")
        if decision == 2:
            try:
                x = float(input("What is your x coordinate?"))
                try:
                    y = float(input("What is your y coordinate?"))
                    try:
                        grow = float(input("How much is the shape growing by? "))
                        coordinatex = x / grow
                        coordinatey = y / grow
                        print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                    except ValueError:
                        print("That isn't a number!")
                except ValueError:
                    print("That isn't a number!")
            except ValueError:
                print("That isn't a number!")
    except ValueError:
        print("That isn't a number!")

def translation():
    try:
        x = float(input("What is the value of your x coordinate? "))
        try:
            y = float(input("What is the value of your y coordinate? "))
            try:
                l = float(input("How much are your coordinates moving left? "))
                try:
                    r = float(input("How much are your coordinates moving right? "))
                    try:
                        u = float(input("How much are your coordinates moving up? "))
                        try:
                            d = float(input("How much are your coordinates moving down? "))
                            xl = x - l
                            coordinatex = x + r
                            yd = y - d
                            coordinatey = y + u
                            print("(" + str(coordinatex) + "," + str(coordinatey) + ")")
                        except ValueError:
                            print("That wasn't a number!")
                    except ValueError:
                        print("That wasn't a number!")
                except ValueError:
                    print("That wasn't a number!")
            except ValueError:
                print("That wasn't a number!")
        except ValueError:
            print("That wasn't a number!")
    except ValueError:
        print("That wasn't a number!")

def sacube():
    try:
        length = float(input("What is the side length of the cube?"))
        x = length * 6
        print("SA = " + str(x))
    except ValueError():
        print("That wasn't a number!")

def saRp():
    try:
        height = float(input("What is the height of the prism?"))
        try:
            width = float(input("What is the width of the prism?"))
            try:
                length = float(input("What is the length of the prism?"))
                x = 2*length*height
                y = 2*height*width
                z = 2*length*width
                sa = x+y+z
                print("SA = " + str(sa))
            except ValueError():
                print("That wasn't a number!")
        except ValueError():
            print("That wasn't a number!")
    except ValueError():
        print("That wasn't a number!")

def saTp():
    try:
        bt = float(input("What is the base of the triangle?"))
        try:
            ht = float(input("What is the height of the triangle?"))
            at = bt*ht/2
            try:
                lb = float(input("What is the length of the long side of the base?"))
                ab = bt*lb
                try:
                    wb = float(input("What is the side length of the short side of the small rectangles?"))
                    asb = lb * wb
                    sa = (at * 2) + (ab * 2) + (asb * 2)
                    print("SA = " + str(sa))
                except ValueError():
                    print("That isn't a number!")
            except ValueError():
                print("That isn't a number!")
        except ValueError():
            print("That isn't a number!")
    except ValueError():
        print("That was't a number!")

def saC():
    pi = 3.14
    try:
        r = float(input("What is the radius of the circles?"))
        try:
            h = float(input("What is the height of the rectangle?"))
            s = 2*pi*r**2
            a = 2*pi*r*h
            sa = s + a
            print("SA = " + str(sa))
        except ValueError():
            print("That wasn't a number!")
    except ValueError():
        print("That wasn't a number!")

def saS():
    pi = 3.14
    try:
        r = float(input("What is the radius of the sphere?"))
        sa = 4*pi*r**2
        print("SA = " + str(sa))
    except ValueError():
        print("That wasn't a number!")

def saCo():
    pi = 3.14
    try:
        r = float(input("What is the radius of the Cone?"))
        try:
            sh = float(input("What is the slant height of the Cone?"))
            s = pi*r**2
            print(str(s))
            a = pi*r*sh
            print(str(a))
            sa = s + a
            print("SA = " + str(sa))
        except ValueError():
            print("That wasn't a number!")
    except ValueError():
        print("That wasn't a number!")

def Vcube():
    try:
        length = float(input("What is the side length of the cube?"))
        v = length**3
        print("V = " + str(v))
    except ValueError():
        print("That wasn't a number!")

def VRP():
    try:
        width = float(input("What is the width of the Prism?"))
        try:
            length = float(input("What is the length of the Prism?"))
            try:
                height = float(input("What is the height of the Prism?"))
                v = width * length * height
                print("V = " + str(v))
            except ValueError():
                print("That wasn't a number!")
        except ValueError():
            print("That wasn't a number!")
    except ValueError():
        print("That wasn't a number!")

def VC():
    try:
        r = float(input("What is the radius of the Circles?"))
        try:
            h = float(input("What is the height of the Cylinder?"))
            v = math.pi * pow(r,3) * h
            print("V = " + str(v))
        except ValueError():
            print("That wasn't a number!")
    except ValueError():
        print("That wasn't a numbr!")

def VS():
    try:
        r = float(input("What is the radius of the sphere?"))
        v = (4/3) * math.pi * pow(r,3)
        print("V = " + str(v))
    except ValueError():
        print("That wasn't a number!")

def VCo():
    try:
        r = float(input("What is the radius of the cone?"))
        try:
            h = float(input("What is the height of the cone?"))
            v = math.pi * pow(r,2) * (h/3)
        except ValueError():
            print("That wasn't a number!")
    except ValueError():
        print("That wasn't a number!")

def force():
    print("F = ma")
    #f = force
    #m = mass
    #a = acceleration
    try:
        m = float(input("What is the mass of the object? "))
        try:
            a = float(input("What is the acceleration of the object? "))
            f = m*a
            print(str(f) + " = " + str(m) + "*" + str(a))
        except ValueError:
            print("That wasn't a number!")
    except ValueError:
        print("That wasn't a number!")

def leave(): 
    messages = random.randint(0,100) #generates a random number everytime the function is called
    if messages < 49: #detects what number was generated and prints a random message out of the 3 
        print("Please come again!")
    if messages > 55:
        print("I hope you enjoyed the program!")
    if messages >= 35 and messages <=39:
        print("Have a good day!")
    if messages >= 40 and messages <=49:
        print("https://rb.gy/o2krdf")
    if messages >= 50 and messages <=55:
        print("Korn")
    
    
choice = p 
option2 = p
y = 0
noleave = p # No longer in use - Variable used for scrapped project
exit = 47
while choice != exit:
    #avaliable choice for calculations
    print("---------------------------------------------")
    print("Avaliable Subjects")
    print("1. Basic Math \n2. Algebra \n3. Geometry \n4. Physics \n5. Other") # \n tells the program to print on a different line then on
    subject = int(input("Subject: "))
    if subject == 1:
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
    if subject == 2:
        print("5. Exponential Equation \n6. Pythagorean Therorem \n7. Linear Equation \n8. Squaring \n9. Square Root \n10. Modulus")
    if subject == 3:
        print("1. Trigonomic and angular functions \n2. Normal equations \n3. Area \n4. Data Analysis \n5.Transformations \n6. Surface Area \n7. Volume")
        choice2 = int(input("What type of geometry would you like? "))
        if choice2 == 1:
            print("11. Trigonomic and angular functions")
        if choice2 == 2:
            print("12. Mid-point \n13. End-point \n14. Distance Formula")
        if choice2 == 3:
            print("15. Circle \n16.Triangle \n17.Parallelogram \n18.Trapezium \n19.Ellipse")
        if choice2 == 4:
            print("20. Mean \n21. Median \n22. Mode")
        if choice2 == 5:
            print("1. Rotations \n2. Reflections \n3. Dilations \n4. Translations")
            choice3 = int(input("Which transformation would you like?"))
            if choice3 == 1:
                print("23. 90 degrees rotaton \n24. 180 degrees rotaton \n25. 270 degrees rotation \n26. 360 degrees rotation")
            if choice3 == 2:
                print("27. Over the x-axis \n28. Over the y-axis \n29. Over the line y=x \n30. Through the origin")
            if choice3 == 3:
                print("31. Dilations")
            if choice3 == 4:
                print("32. Translations")
        if choice2 == 6:
            print("33. Sphere \n34 Cube \n35. Rectangular Prism \n36. Cynlinder \n37. Triangular Prism \n38. Cone")
        if choice2 == 7:
            print("39. Sphere \n40. Cube \n41. Rectangular Prism \n42. Cylinder \n43. Coner")
    if subject == 4:
        print("44. Initial Velocity \n45. Force")
    if subject == 5:
        print("46. Change-log \n47. Quit")
    if choice == exit:
        print("Alright, come back again sometime!")
        break
        exit()
    
    try:
        choice = int(input("Your Option: "))
        p = "placeholder"
        #script for addition
        
        if choice == 1:
            print("---------------------------------------------")
            addition(y,p) #The line of code that calls upon the addition process variable
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #script for subtraction
        
        if choice == 2:
            print("---------------------------------------------")
            subtraction(y,p) #the line of code that calls upon the subtraction process variable
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #script for multiplication
        
        if choice == 3:
            print("---------------------------------------------")
            multiplication() #the line of code that calls upon the multiplication process variable
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #script for division
        
        if choice == 4:
            print("---------------------------------------------")
            division() # the line of code that calls upon the division process variable
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #program for exponential equation
        
        if choice == 5:
            print("---------------------------------------------")
            exponential_equation() # the line of code that calls upon the exponential equation veriable
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #program for pythagorean theorem
        
        if choice == 6:
            print("---------------------------------------------")
            pythagorean_theorem()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #script for Linear Equations
        
        if choice == 7:
            print("---------------------------------------------")
            Linear()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #script for squaring
        
        if choice == 8:
            print("---------------------------------------------")
            squaring() # the line of code that calls upon the squaring variable (just a little shortcut for them)
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #program for square root
        
        if choice == 9:
            print("---------------------------------------------")
            square_root() # the line of code that calls upon the square root equation variable
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Modulus code
        
        if choice == 10:
            print("---------------------------------------------")
            modulus()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #trigonomic and angular functions code
        
        if choice == 11:
            print("---------------------------------------------")
            trigonomic_and_angular_functions()    
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Geometry Midpoint Code
        
        if choice == 12:
            print("---------------------------------------------")
            midpoint()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Geometry Endpoint Code
        
        if choice == 13:
            print("---------------------------------------------")
            endpoint()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Distance formula code
        
        if choice == 14:
            print("---------------------------------------------")
            distance()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Area of a Circle
        
        if choice == 15:
            circle()
            try:
                option2 = input("Wouldnt you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes":
                    continue
                elif option2 == "No" or option2 == "no":
                    choice == exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option, it is a yes or no question")
        #Area of a Triangle
        
        if choice == 16:
            triangle()
            try:
                option2 = input("Wouldnt you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes":
                    continue
                elif option2 == "No" or option2 == "no":
                    choice == exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option, it is a yes or no question")
        #Area of a Paralellogram
        
        if choice == 17:
            paralellogram()
            try:
                option2 = input("Wouldnt you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes":
                    continue
                elif option2 == "No" or option2 == "no":
                    choice == exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option, it is a yes or no question")
        #Area of a Trapezium
        
        if choice == 18:
            trapezium()
            try:
                option2 = input("Wouldnt you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes":
                    continue
                elif option2 == "No" or option2 == "no":
                    choice == exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option, it is a yes or no question")
        #Area of a Ellipse
        
        if choice == 19:
            ellipse()
            try:
                option2 = input("Wouldnt you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes":
                    continue
                elif option2 == "No" or option2 == "no":
                    choice == exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option, it is a yes or no question")
        #Mean data analysis code
        
        if choice == 20:
            print("---------------------------------------------")
            mean()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Median Data Analysis Code
        
        if choice == 21:
            print("---------------------------------------------")
            median()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Mode Data Analysis Code
        
        if choice == 22:
            print("---------------------------------------------")
            mode()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()

        #90 degree rotation
        
        if choice == 23:
            print("---------------------------------------------")
            nrotation()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()

        #180 degree rotation
        
        if choice == 24:
            print("---------------------------------------------")
            orotation()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()

        #270 degree rotation
        
        if choice == 25:
            print("---------------------------------------------")
            twrotation()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()

        #360 degree rotation
        
        if choice == 26:
            print("---------------------------------------------")
            throtation()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Over the x-axis reflection
        
        if choice == 27:
            print("---------------------------------------------")
            xaxis()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Over the y-axis reflection
        
        if choice == 28:
            print("---------------------------------------------")
            yaxis()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Over the line y=x reflection
        
        if choice == 29:
            print("---------------------------------------------")
            yex()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Through the origin reflection
        
        if choice == 30:
            print("---------------------------------------------")
            tto()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Dilations
        
        if choice == 31:
            print("---------------------------------------------")
            dilation()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Translations
        
        if choice == 32:
            print("---------------------------------------------")
            translation()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Surface Area of a Cube

        if choice == 33:
            print("---------------------------------------------")
            sacube()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Surface Area of a Rectangular Prism

        if choice == 34:
            print("---------------------------------------------")
            saRp()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Surface Area of a Rectangular Prism

        if choice == 35:
            print("---------------------------------------------")
            saTp()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Surface Area of a Cylnder

        if choice == 36:
            print("---------------------------------------------")
            saC()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Surface Area of a Sphere

        if choice == 37:
            print("---------------------------------------------")
            saS()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Surface Area of a Cone

        if choice == 38:
            print("---------------------------------------------")
            saCo()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Volume of a Cube

        if choice == 39:
            print("---------------------------------------------")
            Vcube()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Volume of a Rectangular Prism

        if choice == 40:
            print("---------------------------------------------")
            VRP()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Volume of a Cylinder

        if choice == 41:
            print("---------------------------------------------")
            VC()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Volume of a Sphere

        if choice == 42:
            print("---------------------------------------------")
            VS()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Volume of a Cone

        if choice == 43:
            print("---------------------------------------------")
            VCo()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Initial Velocity
      
        if choice == 44:
            print("---------------------------------------------")
            initial_velocity()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Force
        
        if choice == 45:
            print("---------------------------------------------")
            force()
            try:
                option2 = input("Would you like to continue using the calculator?")
                if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                    continue
                elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                    choice = exit
                    leave()
                    continue
                elif option2 == "bee" or option2 == "Bee":
                    print("Ya like Jazz?")
                elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                    print("That is an invalid option")
            except ValueError:
                print("Invalid Option. It is a yes or no question")
                exit()
        #Change-log code
    
        if choice == 46:
            print("---------------------------------------------")
            try:
                print("VERSIONS:")
                print("1. Latest Change-Log")
                print("2. Change-log")
                option1 = int(input("Which version would you like to view?"))
                if option1 == 1:
                    latest_log() # the line of code that calls upon the variable that print only the latest change log
                    try:
                        option2 = input("Would you like to continue using the calculator?")
                        if option2 == "Yes" or option2 == "yes":
                            continue
                        if option2 == "No" or option2 == "no":
                            choice = exit
                            leave()
                            continue
                    except ValueError:
                        print("Invalid Option. It is a yes or no question")
                        exit()
                if option1 == 2:
                    change_log() # the line of code that calls upon the variable that prints the entire change log
                    try:
                        option2 = input("Would you like to continue using the calculator?")
                        if option2 == "Yes" or option2 == "yes": # if the user chooses they want to continue using the calculator then it will continue the program
                            continue
                        elif option2 == "No" or option2 == "no": # if the user chooses they dont want to continue using the calculator program then it will exit the program until they run it again
                            choice = exit
                            leave()
                            continue
                        elif option2 == "bee" or option2 == "Bee":
                            print("Ya like Jazz?")
                        elif option2 != "Yes" or option2 != "yes" or option2 != "No" or option2 != "no" or option2 != "bee" or option2 != "Bee":
                            print("That is an invalid option")
                    except ValueError:
                        print("Invalid Option. It is a yes or no question")
                        exit()
            except ValueError:
                print("Invalid Option. Just enter 1 or 2 next time")
        
        #option to exit program
        
        if choice == exit:
            print("---------------------------------------------")
            leave()
            break
            exit() 

    except ValueError:
        print("---------------------------------------------")
        print("That wasn't an option, please try again")