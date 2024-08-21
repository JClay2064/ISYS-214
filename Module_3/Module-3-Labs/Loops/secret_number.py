import random
 

randomInteger = random.randint(1, 100)

print ("Welcome to guess the secret number game ")
print (" I have guessed a secret number between 1 and 100")

# Start the game
while True:
     # Ask the user to enter a Integer number
     userGuessNumber = int(input("Enter an integer number"))
     
     # Checked if guessed number is correct 
     if userGuessNumber == randomInteger:
           print ("The number was", randomInteger)
           print ("Well done, muggle! You are free now!")
           break # Exit the loop
     else:
           # If incorrect, print the message and prompt again
           print ("Ha ha, You're stuck in my loop")