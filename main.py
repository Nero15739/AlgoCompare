import os
import sys
import time
# Algorithm Comparison Software where two separate algorithms can be selected and face off against each other with varing inputs, both generated and non
# Can Auto find the Base operation and auto insert the iteration count
def main ():
    print("Welcome to Compare Algos") 
    print("Menu:")
    print("1 Create Algorithm")
    print("2 Test Algorithm")
    print("3 Compare Algorithms")
    start = time.time()
    time.sleep(5)
    end = time.time()
    print_stats("Algo2 - Test", start, end,2453)

def print_stats (algorithm_name, start_time, end_time, count):
    difference = end_time - start_time
    print(f"{algorithm_name}\nTook {difference} Seconds to complete\nAnd {count} iterations")




main()