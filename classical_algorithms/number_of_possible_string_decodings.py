'''
-----
essentially the coin changing problem but mapping the output to the alphabet
-----
'''
import string

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

def alpha_code(text):
    text_list = [int(x) for x in str(text)]
    text_sum = sum(text_list)
    encoding_backwards = dict()
    numbers = list(range(1, 27))
    for index, letter in enumerate(string.ascii_lowercase):
        encoding_backwards[letter] = index + 1
    encoding = {y: x for x, y in encoding_backwards.items()}
    subsets = list(subset_sum(numbers, text_sum))
    print(subsets)
    letter_combinations = [[encoding.get(x) for x in u] for u in subsets]
    print(letter_combinations)


def main():
    print(alpha_code(int(input("valid encryption"))))

if __name__ == '__main__':
    main()

