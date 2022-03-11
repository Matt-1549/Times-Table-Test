import random
name = input("What is your name?\n\n")
times_table = int(input("Please input your times table that you want to be tested on: "))
count = 1
score = 0
while count < 11:
  multiplicative = random.randint(1,20)
  question_check = multiplicative*times_table
  print("Q", count, ":", times_table, "*", multiplicative, ":")
  question = int(input())
  if question == question_check:
    print("Correct!")
    score += 1
  else:
    print("Incorrect! It was:", question_check, "!")
  count += 1
print(name, ", You got", score, "out of 10!")
if score > 7:
  print("You are good at your times tables!")
else:
  print("You... could improve at your times tables!")