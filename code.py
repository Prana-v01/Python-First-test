name = input("What is your name?: ")

print("Question 1: What Two values do booleans store?: ")
print(" 1)true\n 2)false\n 3)True and false\n 4)true and False\n 5)True and False\n")

question_1 = int(input("Which number is the correct choice?: "))
score = 0
#the first question and the if statements
if question_1 == 1 or question_1 == 2:
    print("Incorrect\n","Your score is",score)
    score += 0
elif question_1 == 3 or question_1 == 4:
    print("Very close..\n","Your score is",score)
    score += 0.5
elif question_1 == question_1 == 5:
    score += 1
    print("Correct! Great job\n","Your score is",score)
else:
    print("Error")
    score = 0
#0.5 or 1 can be the score from here.

#questions
#print the options for user

#second question and the if statements
print("1)\n x = 2\n if x == x \n print(x)\n\n 2)x = 2/n if x = x:\n print(x)\n\n 3) x = 2\n if x == x:\n print(x)\n")
question_2 = input("What qualifies as an if statement?: ") # the second question
if question_2 == "1" or question_2 == "2":
    print("Wrong.")
    score += 0
elif question_2 == "3": #why does it work when i add "" around the number but when i dont it doesnt? It sure wasent the case above.
    print("correct!")
    score += 1
    print(score) #update users current score
else:
    print("error")
#the best score will be 1 from here. 0 to 2

print("If you get this correct; you will recieve 2 points. However, If incorrect... -2 points.\n Goodluck :) \n\n")
print("1) A While Loop is used to repeat a specific block of code an unknown number of times, until a condition is met\n 2)used for iterating over a sequence\n")
question_3 = input("What is a while loop?: ")

#3rd question + if statements

if question_3 == "1":
    print("Correct!")
    score += 2
    print(score)
elif question_3 == "2":
    print("Wrong!!")
    score -= 2
    print(score)
else:
    print("error")
#the best score is 2 and the worst is -2 = -2 to 4

#4th question + if statements

print("1) A foor loop repeats a specific amount\n 2) a for loop repeats only once\n 3) a for loop repeats forever.\n")
question_4 = input("What is a for loop?: ")

if question_4 == "1":
    print("correct!")
    score += 2
    print(score)
elif question_4 == "2":
    print("incorrect!")
    score -= 1
    print(score)
else:
    print("error")
    
# max score is +2 and lowest is -1
    
"""
#this is the first example of concatenation (this is usefull so i can put this into the print statements)
x = "Python is "
y = "awesome"
z =  x + y
print(z)


#this is the second example of concatenation
x = 5
y = 10
print(x + y)

#third and final example
x = 5
y = "John"
print(str(x)+ " " + y)

"""
#5th question + if statements
print("1) x = 'python'\n y = 'awesome'\n z = x + y\n print(z)\n\n 2) x = 5\n y = 10\n print(x+y)\n\n 3) x= 5\n y = 'John'\n print(str(x) + " " + y\n \n 4) All the above\n")
question_5 = input("Which one is the correct example of concatenation?: ")

if question_5 == 1 or question_5 == 2 or question_5 == 3:
    print("Incorrect.")
    score += 1
    print(score)
if question_5 == 4:
    print("correct! Great job!")
    score += 2
    print(score)
else:
    print("error")
#max score is 2 or 1.

#6th and final question + if statements
print("\n a = 2,\n b = 3\n print(b**a)\n\n 1)6\n 2)8\n 3)10\n 4)9")
question_6 = input("What will this code print? Submit your awnser: ")

if question_6 == 1 or question_6 == 2 or question_6 == 3:
    print("Incorrect.. ")
    score -= 1
    print(score)
    
if score >= 5:
    print(f"Congratulations {name} You have beat my test. More tests coming up!")
else:
    print("You have LOST the quiz. Sorry. Try again, maybe..")
    
