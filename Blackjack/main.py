import art
import random
def blackjack():
    global player_credit
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    tokens = [50 , 100 , 200 , 500, 1000]


    print(art.logo)

    player_cards = []
    dealer_cards = []

    def serve_cards():
        """
        Serves two cards to the player and the dealer
        :return:
        """
        player_cards.extend(random.choices(cards,k= 2))
        dealer_cards.extend(random.choices(cards,k= 2))

    def clear_deck():
        """
        clear cards on both hands
        :return:
        """
        player_cards.clear()
        dealer_cards.clear()

    def check_player_hands():
        """
        check the player hands if he won by a blackjack or lost by a bust. Also adjusts the player credit
        :return: boolean
        """
        global player_credit
        player_score = sum(player_cards)
        if player_score == 21:
            print_player_stats()
            print("Blackjack! You win!")
            print(art.you_win)
            player_credit += player_bid * 2
            return False
        elif player_score > 21:
            print_player_stats()
            print("Bust!")
            print(art.you_lose)
            return False
        else:
            return True

    def check_dealer_hands():
        """
        check the dealer hands if he won by a blackjack or lost by a bust. Also adjusts the player credit
        :return: boolean
        """
        global player_credit
        dealer_score = sum(dealer_cards)
        while dealer_score < 17:
            hit(dealer_cards)
            dealer_score = sum(dealer_cards)
        if dealer_score == 21:
            reveal_dealer__hidden_card()
            print("Dealer has Blackjack")
            print(art.you_lose)
            return False
        elif dealer_score > 21:
            reveal_dealer__hidden_card()
            print("Dealer Busts!")
            print(art.you_win)
            player_credit += player_bid * 2
            return False
        else:
            return True

    def check_winner(p_cards, d_cards):
        """
        Checks the winner of the game
        :param p_cards:
        :param d_cards:
        :return:
        """
        global player_credit
        player_score = sum(p_cards)
        dealer_score = sum(d_cards)
        print(f"Your final hand: {p_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {d_cards}, final score: {dealer_score}")
        if player_score > dealer_score:
            print("You win!")
            print(art.you_win)
            player_credit += player_bid * 2

        elif player_score < dealer_score:
            print("You lose!")
            print(art.you_lose)
        else:
            print("Draw!")
            print(art.draw)
            player_credit += player_bid

    def hit(user: list):
        """
        Adds a card to the player's hand
        :param user:
        :return:
        """
        user.append(random.choice(cards))
        
    def print_player_stats():
        """
        Prints the player's cards and score
        :return:
        """
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    
    def print_dealer_stats():
        """
        Prints the dealer's first card
        :return:
        """
        print(f"Dealer's first card: {dealer_cards[0]},*hidden*")

    def  print_deck_stats():
        """
        Prints the player and dealer stats
        :return:
        """
        print_player_stats()
        print_dealer_stats()

    def reveal_dealer__hidden_card():
        """
        Reveals the dealer's hidden card
        :return:
        """
        print(f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}")

    start_game = input("Fancy a game of Blackjack? Type 'y' or 'n': ")

    game_in_session = False

    if start_game.lower() == 'y':
        game_in_session = True
        player_credit = 1000
        print("Welcome!")

    else:
        print("Goodbye")

    while game_in_session:
        clear_deck()
        serve_cards()
        player_bid = 0

        print(f"Your current credit: {player_credit}")

        player_bidding_session = True

        while player_bidding_session:
            available_tokens = [token for token in tokens if token <= player_credit]

            player_token = int(input(f"Choose a token: {available_tokens}") or 0)

            if player_token in available_tokens:
                if player_token <= player_credit:
                    player_bid += player_token
                    player_credit -= player_token
                else:
                    print("insufficient credit")
            else:
                print("Invalid token")

            if player_bid == 0:
                print("You must bid something!")
            else:
                print(f"Your current bid: {player_bid}")

                if player_credit >= player_bid:
                    bid_more = input("Would you like to bid more? Type 'y' or 'n': ")
                    if bid_more.lower() == 'y':
                        player_bidding_session = True
                    else:
                        player_bidding_session = False
                else:
                    player_bidding_session = False

        player_round = True

        dealer_round = True

        print_deck_stats()

        if check_player_hands():

            while player_round:

                hit_or_stand = input("Would you like to hit or stand? Type 'hit' or 'stand': ")

                if hit_or_stand.lower() == 'hit':
                    hit(player_cards)
                    if check_player_hands():
                        player_round = True
                        print_player_stats()
                    else:
                        print_deck_stats()
                        player_round = False
                        dealer_round = False
                elif hit_or_stand.lower() == 'stand':
                    if check_player_hands():
                        print_player_stats()
                        player_round = False
                    else:
                        print_deck_stats()
                        player_round = False
                        dealer_round = False

        if check_dealer_hands():
            while dealer_round:
                 if check_dealer_hands():
                    reveal_dealer__hidden_card()
                    check_winner(player_cards,dealer_cards)
                    dealer_round = False
                 else:
                    reveal_dealer__hidden_card()
                    dealer_round = False

        if  player_credit < 50:
            print("You have no more tokens to bid with!")
            game_in_session = False
        else:
            print(f"Your current credit: {player_credit}")
            play_again = input("Fancy another round? 'yes' 'no'?")

            if play_again.lower() == 'yes':
                print("Another round!")
                print('\n' * 20)
            else:
                print("Goodbye!")
                game_in_session = False



















          







blackjack()


















