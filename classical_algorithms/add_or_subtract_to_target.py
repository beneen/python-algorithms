import os


def minumum_number(limit, array):
    return False

def main():
    limit = int(input().strip())

    array_user_input = int(input().strip())

    array = []

    for _ in range(array_user_input):
        happy_item = int(input().strip())
        array.append(happy_item)

    print(minumum_number(limit, array))




if __name__ == '__main__':
    main()