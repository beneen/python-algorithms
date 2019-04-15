'''
-----
Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is a substring of A and 0 otherwise
-----
'''


def is_binary_substring(larger_string, shorter_string):
    if shorter_string in larger_string:
        return True
    else:
        return False


def main():
    print(is_binary_substring(input("larger binary string"), input("shorter binary string")))

if __name__ == '__main__':
    main()
