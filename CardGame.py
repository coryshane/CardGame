"""
Cory Stephens
Python Card Game
"""

import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMPUTER = 2

# I wanted two arrays to hold both the card rank/suit and another for location
# So cardLoc holds the cards position (Deck, player, computer) and deckOfCards holds the rank and suit
cardLoc = [] * NUMCARDS
deckOfCards = [] * NUMCARDS
suitName = ("Hearts", "Diamonds", "Spades", "Clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
	clearDeck()
	createDeck()
	# I removed the loop here from the original function because I had a bug where it would often give fewer than 5 cards
	assignCard(PLAYER)
	assignCard(COMPUTER)
	
	showDeck()
	print("\n\n")
	showHand(PLAYER)
	print("\n")
	showHand(COMPUTER)	
	print("\n")
	
# For createDeck, I want to run through both arrays, and create a new array filled with the rank and suit
def createDeck(): 
	index = 0
	for card in suitName:
		for rank in rankName:
			deckOfCards.insert(index, rank + " of " + card)
			index += 1
	clearDeck()
	
# Iterate through a loop 5 times to assign 5 cards to the selected player
def assignCard(player):
	index = 0
	# Added a loop inside the assignCards function itself to remove the bug assigning less than 5 cards
	while (index < 5):
		randNum = random.randint(0, NUMCARDS)
		if (cardLoc[randNum] == playerName[0]):
			cardLoc.pop(randNum)
			cardLoc.insert(randNum, playerName[player])
			index += 1

# Set the default location for every card to the deck. Aka playerName[0]
def clearDeck():
	for index in range(0, NUMCARDS):
		cardLoc.insert(index, playerName[0])
		
# showDeck currently shows all the cards created, in the deck, players hand, and computers hand. This function would never be in a real card game
def showDeck():
	print("Location of all cards")
	print("#	card	location")
	index = 0
	for card in deckOfCards:
		print(index, card, cardLoc[index])
		index += 1
    
# Go through the entire index. If the index is the same as the player being called, print the card at that index
def showHand(player):
	print("Showing "+ playerName[player] +"'s hand:")
	index = 0
	for index in range(0, NUMCARDS):
		if cardLoc[index] == playerName[player]:
			print(deckOfCards[index])
			index += 1
			
			
main()