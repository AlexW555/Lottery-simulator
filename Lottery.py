import random
counter = 0
winningNums = []

numOfTickets = int(input("How many weeks do you want to play?"))
num1 = int(input("Please enter in your first number"))
num2 = int(input("Please enter your seccond number"))
num3 = int(input("Please enter in your third number"))
num4 = int(input("Please enter in your fourth number"))
num5 = int(input("Please enter in your fifth number"))
num6 = int(input("Please enter in your sixth number"))

for i in range(numOfTickets):
    for j in range(6):
        r = random.randint(1,59)
        if r not in winningNums:
            winningNums.append(r)

    

    if num1 in winningNums:
        counter += 1
    if num2 in winningNums:
        counter += 1
    if num3 in winningNums:
        counter += 1
    if num4 in winningNums:
        counter += 1
    if num5 in winningNums:
        counter += 1
    if num6 in winningNums:
        counter += 1
    
    #print("The winning numbers were: ")
    #for i in range(len(winningNums)):
      #  print(winningNums[i])
          
    #if counter == 0:
        #print("You won nothing")

    #if counter == 1:
        #print("You won nothing")

    if counter == 2:
        print("Week: ", i+1)
        print("You won £2")

    if counter == 3:
        print("Week: ", i+1)
        print("You won £30")
        for i in range(3):
            print(".........")

    if counter == 4:
        print("Week: ", i+1)
        print("You won £140")
        for i in range(5):
            print(".........")

    if counter == 5:
        print("Week: ", i+1)
        print("You won £1750")
        for i in range(10):
            print(".........")

    if counter == 6:
        print("Week: ", i+1)
        print("You won £6317431")
        for i in range(10):
            print(".........")

    counter = 0
    winningNums.clear()

