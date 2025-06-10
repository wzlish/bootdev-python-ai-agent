#import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def get_files_info_tests():
    tests = [("calculator", "."), ("calculator", "pkg"), ("calculator", "/bin"), ("calculator", "../")]

    for a,b in tests:
        print(f"Test results for: get_files_info({a}, {b})")
        print(get_files_info(a,b))

def get_file_content_tests():

    #tests = [("calculator", "lorem.txt")]
    tests = [("calculator", "main.py"),("calculator", "pkg/calculator.py"),("calculator", "/bin/cat")]

    for a,b in tests:
        print(f"Test results for: get_file_content({a},{b})")
        print(get_file_content(a,b))


if __name__ == "__main__":

  #get_files_info_tests()
  get_file_content_tests()
