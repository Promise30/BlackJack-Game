import random
from Blackjack_logo import blackjack_logo

def draw_card():
    """Returns a randomly selected card from deck of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def check_total(cards):
    """"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 


def compare(player_score , computer_score):
    """Compares the scores and returns a string that corresponds to the final result"""
    if player_score == computer_score:
        return "Draw"
    elif player_score == 0:
        return "You win, you have a blackjack!"
    elif computer_score == 0:
        return "You lose, Computer has a blackjack"
    elif player_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Computer went over, you win!"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose."


def play_game():
    print(blackjack_logo)
    player_cards = []
    computer_cards = []

    is_game_over = False

    # Draw 2 random cards from the deck of cards for the player and computer
    for i in range(2):
        player_cards.append(draw_card())
        computer_cards.append(draw_card())

    while not is_game_over:
        player_score = check_total(player_cards)
        computer_score = check_total(computer_cards)

        print(f" Your cards: {player_cards}, Current score: {player_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            request = input("Type 'y' to get another card, type 'n' to pass: ")
            if request == 'y':
                player_cards.append(draw_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = check_total(computer_cards)

    print(f"    Your final hand: {player_cards}, final_score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final_score: {computer_score}")
    print(compare(player_score , computer_score))

while input("Do you want to play a game of BlackJack: 'y' or 'n': ") == 'y':
    play_game()

            
