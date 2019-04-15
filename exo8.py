#Make a two-layer Rock-Paper-Scissors ask for player plays (using input),
#compare them, print out a message of congratulations to the winner, and ask
#if the players want to start a new game)issors game. (Hi

c = input("PLAYER1_R or P or S:")
while not (c == "R" or c == "P" or c == "S" or c == "r" or c == "p" or c == "s"):
 c = input("Plz PLAYER1 choose R or P or S:")
d = input(" PLAYER2_R or P or S:")
while not (d == "R" or d == "P" or d == "S" or c == "r" or c == "p" or c == "s"):
 d = input(" Plz PLAYER2 choose R or P or S:")
if c == d:
     print("equal")
elif (((d == "P" or d == "p") and (c == "R" or c == "r")) or ((d == "R"or d == "r") and (c == "S"or c == "s")) or ((d == "S"or d == "s") and (c == "P" or c == "p"))):
     print("player2 is the winner")
else:
     print("player1 is the winner")




