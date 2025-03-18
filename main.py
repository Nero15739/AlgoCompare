import os
import sys
import time

import importlib.util

# Algorithm Comparison Software where two separate algorithms can be selected and face off against each other with varing inputs, both generated and non
# Can Auto find the Base operation and auto insert the iteration count
class Algorithm ():
    def __init__(self):
        self.__file_path = None
        self.name = None
        self.valid = False
        self.has_counter = False
        self.__spec = None
        self.__algo_module = None
        pass

    def __init__(self, file_path):
        self.__file_path = file_path
        self.name = None
        self.valid = False
        self.has_counter = False
        self.__spec = None
        self.__algo_module = None
        
        #should compile and test to see if the file is a valid Algorithm 
        self.load_script(file_path)
        
    def __str__(self):
        return f"{self.name} is an Algorithm"

    def load_script(self, file_path):
        module_name = file_path
        if file_path.endswith(".py"):
            module_name = file_path[:-3] #removes the .py extention
            
            self.__spec = importlib.util.spec_from_file_location(module_name, file_path)
            self.algo_module = importlib.util.module_from_spec(self.__spec)
            

    def run_script(self, input):
        self.__spec.loader.exec_module(self.algo_module)
        start_time = time.perf_counter()
        array, count = self.algo_module.main(input)
        end_time = time.perf_counter()
        
        return array, count, start_time, end_time



def main ():

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            print(f"Algorithm 1:{sys.argv[1]}")
            print(f"Algorithm 2:{sys.argv[2]}")
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
                test_algorithm()
            case "3":
                compare_algorithms()
            case "4":
                print("Goodbye")
            case _:
                print("unknown input - Must be a number from 1 - 4")

    # start = time.perf_counter()
    # end = time.perf_counter()
    # print_stats("Algo2 - Test", start, end,2453)

def print_stats (algorithm_name, start_time, end_time, count):
    difference = end_time - start_time
    print(f"{algorithm_name}\nTook {difference} Seconds to complete\nAnd {count} iterations")

def create_algorithm():
    print("Create Algo")
    pass

def test_algorithm():
    print("Test Algo")
    algorithm = Algorithm("Tests/TestAlgoPrint.py")
    try:
        data, count, start, end = algorithm.run_script([1,2,43,2])
        print(f"Data returned: {data} with a iteration count of {count}")
        print_stats(algorithm, start, end, -1);
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

    print_stats(first_algorithm,first_start,first_end,-1);
    print_stats(second_algorithm,second_start,second_end,-1);


main()