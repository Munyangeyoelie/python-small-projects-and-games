print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0
question = 0
answer = input("What does CPU stand for ? ")
if answer == "Central Processing Unit" :
    print("correct")

    score +=1 
else :
    print("Incorect")
    question +=1
answer = input("What Is the capoyal city of Rwanda? ")
if answer == "Kigali" :
    print("correct")
    score +=1 
else :
    print("Incorect")
    question -=1
answer = input("what is Biology? ")
if answer == "Biology is the study of life" :
    print("correct")
    score +=1 
else :
    print("Incorect")
    question +=1
answer = input("Who created Adam and Eve? ")
if answer == "Jesus" :
    print("correct")
    score +=1 
else :
    print("Incorect")
    question +=1
answer = input("In which year did Jesus Die? ")
if answer == "33 AC" :
    print("correct")
    score +=1 
else :
    print("Incorect")
    question +=1
answer = input("How many years did Adam live? ")
if answer == "900 ":
    print("correct")
    score +=1 
else :
    print("Incorect")
    question +=1
answer = input("What is most  beauliful in black ? ")
if answer == "People":
    print("correct")
    score +=1 
else :
    print("Incorect")
    question +=1

print("You got " + str(score) + " question coreect")
marks = score/question * 100
print("You got " + str(marks) + "%" )


