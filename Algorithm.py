import os
import importlib.util
import time

class File():
    def __init__(self,name,file_path):
        self.name = name
        self.file_path = file_path
    

class Algorithm (File):
    def __init__(self):
        super.__init__(self, None, None)
        self.valid = False
        self.has_counter = False
        self.__spec = None
        self.__algo_module = None
        pass

    def __init__(self, file_path):
        super.__init__(self,file_path, file_path)
        self.valid = False
        self.has_counter = False
        self.__spec = None
        self.__algo_module = None
        
        #should compile and test to see if the file is a valid Algorithm 
        self.load_script(file_path)
        
    def __str__(self):
        return f"{self.name} is an Algorithm"

    #Loads the Script into the Algorithm so run_script can make use of it 
    def load_script(self, file_path):
        
        module_name = file_path
        if file_path.endswith(".py"):
            module_name = file_path[:-3] #removes the .py extention
            
            self.__spec = importlib.util.spec_from_file_location(module_name, file_path)
            self.algo_module = importlib.util.module_from_spec(self.__spec)

    def reload_script(self):
        try:
            self.load_script(self.__file_path)
        except Exception as e:
            print(e)
            
    #Will run script if it is present
    def run_script(self, input):
        if self.algo_module == None:
            raise Exception("The Algorithm has not been loaded!")
            
        self.__spec.loader.exec_module(self.algo_module)
        start_time = time.perf_counter()
        array, count = self.algo_module.main(input)
        end_time = time.perf_counter()
        
        return array, count, start_time, end_time
    
    def print_stats (algorithm_name, start_time, end_time, count):
        difference = end_time - start_time
        print(f"{algorithm_name}\nTook {difference} Seconds to complete\nAnd {count} iterations")