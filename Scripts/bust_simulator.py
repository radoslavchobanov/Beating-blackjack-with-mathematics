import blackjack as bj


def run_simulations(n, hand_value):
    """
        Run simulations of rounds and print statistics based on the results.

        Arguments:
        - n: An integer representing the total number of rounds to simulate.
        - hand_value: An integer representing the target hand value to check for bust.

        Returns:
            None
    """

    # Run the bust simulation and retrieve the results
    (bust_counter, non_bust_counter) = bj.run_bust_simulation(n, hand_value)

    # Print the statistics
    print_statistics(bust_counter, non_bust_counter)


def print_statistics(bust_counter, non_bust_counter):
    """
        Print statistics based on the bust and non-bust counters.

        Arguments:
        - bust_counter (int): The number of rounds resulting in a bust.
        - non_bust_counter (int): The number of rounds not resulting in a bust.

        Returns:
            None
    """
    
    # Print the bust counter
    print(bust_counter)
    # Print the non-bust counter
    print(non_bust_counter)
