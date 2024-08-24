import random

options = ["Stone", "Paper", "Scissors"]
result = [0, 0, 0]

def selectMove():
    move = random.choice(options)
    return move

def printScore():
    print(f"Score: \nYou: {result[0]}\nCPU: {result[1]}\nDraw: {result[2]}")

def findWinner(cpu_move, user_input):
    if user_input in options:
        
        if cpu_move == user_input:
            result[2] += 1
            print("It is a draw!")
            printScore()
            
        elif user_input == "Stone":
            if cpu_move == "Scissors":
                print("You won!")
                result[0] += 1
                printScore()
            if cpu_move == "Paper":
                print("You Lost!")
                result[1] += 1
                printScore()
                
        elif user_input == "Paper":
            if cpu_move == "Stone":
                print("You won!")
                result[0] += 1
                printScore()
            if cpu_move == "Scissors":
                print("You Lost")
                result[1] += 1
                printScore()
                
        elif user_input == "Scissors":
            if cpu_move == "Paper":
                print("You won")
                result[0] += 1
                printScore()
            if cpu_move == "Stone":
                print("You Lost")
                result[1] += 1
                printScore()
    else:
        print("Invalid Input!")

def userInput():
    user_input = input("Enter your move (type \"Exit\" to end game): ")
    return user_input

if __name__ == "__main__":
    while True:    
        user_input = userInput()
        if user_input == "Exit":
            raise SystemExit("Exiting the program.")
        cpu_move = selectMove()
        print(f"CPU move: {cpu_move}")
        findWinner(cpu_move, user_input)

    