#import unittest
from functions.get_files_info import get_files_info


if __name__ == "__main__":

    tests = [("calculator", "."), ("calculator", "pkg"), ("calculator", "/bin"), ("calculator", "../")]

    for a,b in tests:
        print(f"Test results for: {a} + {b}")
        print(get_files_info(a,b))
