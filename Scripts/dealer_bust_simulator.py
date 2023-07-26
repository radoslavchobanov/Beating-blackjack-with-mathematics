import blackjack as bj
import initial_hand_sum_simulator as ss
import matplotlib.pyplot as plt

bust_counter_statistic = {}

total_simulations = 100000

(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 2)
bust_counter_statistic[2] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 3)
bust_counter_statistic[3] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 4)
bust_counter_statistic[4] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 5)
bust_counter_statistic[5] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 6)
bust_counter_statistic[6] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 7)
bust_counter_statistic[7] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 8)
bust_counter_statistic[8] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 9)
bust_counter_statistic[9] = bust_counter / total_simulations
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 10)
bust_counter_statistic[10] = bust_counter / total_simulations

print(bust_counter, " ", non_bust_counter)
(bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(total_simulations, 11)
bust_counter_statistic[11] = bust_counter / total_simulations


if __name__ == "__main__":
    # Get the keys and the values in separated lists
    keys = list(bust_counter_statistic.keys())
    values = list(bust_counter_statistic.values())

    # Draw the histogram
    plt.bar(range(len(keys)), values)
    plt.xlabel('Dealer upcard')
    plt.ylabel('Busting odds')
    plt.title('Histogram')
    plt.xticks(range(len(keys)), keys)
    plt.show()


def run_simulations_and_print_statistics(n, upcard_value):
    (bust_counter, non_bust_counter) = bj.run_dealer_bust_simulation(n, upcard_value)