# I created a python file which contains the questions and answers
# called this file question_data

# import the data list from question_data
from data import question_data

# print the program title     
print ("""
       QUIZ GAME\n""")

# create a variable called score and assign it to the number 0
score = 0
# let the number of dictionaries in the question_data list be 'num'
num = len (question_data)

# create a while loop which runs while num is 0
while num!=0:
    # create a for loop for the question data
    #...which represents each elements as 'question'
    for question in question_data:
        # let the value of the text key be 'text'
        text = question["text"]
        # let the value of the answer key be 'answer'
        answer = question["answer"]
# prompt the user to answer True or False and assign it to the variable 'ans'
        ans = input (f"{text}. (True/False): ").title()
# if the user's answer is the same as the answer in the dictionary....
        if ans==answer:
            # increase the score by 1 and print the next line
            score+=1
            print ("That is correct!")
        else:
# if not, print this next line
            print ("That is incorrect!")

# as the for loop runs, let the new value of num be 1 less
        num-=1
# when the loop breaks, print the total score
print (f"You scored {score} points")