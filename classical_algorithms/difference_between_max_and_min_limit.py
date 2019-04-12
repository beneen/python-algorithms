import os


def minumum_number(limit, array):
    sorted_array = sorted(array)

    if (sorted_array[-1] - sorted_array[0]) < limit:
        return len(sorted_array)
    backwards_array = sorted(array, reverse=True)
    composite_list = (list(zip( * ((x, y) for (x, y) in zip(sorted_array, backwards_array) if abs(x - y) >= limit))))
    return len(composite_list[0]) + 1

def main():
    limit = int(input("limit:").strip())

    array_user_input = int(input("size of array:").strip())

    array = []

    for _ in range(array_user_input):
        item = int(input("array elements:").strip())
        array.append(item)

    print(minumum_number(limit, array))


if __name__ == '__main__':
    main()