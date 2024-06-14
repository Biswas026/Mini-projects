#create a program capable of displaying questions to the user like kbc
#use list data tyoe to store the questions and their correct answers
#Display the final amount the person is taking home
import random

#Name=input("Enter your name")
print("Let's play KBC")
question=[["What is Our national language","Hindi","English","urdu","Odia",1],
          ["What is Our national Animal","Elephant","Tiger","Zebra","Camel",2],
          ["What is Our Mother language","Hindi","English","urdu","Odia",4]]
levels=[1000,2000,5000,10000,40000,100000,320000,640000,1250000,10000000]

for i in range(0,10):
  x=random.randint(0,2);
  questions=question[x][0]
  print(questions)
  print(f"a){question[x][1]}                             b){question[x][2]}")
  print(f"c){question[x][3]}                             d){question[x][4]}")
  answer=int(input("Enter your desired option as 1,2,3,4"))
  if answer==question[x][5]:
    print(f"Your answer is correct. You won{levels[i]}")
  else:
      print("your answer is incorrect. Sorry you loose")

# you can add questions and make it as a workable program
# lessons learned 1.Fstrings 2.Random function







