import random
def it(choice):
    if choice == 0:
        player = "rock"
    if choice == 1:
        player = "paper"
    if choice == 2:
        player = "scissors"
    return (player)

player0 = int(input("rock, paper or scissors? 0, 1, 2"))
player = it(player0)
print("PLAYER CHOSE", player)
cpu0 = random.randint(0, 2)
cpu = it(cpu0)
print("COMPUTER CHOSE", cpu)
if player == "rock" and cpu == "rock":
    print("IT WAS A TIE")
if player == "rock" and cpu == "paper":
    print("COMPUTER WINS")
if player == "rock" and cpu == "scissors":
    print("PLAYER WINS")

if player == "paper" and cpu == "rock":
    print("PLAYER WINS")
if player == "paper" and cpu == "paper":
    print("IT WAS A TIE")
if player == "paper" and cpu == "scissors":
    print("COMPUTER WINS")

if player == "scissors" and cpu == "rock":
    print("COMPUTER WINS")
if player == "rock" and cpu == "paper":
    print("COMPUTER WINS")
if player == "paper" and cpu == "scissors":
    print("COMPUTER WINS")
