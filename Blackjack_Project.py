# Blackjack Project 

import random
import os
os.system('cls')

# *** Blackjack House Rules ***

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
    '''Returns random card from deck.'''
    return random.choice(cards)

# Create a scoreboard to keep track of wins and loses

wins = 0
loses = 0

# Create a while loop to start the game.
# Deal the user and computer 2 cards each using deal_card() and append().

blackjack = True
while blackjack == True:
    '''Beginning of blackjack game.'''

    user_cards = []
    computer_cards = []

    user_cards.append(deal_card(user_cards))
    computer_cards.append(deal_card(computer_cards))
    user_cards.append(deal_card(user_cards))
    computer_cards.append(deal_card(computer_cards))

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    # Create a function called calculate_score() that takes a List of cards as input and returns the score. 
   
    def calculate_score(hand):
        '''Calculates the sum of all cards in specified hand.'''
        # Check for a blackjack (a hand with only 2 cards: ace + 10).
        # Return 0 instead of the actual score. 0 will represent a blackjack.
        run = True
        while run == True:
            if len(hand) == 2 and sum(hand) == 21:
                return 0
            # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
            # if score > 21 and 11 in hand:
            if sum(hand) > 21:
                if 11 in hand:   
                    hand.remove(11)
                    hand.append(1)
                    return sum(hand)
                else:
                    return sum(hand)
            else:
                return sum(hand)

    # Create a while loop to calculate the user's cards.

    user_turn = True
    while user_turn == True:
        os.system('cls')
        print(logo)
        print(f"User hand: {user_cards} \nComputer hand: [{computer_cards[0]}], [?] \nWins: {wins} \nLoses: {loses}")
        # The score will need to be rechecked with every new card drawn         
        user_score = calculate_score(user_cards)
        if user_score == 0 or user_score > 20:
            break
        hit = input("Do you want to draw another card? Type 'yes' or 'no': ")
        if hit == "yes":
            user_cards.append(deal_card(user_cards))
            calculate_score(user_cards)
        elif hit == "no":
            break
        else:
            break

    # Once the user is done, it's the computer's turn. The computer should keep 
    # drawing cards as long as it has a score less than 17.

    computer_turn = True
    while computer_turn == True:
        os.system('cls')
        print(logo)
        print(f"User hand: {user_cards} \nComputer hand: {computer_cards[0]} \nWins: {wins} \nLoses: {loses}")
        computer_score = calculate_score(computer_cards)
        if user_score == 0 or computer_score > 20:
            break
        elif computer_score < 17:
            computer_cards.append(deal_card(computer_cards))
            calculate_score(computer_cards)
        else:
            break

    # Compare scores.
    # If the user_score is over 21, then the user loses.
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), # then the user loses. If the user has a blackjack (0), then the user wins.
    # If the computer_score is over 21, then the computer loses.
    # If none of the above, then the player with the highest score wins.

    os.system('cls')
    print(logo)
    print(f"User final hand: {user_cards}")
    print(f"Computer final hand: {computer_cards}")
    if user_score > 21:
        loses += 1
        print(f"Bust, you lose! \nWins: {wins} \nLoses: {loses}")
    elif user_score == computer_score:
        print(f"Draw! \nWins: {wins} \nLoses: {loses}")
    elif computer_score == 0:
        loses += 1
        print(f"Computer got blackjack, you lose! \nWins: {wins} \nLoses: {loses}")
    elif user_score == 0:
        wins += 1
        print(f"Blackjack, you win! \nWins: {wins} \nLoses: {loses}")
    elif computer_score > 21:
        wins += 1
        print(f"Computer busts, you win! \nWins: {wins} \nLoses: {loses}")       
    elif computer_score > user_score:
        loses += 1
        print(f"You lose! \nWins: {wins} \nLoses: {loses}")
    elif user_score > computer_score:
        wins += 1
        print(f"You win! \nWins: {wins} \nLoses: {loses}")
        

    # Ask the user if they want to restart the game. If they answer yes, clear the console

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again == 'yes':
        blackjack = True
    elif play_again == 'no':
        os.system('cls')
        print(logo)
        print(f"Wins: {wins} \nLoses: {loses}")
        print(input("Thanks for playing!"))
        blackjack = False