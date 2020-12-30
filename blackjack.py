from src import Card, Deck, Hand, Chips
from utils import *

# GLOBAL
playing = True

# keep playing as long is player wants to play
while True:

    print("BLACKJACK GAME")

    # make and shuffle deck
    deck = Deck()
    deck.shuffle()

    # deal 2 cards to player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # deal 2 cards to dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # give chips to player, default chips=100
    player_chips = Chips()
    # ask player to bet chips
    take_bet(player_chips)
    # show cards of player and dealer
    show_some(player_hand, dealer_hand)

    # keep playing
    while playing:
        # hit or stand, wait till player stands or busts
        playing = hit_or_stand(deck, player_hand, playing)

        # show cards after player stands or hits
        show_some(player_hand, dealer_hand)

        # player bust
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    # if player stands
    if player_hand.value <=21:
        # soft check of 17 points from dealer
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        # show cards until dealer wins or busts
        show_all(player_hand, dealer_hand)

        # checking if player wins or lose
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # show amount of chips before next round
    print(f'\nPlayer total chips are at: {player_chips.total}')

    # ask player if they want to play again
    new_game = input("Do you want to play again? 'Y' or 'N': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print('Thank you for playing')
        break
