import random
while True:
    choices = ["Rock","Paper","Sicssors"]
    computer= random.choice(choices)
    player = None

    while player not in choices:
        player = input("\t*** Rock,Paper,Sicssors ***\nPick your Choice: ").capitalize()
        if(player not in choices):
            print("\nYou have entered an incorrect choice \nTry Again\n")
    print("\n")
    print("You chose: ",player)
    print("\nComputer Chose:",computer)

    if player == computer:
        print("\nIts a Tie !!!")
    elif (player == "Rock" and computer == "Sicssors") or (player == "Paper" and computer == "Rock") or (player == "Sicssor" and computer == "Paper"):
        print("\nPlayer wins\n\nWell Played Good Game...!")
    else:
        print("\nComputer wins\n\nBetter Luck Next Time...!")
    play_again = input("Do yu wanna play again :(Yes or No) ?").capitalize()
    if play_again != "Yes":
        break
print("\nSee You Next time")

