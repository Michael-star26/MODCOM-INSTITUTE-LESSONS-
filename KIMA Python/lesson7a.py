# Apply datat types, conditional statements ,interative statements in one application/Program
# card game
# List of cards
cards=["King","Queen","Ace",]
points=0
player=input("Enter the player Name: ")
# Use loops to determine the number of times to play the game
for x in range(5):
    import random
    random.shuffle(cards)
    print("Current card is ",cards[0])
    random.shuffle(cards)
    answer=input("Guess The next Card: ")
    random.shuffle(cards)
    # check if the input is the same as the answer
    if answer==cards[0]:
        print("Correct!!!The card Was",cards[0], "You got 3 Points")
        #remove the card
        cards.remove(cards[0])

        points=points+3#Award player some points
    else:
        print("Its WronMg!!!The card Was",cards[0], "\nGood luck in the next card")
print(f"Game Over!!!. You Got {points} Points")
if points>=9:
    print("Great Work!!",player)

