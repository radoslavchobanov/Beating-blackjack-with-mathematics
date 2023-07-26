import blackjack as bj
import matplotlib.pyplot as plt

# Times drawing pair of cards from a deck
simulations_count = 100000000
# _____________________________________________________________________________________________________________


def get_sorted_initial_hand_sum_possibilities():
    # Get dictionary with pair (sum, count)
    initial_hand_sum_possibilities = bj.run_initial_hand_sum_simulations(
        simulations_count)

    # Sort the dictionary in incrementing order by key
    sorted_initial_hand_sum_possibilities = dict(
        sorted(initial_hand_sum_possibilities.items(), key=lambda x: x[0]))

    return sorted_initial_hand_sum_possibilities


if __name__ == "__main__":
    # Get the statistic dictionary
    sorted_sum_possibilities = get_sorted_initial_hand_sum_possibilities()

    # Get the keys and the values in separated lists
    keys = list(sorted_sum_possibilities.keys())
    values = list(sorted_sum_possibilities.values())

    # Draw the histogram
    plt.bar(range(len(keys)), values)
    plt.xlabel('Player initial hand value')
    plt.ylabel('Amount of times having the relevant hand value')
    plt.title('Histogram')
    plt.xticks(range(len(keys)), keys)
    plt.show()
