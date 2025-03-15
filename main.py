import os
import sys
import time


# Algorithm Comparison Software where two separate algorithms can be selected and face off against each other with varing inputs, both generated and non
# Can Auto find the Base operation and auto insert the iteration count
class Algorithm:
    def __init__():
        self.__file_path
        self.valid = False
        self.has_counter = False


def main ():

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            print(f"Algorithm 1:{sys.argv[1]}")
            print(f"Algorithm 2:{sys.argv[2]}")

    print("Welcome to Compare Algos") 
    print("Menu:")
    print("1 Create Algorithm")
    print("2 Test Algorithm")
    print("3 Compare Algorithms")



    start = time.perf_counter()
    
    end = time.perf_counter()
    print_stats("Algo2 - Test", start, end,2453)

def print_stats (algorithm_name, start_time, end_time, count):
    difference = end_time - start_time
    print(f"{algorithm_name}\nTook {difference} Seconds to complete\nAnd {count} iterations")

def compare_algorithms (first_algorithm, second_algorithm):
    first_start = time.perf_counter()
    time.sleep(5) #The algorithm running and returning values
    first_end = time.perf_counter()
    second_start = time.perf_counter()
    time.sleep(5)
    second_end = time.perf_counter()

    print_stats(first_algorithm,first_start,first_end,-1);
    print_stats(second_algorithm,second_start,second_end,-1);


main()