'''
Exercise 8: Rock Paper Scissors

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player
plays (using input), compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

'''

# Solution
user_one = input("Name of player one:")
user_two = input("Name of player two:")
while True:
    # Input 
    try:
        user_one_answer = int(input("{}, Please input your choice:\n1.Rock\n2.Scissors\n3.Paper\n".format(user_one)))
        user_two_answer = int(input("{}, Please input your choice:\n1.Rock\n2.Scissors\n3.Paper\n".format(user_two)))
        # Check input
        if user_one_answer not in range(1,4) or user_two_answer not in range(1,4):
            print("Input outrange")
            continue
    except:
        print("Input error.")
        continue
    # Compare
    if user_one_answer + 1 == user_two_answer or user_one_answer - 2 == user_two_answer:
        print("{} win!".format(user_one))
    elif user_one_answer == user_two_answer:
        print("Draw.")
    else:
        print("{} win!".format(user_two))
    # Start a new game
    try:
        if int(input("Input number 1 to star a new game, or any to exit.")) == 0:
            break
    except:
        print("Input error. Exit the game.")
        break
    
