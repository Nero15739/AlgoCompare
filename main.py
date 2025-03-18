import os
import sys
import time

from Algorithm import Algorithm

# Algorithm Comparison Software where two separate algorithms can be selected and face off against each other with varing inputs, both generated and non
# Can Auto find the Base operation and auto insert the iteration count




def main ():

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            print(f"Algorithm 1:{sys.argv[1]}")
            print(f"Algorithm 2:{sys.argv[2]}")
    
    algorithms_to_test = []

    response = None
    while response != "4":
        print("Welcome to Compare Algos") 
        print("Menu:")
        print("1 Create Algorithm")
        print("2 Test Algorithm")
        print("3 Compare Algorithms")
        print("4 Exit")

        response = input("Enter a number to continue:\n")
        match response:
            case "1":
                create_algorithm()
            case "2":
                selected_algorithm_index = 0
                if len(algorithms_to_test) > 1:
                    while test_response != "4":
                        print("Welcome to Compare Algos") 
                        print("Menu:")
                        print("1 Create Algorithm")
                        print("2 Test Algorithm")
                        print("3 Compare Algorithms")
                        print("4 Exit")
                        test_response = input("Enter a number to continue:\n")
                elif len(algorithms_to_test) == 1:
                    print(f"Do you want to run {algorithms_to_test[0]}")
                test_algorithm(algorithms_to_test[selected_algorithm_index])
            case "3":
                compare_algorithms()
            case "4":
                print("Goodbye")
            case _:
                print("unknown input - Must be a number from 1 - 4")

    # start = time.perf_counter()
    # end = time.perf_counter()
    # print_stats("Algo2 - Test", start, end,2453)



def create_algorithm():
    print("Create Algo")
    pass

def test_algorithm():
    print("Test Algo")
    algorithm = Algorithm("Tests/TestAlgoPrint.py")
    try:
        data, count, start, end = algorithm.run_script([1,2,43,2])
        print(f"Data returned: {data} with a iteration count of {count}")
        algorithm.print_stats(algorithm, start, end, -1);
    except Exception as e:
        print(e)
    pass

def compare_algorithms (first_algorithm, second_algorithm):
    first_start = time.perf_counter()
    time.sleep(5) #The algorithm running and returning values
    first_end = time.perf_counter()
    second_start = time.perf_counter()
    time.sleep(5)
    second_end = time.perf_counter()

    Algorithm.print_stats(first_algorithm,first_start,first_end,-1);
    Algorithm.print_stats(second_algorithm,second_start,second_end,-1);


main()