import random
import os
import bj_basic_strategies as bs

# RULES:
# !!! Surrender is not allowed
# !!! Split is not allowed
# !!! Double is not allowed
# !!! Single-Deck

# Define the ranks, suits, and values of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

total_wins = 0
total_losses = 0
total_ties = 0


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to create a shuffled deck of cards
def create_deck():
    """
        Generate a deck of cards by combining the predefined ranks and suits.
        Each card is represented as a tuple (rank, suit).

        Returns:
        - deck: A shuffled deck of cards as a list of tuples.
    """

    # Initialize an empty list to store the cards in the deck
    deck = []
    # Iterate over each suit (e.g., spades, hearts, diamonds, clubs)
    for suit in suits:
        # Iterate over each rank (e.g., 2, 3, 4, ..., J, Q, K, A)
        for rank in ranks:
            # Add a tuple representing each card to the deck
            deck.append((rank, suit))
    # Shuffle the deck randomly
    random.shuffle(deck)
    return deck


# Function to hit (draw) additional cards from the deck
def hit_cards(deck, num_cards=2):
    """
        Draw a specified number of cards from the deck, representing a hit.

        Arguments:
        - deck: A list representing the deck of cards.
        - num_cards (optional): The number of cards to draw (default is 2).

        Returns:
        - hand: A list of cards drawn from the deck.
    """

    # Create a new deck when there are no cards left in the current deck.
    if len(deck) <= 2:
        deck = create_deck()
    # Initialize an empty list to store the drawn cards
    hand = []
    # Iterate for the specified number of cards
    for _ in range(num_cards):
        # Remove the last card from the deck (representing a hit)
        card = deck.pop()
        # Add the drawn card to the hand
        hand.append(card)
    return hand


# Function to hit (draw) a specific card value from the deck
def hit_card(deck, value):
    """
        Draw a specific card value from the deck, representing a hit.

        Arguments:
        - deck: A list representing the deck of cards.
        - value: The numerical value of the card to draw.

        Returns:
        - card_to_hit: The card with the specified value, or None if not found.
    """

    # Create a new deck when there are no cards left in the current deck.
    if len(deck) <= 0:
        deck = create_deck()

    # If the value is 1, it is converted to 11 to account for the Ace's value.
    if value == 1:
        value = 11

    # Initialize the card_to_hit variable as None
    card_to_hit = None
    # Iterate over each card in the deck
    for card in deck:
        # Check if the value of the card matches the specified value
        if values[card[0]] == value:
            card_to_hit = card

    return card_to_hit


# Function to calculate the value of a hand
def calculate_hand_value(hand):
    """
        Calculate the numerical value of a hand in blackjack.

        Arguments:
        - hand: A list representing the hand of cards.

        Returns:
        - value: The numerical value of the hand.
    """

    # Initialize the value of the hand to zero
    value = 0
    # Initialize the count of aces in the hand to zero
    num_aces = 0

    # Iterate over each card in the hand
    for card in hand:
        # Get the rank of the card
        rank = card[0]
        # Add the value of the card to the total hand value
        value += values[rank]
        # Check if the card is an Ace
        if rank == 'A':
            # Increment the count of aces
            num_aces += 1

    # Check if the hand value is greater than 21 and there are aces in the hand
    while value > 21 and num_aces > 0:
        # Reduce the value by 10 to change the value of an Ace from 11 to 1
        value -= 10
        # Decrement the count of aces
        num_aces -= 1

    return value


# Player's turn function
def player_turn(deck, player_hand):
    """
        Simulate the player's turn in the blackjack game.

        Arguments:
        - deck: A list representing the deck of cards.
        - player_hand: A list representing the player's hand of cards.

        Returns:
        - True if the player wins or stands, False if the player busts.
    """

    # Access the global variables for total wins and total losses
    global total_wins, total_losses

    # Continue the player's turn until the player wins, stands, or busts
    while True:
        print("\nPlayer's Hand:", player_hand)
        # Calculate the value of the player's hand
        player_value = calculate_hand_value(player_hand)
        print("Player's Hand Value:", player_value)

        # Check if the player busts (hand value exceeds 21)
        if player_value > 21:
            break

        # Prompt the player for their choice
        choice = input("Do you want to hit or stand? (h/s): ")
        # If the choice is to hit
        if choice.lower() == 'h':
            # Draw an additional card from the deck
            player_hand.extend(hit_cards(deck, num_cards=1))
        # If the choice is to stand
        elif choice.lower() == 's':
            # Return True to indicate the player's stand
            break

        print()  # Add a newline for formatting


def bot_turn(deck, bot_hand, dealer_upcard):
    bot_hand_value = calculate_hand_value(bot_hand)
    dealer_upcard_rank = dealer_upcard[0]

    if is_initial_hand_soft(bot_hand):  # soft hand
        while bs.should_hit_soft_hand(bot_hand_value, dealer_upcard_rank):
            bot_hand.extend(hit_cards(deck, num_cards=1))
            bot_hand_value = calculate_hand_value(bot_hand)
    else:  # hard hand
        while bs.should_hit_hard_hand(bot_hand_value, dealer_upcard_rank):
            bot_hand.extend(hit_cards(deck, num_cards=1))
            bot_hand_value = calculate_hand_value(bot_hand)


# Dealer's turn function
def dealer_turn(deck, dealer_hand, is_simulation=False):
    """
        Simulate the dealer's turn in the blackjack game.

        Arguments:
        - deck: A list representing the deck of cards.
        - dealer_hand: A list representing the dealer's hand of cards.
        - is_simulation (optional): Boolean indicating whether it's a simulation or not (default is False). 
                                    If it is not a simulation, 
                                    it makes the relevant prints for better presentation on playing.

        Returns:
        - None
    """

    # Calculate the value of the dealer's hand
    dealer_value = calculate_hand_value(dealer_hand)

    # If the call of the function is not from a simulation - make the relevant prints
    if not is_simulation:
        print("\nDealer's Hand:", dealer_hand)
        print("Dealer's Hand Value:", dealer_value)

    # Continue drawing cards until the dealer's hand value reaches 17 or higher
    while dealer_value < 17:
        dealer_hand.extend(hit_cards(deck, num_cards=1))
        dealer_value = calculate_hand_value(dealer_hand)

        if not is_simulation:
            print("Dealer hits!")
            print("Dealer's Hand:", dealer_hand)
            print("Dealer's Hand Value:", dealer_value)


# Function to compare hands
def compare_hands(player_hand, dealer_hand, is_simulation=False):
    """
        Compare the player's and dealer's hands to determine the outcome.

        Arguments:
        - player_hand: A list representing the player's hand of cards.
        - dealer_hand: A list representing the dealer's hand of cards.
        - is_simulation (optional): Boolean indicating whether it's a simulation or not (default is False).

        Returns:
        - None
    """
    # Access the global variables for total wins, total losses and total ties
    global total_wins, total_losses, total_ties

    # Calculate the value of the player's hand
    player_value = calculate_hand_value(player_hand)
    # Calculate the value of the dealer's hand
    dealer_value = calculate_hand_value(dealer_hand)

    if not is_simulation:
        print("\nPlayer's Hand:", player_hand)
        print("Player's Hand Value:", player_value)
        print("\nDealer's Hand:", dealer_hand)
        print("Dealer's Hand Value:", dealer_value)

    # Compare the values of the player's and dealer's hands to determine the outcome
    if player_value > dealer_value:
        if not is_simulation:
            print("Player wins!")
        # Increment the total wins counter
        total_wins += 1
    elif player_value < dealer_value:
        if not is_simulation:
            print("Dealer wins!")
        # Increment the total losses counter
        total_losses += 1
    else:
        if not is_simulation:
            print("It's a tie!")
        # Increment the total ties counter
        total_ties += 1


# Function to check if the initial hand is soft
def is_initial_hand_soft(hand):
    """
        Arguments:
        - hand: A list representing the player's or dealer's hand of cards.

        Returns:
        - True if the hand is a soft hand (contains an Ace), False otherwise.
    """

    # Iterate over each card in the hand
    for card in hand:
        # Get the rank of the card
        rank = card[0]
        if rank == 'A':
            # If the rank of the card is 'A' (Ace), return True
            return True
        else:
            # If not, return false
            return False


# Function to play the game
# This function is the main entry point for playing the game of Blackjack.
def play_game():

    global total_wins, total_losses, total_ties

    print("Welcome to Blackjack!")

    # Create a new shuffled deck
    deck = create_deck()

    while True:
        # Clear the screen for a new round
        clear_screen()

        # Deal initial cards to the player and dealer
        player_hand = hit_cards(deck, num_cards=2)
        dealer_hand = hit_cards(deck, num_cards=2)

        # Player's turn
        player_turn(deck, player_hand)
        player_hand_value = calculate_hand_value(player_hand)
        if player_hand_value > 21:
            print("Player busts! Dealer wins.")
            # Increment the total losses counter
            total_losses += 1
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                print("Thanks for playing!")
                break
            else:
                continue

        # Dealer's turn
        dealer_turn(deck, dealer_hand)
        dealer_hand_value = calculate_hand_value(dealer_hand)
        if dealer_hand_value > 21:
            print("Dealer busted! You win!")
            # Increment the total wins counter
            total_wins += 1
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                print("Thanks for playing!")
                break
            else:
                continue

        # Compare hands to determine the outcome
        compare_hands(player_hand, dealer_hand)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break


# Function to run complete game simulations using the basic strategies
def run_complete_game_simulations_with_basic_strategies(n, debug_logs=False):
    """
        Arguments:
        - n: An integer representing the number of game simulations to run.
        - debug_logs: A boolean indicating whether to print debug logs.

        Returns:
        - tuple<int, int, int, list[]> where:
            - first int is total wins.
            - second int is total losses.
            - third int is total ties.
            - list with winrates
    """

    total_wins = 0
    total_losses = 0
    total_ties = 0
    winrate = []

    deck = create_deck()
    iteration = 0
    while iteration < n:

        if (iteration > 0):
            winrate.append(total_wins/iteration)

        # Increase the iteration
        iteration += 1

        if debug_logs:  # Adding new line for formatting
            print()
            print("Iteration:" + str(iteration))

        # Hit the initial 2 cards
        bot_hand = hit_cards(deck, num_cards=2)
        dealer_hand = hit_cards(deck, num_cards=2)
        dealer_upcard = dealer_hand[0]

        # Bot's turn
        bot_turn(deck, bot_hand, dealer_upcard)
        bot_hand_value = calculate_hand_value(bot_hand)

        if debug_logs:  # Print bot's hand value
            print("Bot: " + str(bot_hand_value))

        if bot_hand_value > 21:
            if debug_logs:
                print("Bot busted! Dealer wins!")
            total_losses += 1
            continue

        # Dealer's turn
        dealer_turn(deck, dealer_hand, is_simulation=True)
        dealer_hand_value = calculate_hand_value(dealer_hand)

        if debug_logs:  # Print dealer's hand value
            print("Dealer: " + str(dealer_hand_value))

        if dealer_hand_value > 21:
            if debug_logs:
                print("Dealer busted! Bot wins!")
            total_wins += 1
            continue

        # Compare hands
        if bot_hand_value > dealer_hand_value:
            if debug_logs:
                print("Bot wins - has more hand value than dealer")
            total_wins += 1
        elif bot_hand_value < dealer_hand_value:
            if debug_logs:
                print("Bot looses - has less hand value than dealer")
            total_losses += 1
        else:
            if debug_logs:
                print("Tie")
            total_ties += 1

    return (total_wins, total_losses, total_ties, winrate)


# Function to run initial hand sum simulation
def run_initial_hand_sum_simulations(n):
    """
        Arguments:
        - n: An integer representing the total number of rounds to simulate.

        Returns:
        - initial_hand_sum_statistic: A dictionary containing the statistics of initial hand sums.
    """

    # Initialize the dictionary to store the statistics of initial hand sums
    card_sum_statistic = {}

    iteration = 0

    deck = create_deck()

    while iteration < n:

        # Increase the iteration
        iteration += 1

        # Hit the initial 2 cards for the hand
        hand = hit_cards(deck, num_cards=2)
        hand_value = calculate_hand_value(hand)

        # Update the statistics dictionary with the player's hand value
        if hand_value in card_sum_statistic:
            card_sum_statistic[hand_value] += 1
        else:
            card_sum_statistic[hand_value] = 1

    return card_sum_statistic


# Function to run a simulation and determine the number of times the dealer busts or doesn't bust
def run_dealer_bust_simulation(n, card_value):
    """
        Arguments:
        - n: An integer representing the total number of rounds to simulate.
        - card_value: An integer representing the value of the upcard of the dealer's hand. (2, 11)

        Returns:
        - tuple<int, int> where the first int is "bust_counter" and the second int is the "non_bust_counter" 
            - bust_counter: An integer representing the number of times the dealer busts.
            - non_bust_counter: An integer representing the number of times the dealer doesn't bust.
    """

    # Initialize counters
    bust_counter = 0
    non_bust_counter = 0
    iteration = 0

    # Run simulation for specified number of rounds
    while iteration < n:

        # Create a new deck for each round
        deck = create_deck()
        iteration += 1

        # Set up the dealer's hand with the specified card value
        first_card = hit_card(deck, card_value)
        second_card = hit_cards(deck, num_cards=1)
        dealer_hand = [first_card, second_card[0]]

        # Simulate the dealer's turn until reaching a hand value of 17 or higher
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.extend(hit_cards(deck, num_cards=1))

        # Check if the dealer busts or not and update counters
        if (calculate_hand_value(dealer_hand)) > 21:
            bust_counter += 1
        else:
            non_bust_counter += 1

    return (bust_counter, non_bust_counter)


# Function to run a simulation and determine the number of times a player's starting hand busts or doesn't bust
def run_bust_simulation(n, hand_value, hard_hand):
    """
        Arguments:
        - n: An integer representing the total number of rounds to simulate.
        - hand_value: An integer representing the target hand value to check for bust.
        - hard_hand: A bool representing if the hand value should be hard hand (not including aces) or not

        Returns:
        - tuple<int, int> where the first int is "bust_counter" and the second int is the "non_bust_counter" 
            - bust_counter: An integer representing the number of times the hand busts.
            - non_bust_counter: An integer representing the number of times the hand doesn't bust.
    """

    # Initialize counters
    bust_counter = 0
    non_bust_counter = 0
    iteration = 0

    # Run simulation for specified number of rounds
    while iteration < n:

        iteration += 1

        # Find the lowest value of the first card in order to be able to reach the wanted hand value
        while True:
            deck = create_deck()
            first_card = (hit_cards(deck, num_cards=1))[0]
            if hard_hand == True and first_card[0] == 'A':
                continue
            if values[first_card[0]] > hand_value - 11:
                break

        # Determine the second card's value needed to reach the hand value
        if hard_hand == True:
            while True:
                temp_deck = deck
                random.shuffle(temp_deck)
                second_card = hit_card(
                    temp_deck, hand_value - values[first_card[0]])
                if (second_card[0] == 'A'):
                    continue
                else:
                    deck = temp_deck
                    break

        else:
            second_card = hit_card(deck, hand_value - values[first_card[0]])

        # Create the hand with the first two cards and hit one additional card
        hand = [first_card, second_card]
        hand.extend(hit_cards(deck, num_cards=1))

        # Check if the hand busts or not and update counters
        if calculate_hand_value(hand) > 21:
            # print(hand)
            # print(calculate_hand_value(hand), ": yes", )
            bust_counter += 1
        else:
            # print(hand)
            # print(calculate_hand_value(hand), ": no", )
            non_bust_counter += 1

    return (bust_counter, non_bust_counter)
