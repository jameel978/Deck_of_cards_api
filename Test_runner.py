
import unittest
from concurrent.futures import ThreadPoolExecutor
from io import StringIO
import time

# Import your test modules
from Tests.test_piles import *
from Tests.test_decks import *


def run_test(current_test):
    suite = unittest.TestSuite()
    suite.addTest(init_test(current_test))
    # Run the test suite
    result = unittest.TextTestRunner(stream=StringIO(), verbosity=2).run(suite)
    time_spent = result.collectedDurations[0][1]
    if result.wasSuccessful():
        print(f'{current_test[1]} Passed!, run time {time_spent:.2f} sec')
    else:
        print(f'{current_test[1]} Failed!, run time {time_spent:.2f} sec')

def init_test(input_):
    return input_[0](input_[1])

def run_tests_in_parallel(test_cases):
    with ThreadPoolExecutor(max_workers=len(test_cases)) as executor:
        executor.map(run_test, test_cases)

def run_tests_in_serrial(test_classes):
    for test  in test_classes:
        run_test(test)

if __name__ == "__main__":
    # List of test classes
    test_classes = [DeckOfCards_decks_tests, DeckOfCards_piles_tests]
    all_test_cases = prepair_all_tests(test_classes)


    #read from config
    test_config = read_json("Config/Test_runner.json")
    serial_run = test_config["run_serial"]
    start_time = time.time()
    if serial_run:
        print("running test in serial")
        print("")
        run_tests_in_serrial(all_test_cases)
    else:
        print("running test in serial")
        print("")
        run_tests_in_parallel(all_test_cases)
    elapsed_time = time.time() - start_time
    print("")
    print(f"Total Run time: {elapsed_time:.2f} seconds")


