import blackjack as bj

# Running simulations of the complete game using basic strategies and calculating statistics based on the results
def run_simulations_and_print_statistics(n):
    """
        Args:
            n (int): The number of game simulations to run.
    """

    total_wins = 0
    total_losses = 0
    total_ties = 0

    # Run game simulations and retrieve the results
    (total_wins, total_losses,
     total_ties, winrates) = bj.run_complete_game_simulations_with_basic_strategies(n)

    # Print the statistics
    print_statistics(total_wins, total_losses, total_ties)


def print_statistics(wins, losses, ties):
    """
        Print the statistics of the game simulations.
    """

    print("total wins: " + str(wins))
    print("total losses: " + str(losses))
    print("total ties: " + str(ties))
    print("winrate: " + str(round(wins/(wins + losses + ties), 2)))
