'''
-----
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!
Input
-----
'''

def primes_between(lower_limit, upper_limit):
    return([x for x in range(lower_limit, upper_limit) if all(x % y != 0 for y in range(2, x))])

def main():
    print(primes_between(int(input("prime lower limit")), int(input("prime upper limit"))))

if __name__ == '__main__':
    main()
