#import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def get_files_info_tests():
    tests = [("calculator", "."), ("calculator", "pkg"), ("calculator", "/bin"), ("calculator", "../")]

    for args in tests:
        print(f"Test results for: get_files_info({", ".join(args)})")
        print(get_files_info(*args))

def get_file_content_tests():

    #tests = [("calculator", "lorem.txt")]
    tests = [("calculator", "main.py"),("calculator", "pkg/calculator.py"),("calculator", "/bin/cat")]

    for args in tests:
        print(f"Test results for: get_file_content({", ".join(args)})")
        print(get_file_content(*args))

def write_file_tests():

    tests = [("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")]

    for args in tests:
        print(f"Test results for: write_file({", ".join(args)})")
        print(write_file(*args))


def run_python_tests():

    tests = [("calculator", "main.py"),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py")]

    for args in tests:
        print(f"Test results for: run_python_file({", ".join(args)})")
        print(run_python_file(*args))

if __name__ == "__main__":

  #get_files_info_tests()
  #get_file_content_tests()
  #write_file_tests()
  run_python_tests()
