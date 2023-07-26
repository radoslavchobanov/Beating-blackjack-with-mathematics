import initial_hand_sum_simulator as ss
import blackjack as bj
import basic_strategy_simulator as bss
import matplotlib.pyplot as plt

bust_counters = {}

for number in range(12, 21):
    (bust_counter, non_bust_counter) = bj.run_bust_simulation(10000, number, True)
    bust_counters[number] = bust_counter

bust_counters = dict(sorted(bust_counters.items()))

for key, value in bust_counters.items():
    print(key, ":", value)


# bust_counter, non_bust_counter = bj.run_bust_simulation(1000, 20, True)
# print(bust_counter)