from src import Hand, Chips, Deck

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Enter your Bet: "))
        except ValueError:
            print("Please provide and integer")
        else:
            if chips.bet > chips.total:
                print(f"You dont have enough chips, you have {chips.total} chips")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand, playing=True):

    while True:
        x = input("Hit or Stand? type 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn")
            playing = False
            return playing
        else:
            print("Enter 'h' or 's' only!")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:\n")
    print(*player.cards, sep='\n')

def show_all(player, dealer):
    print("\nDealer's Hand:\n")
    print(*dealer.cards, sep='\n')
    print(f"\nDealer's Hand={dealer.value}")
    print("\nPlayer's Hand:\n")
    print(*player.cards, sep='\n')
    print(f"\nPlayer's Hand={player.value}")

def player_busts(player, dealer, chips):
    print('Player busted')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer busted')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.lose_bet()

def push(player, dealer):
    print('Dealer and Player tie!')
