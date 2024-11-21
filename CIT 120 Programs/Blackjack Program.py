'''
Michael Porter | Completed: 9/29/2022
CIT 144 | Gray, Eric
Blackjack Program
'''

'''
This program enables the user to play digital blackjack through the use of Python programming. The user will play as "player" against an AI controlled "opponent."
The goal of blackjack is to get as close as you can to hitting a total value of 21 without going over. If you hit 21 exactly, you win, but if you go over you lose.
You can stand your deck which will end your turn for the rest of the game until all players either go over, hit 21, or stand their deck. After all players stand their hand,
the player with the greatest number wins while the lower number loses.
'''
from itertools import product #imports the intertools method from the product module
import random #imports the random module
import time
from os import linesep #imports the os method from the linesep module

global suits #defines the suits list as a global variable
global numbers #defines the numbers list as a global variable
global maxvalue
actions = ['h','s','q'] #defines the contents of the actions available to the user
suits = ['hearts', 'clubs', 'spades', 'diamonds'] #defines the different suits of the cards
numbers = set([i for i in range(2,15)]) #defines all possible card values
random.seed(time.process_time()) #sets the seed that is used in the random number generator.  This is important. Using the same number always produces the same results.  Using the process time swhich is the number of seconds from when run will guarantee random numbers
countop=0 #defines the count opponent variable later used for when both sides stay their hands
countpl=0 #dfines the count player variable later used for when both sides stay their hands
maxvalue = 52

def create_standard_deck(deck=[]): #defines the create_standard_deck function that creates the deck of cards
    suits.sort() #sorts all suits to alphabetically order the cards
    for suit in suits: 
        for number in numbers:
            card = (suit,number) #makmes both the suit and number into one card
            deck.append(card) #adds the card to the deck
    return deck #returns deck from the function

def draw_card_player(deck,player,maxvalue): #defines a function to draw a card and add it to the playere's deck
    number = random.randint(0,maxvalue)
    card = deck[number]
    deck.remove(card) #removes said card from the deck
    player.append(card) #adds said card to the player's deck
    maxvalue -= 1
    return deck,player,maxvalue #returns both the deck and player variables

def draw_card_opponent(deck,opponent,maxvalue): #same function as draw_card_player except to add a card to the opponent's deck instead
    number = random.randint(0,maxvalue)
    card = deck[number]
    deck.remove(card)
    opponent.append(card)
    maxvalue-=1
    return deck,opponent,maxvalue

def display_player(player,opponent): #defines a function that detects whether the deck in hand belongs to the player or the opponent
    if player[0] == opponent[0]: #if the first card in "player"'s deck is the same as the first card in the "opponent"'s deck
        player = "Opponent: " 
    elif player[0] != opponent[0]: #if the first card in "player"'s deck is different as the first card in the "opponent"'s deck
        player = "Player: "
    print(player) #prints which player the deck belongs to

def get_count(player): #defines a function to display the total score of a player
    value = 0 # defines an empty integer value variable
    for card in player: #goes through each card in the given deck
        if card[1] >= 10 and card[1] <=13: #detects if the card is a Jack, Queen, or King
            value+=10 #adds 10 to the total
        elif card[1] == 14: #detects if the card is an Ace
            value+=11 #adds 11 to the total
        else:
            value+= card[1] #detects if the card is not an Ace, Jack, Queen, or King. Rather just a normal number and adds that number to the total
    return value #returns the total score

def check_cards(player): #defines a function that checks and tells the player whether or not they have won, lost, or can keep going if they wish
    value = get_count(player) #gets the total score of the provided deck using the get_count() function
    if value == 21: #if the score of the deck is equal to 21, the player has won
        return "WIN" 
    elif value > 21: #if the score is greater than 21, the player has lost
        return "BUST"
    else: #if the score is not equal to or greater than 21, the game continues and the player can keep playing if they wish
        return "OK"
def hit(deck,player,opponent): #defines a function that displays all needed information if the player decides to keep playing
    display_player(player,opponent) #calls upon the display_player function to detect whether it is the Opponent or human Player's turn
    if player[0] == opponent[0]: #if the first card in "player"'s deck is the same as the first card in the "opponent"'s deck
        for card in opponent:
            print(card, end=' ')
    elif player[0] != opponent[0]: #if the first card in "player"'s deck is different as the first card in the "opponent"'s deck
        for card in player:
            print(card,end=' ')
    print(f'\n{get_count(player)}') #prints the total score of the player's deck
    print(check_cards(player)) #prints whether the player has won, lost, or can keep going

def check_winner(player, opponent):
    opcount=get_count(opponent) #grabs the opponent's total score
    print(f'Opponent: {opcount}') #prints opponent's score
    plcount=get_count(player) #grabs the player's total score
    print(f'Player: {plcount}') #prints the player's score
    if opcount < 21:
        if opcount > plcount: #declares opponent as the winner if their score is greater
            result="WIN"
            winner = "Opponent"
            game_over=True
        elif plcount > 21:
            result="WIN"
            winner="Opponent"
            game_over=True
    if plcount < 21:
        if plcount > opcount: #declares human player as the winner if their score is greater
            result="WIN"
            winner = "Player"
            game_over=True
        elif opcount > 21:
            result="WIN"
            winner="Player"
            game_over=True
    if plcount == opcount:
        result="Draw"
        winner = "None"
        game_over = "True"
    return result, winner, game_over

def create_blackjack_game(maxvalue): #defines a function that allows the start of the game and gives both player's their first two cards to start
    player=[] #defines an empty list
    opponent=[] #defines an empty list
    deck = create_standard_deck(deck=[]) #creates the deck from the returned variable in the create_standard_deck function
    for i in range(1): #repeats following indented code once
        deck,player,maxvalue=draw_card_player(deck,player,maxvalue) #removes a card from the deck and adds the card to the player's deck
        deck,opponent,maxvalue=draw_card_opponent(deck,opponent,maxvalue) #removes a card from the deck and adds the card to the opponent's deck
    hit(deck,player,opponent) #uses the hit function that displays all needed information
    print("-----") #prints a seperator line for easier readability
    hit(deck,opponent,opponent) #uses the hit function that displays all needed information for the opponent
    return deck, opponent, player,maxvalue #returns both values to the next function to start the game

def play_blackjack_game(deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue): #defines a function where the main game will take place and passes in all needed variables
    player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep) #allows the player to choose if they would like to add a card to their hand, stay their hand, or quit the game entirely
    while player_action not in ('s', 'h', 'q'): #repeats the player's choice if they do not pick any of the three options
        player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep) 
    if player_action == 'q': #if the player chooses to quit the game, the program ends
        print("Player forfeited")
        exit()
    while player_action != 'q': #if the player did not choose to quit the game
        if player_action == 'h': #if the player would like to add a card to their deck
            deck,player,maxvalue=draw_card_player(deck,player,maxvalue) #removes a card from the deck and adds it to the player's deck
            hit(deck,player,opponent) #prints all needed information
            print("-----") #divider for readability
            if check_cards(player) == "WIN" or check_cards(player)=="BUST": #if the player has won or lost, marks the game as over
                game_over=True
                if check_cards(player)=="WIN": #if the player has won the game
                    result="Win"
                elif check_cards(player)=="BUST": #if the player has lost the gamge
                    result="Lose"
                winner = "Player"
                return deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue #returns all expected values to avoid errors in program
            if get_count(opponent) < 17: #if the AI opponent's score is less than 17
                deck,opponent,maxvalue=draw_card_opponent(deck,opponent,maxvalue) #removes a card from the deck and adds it to the opponent's deck
                hit(deck,opponent,opponent) #prints all needed information fro the opponent
                print("-----") #divider
                if check_cards(opponent) == "WIN" or check_cards(opponent)=="BUST": #repeats the same process above except for the opponent instead of the player
                    game_over=True
                    if check_cards(opponent)=="WIN":
                        result="Bust"
                    elif check_cards(opponent)=="BUST":
                        result="Win"
                    winner = "Opponent"
                    return deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue #returns all expected values to avoid errors in program
            if countpl != countpl-1: #detects whether or not the player has decided to stay their hand instead
                countpl+=1
        if player_action == 's': #if the player wants to stay their hand, continues the opponent's turn until they want to stay their hand as well
            while get_count(opponent) < 17: #opponent will continue drawing cards until their score is greater than or equal to 17
                deck,opponent,maxvalue=draw_card_opponent(deck,opponent,maxvalue)
                hit(deck,opponent,opponent)
                if check_cards=="WIN"or check_cards=="BUST":
                    break
            result, winner, game_over = check_winner(player,opponent)
            return deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue
        if countop == countop-1 and countpl == countpl-1: #if both players have stayed their hand, the one with the highest value not over 21 wins
            result, winner, game_over = check_winner(player,opponent)
        return deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue

    return deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue #returns all expected values to avoid errors
winner="" #creates a blank string statement
result="" #creates a blank string statement
deck,opponent,player,maxvalue = create_blackjack_game(maxvalue) #calls upon the create_blackjack_game to setup the first stages of the game to make it playable
game_over=False #declares the game as started
while game_over != True: #will contineu the play the game until the game is declared as over and someone has lost or won
    deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue = play_blackjack_game(deck,player,opponent,countpl,countop,game_over,winner,result,maxvalue) #calls upon the play_blackjack_game to enable the main function of the game
print(f'{winner}:{result}') #prints out either Opponent or Player and whether they have Lost or Won