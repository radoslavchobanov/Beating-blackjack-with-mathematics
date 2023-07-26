import matplotlib.pyplot as plt
import initial_hand_sum_simulator as ss

# what is the possibility for busting with 3 cards; what about 4, 5, 6, ... etc

# !!! Busting with 3 cards is only possible if the sum of the inital 2 cards was 12 or greater

# First lets find what is the possibility of getting 12 or more hand value in the initial 2 cards
initial_hand_possibilities = ss.get_sorted_initial_hand_sum_possibilities()
total_simulations = ss.simulations_count

sum_of_simulations_with_12_or_more = 0
possibility_for_12_or_more = 0.0

for key, value in initial_hand_possibilities.items():
    if key >= 12:
        sum_of_simulations_with_12_or_more += value

print(round(sum_of_simulations_with_12_or_more / total_simulations, 5))

# The possibility is roughly 78%

# from here:
# to bust with sum of 12, only possibility is having a card with value of 10 => 10, J, Q, K => 4*4 = 16 cards
# 16 cards to bust from 52 in total => 16/52 = 0.3076923076923077 = 30.77%

# to bust with sum of 12 -> 4*4/52 = 0.3076923076923077 = 30.77%

# to bust with sum of 13 -> 5*4/52 = 0.3846153846153846 = 38.46%

# to bust with sum of 14 -> 6*4/52 = 0.4615384615384615 = 46.15%

# to bust with sum of 15 -> 7*4/52 = 0.5384615384615385 = 53.85%

# to bust with sum of 16 -> 8*4/52 = 0.6153846153846154 = 61.54%

# to bust with sum of 17 -> 9*4/52 = 0.6923076923076923 = 69.23%

# to bust with sum of 18 -> 10*4/52 = 0.7692307692307692 = 76.92%

# to bust with sum of 19 -> 11*4/52 = 0.8461538461538462 = 84.62%

# to bust with sum of 20 -> 12*4/52 = 0.9230769230769231 = 92.31%
