import random 
#guess the number
def GuessNumber():
    numRange = int(input("Enter the range: "))
    print("You entered the range of: " , numRange)
    if numRange < 5:
        print("The range must be greater than ", numRange)
    else:
        print("Guess the number between the range of " , numRange)
        userinput  = int(input())
        random_number = random.randrange(0, numRange)
        if userinput == random_number:
            print("Yoo!!!! Your guess is correct...")
        else:
            print("Ooopsss!!! Your guess is incorrect...")
            print("The correct number is: ", random_number)
        
GuessNumber()