import random


def generate_random_data(n):
    a_list = random.sample(range(1, 1000), n)
    return a_list


def generate_sorted_data(n):
    a_list = random.sample(range(1, 1000), n)
    a_list.sort()
    return a_list


def generate_reversed_sorted_data(n):
    a_list = random.sample(range(1, 1000), n)
    a_list.sort(reverse=True)
    return a_list


def generate_almost_sorted_data(n, m):
    a_list = random.sample(range(1, 1000), n)
    a_list.sort()
    while m > 0:
        swapPos1 = swapPos2 = random.randint(0,n-1)
        while swapPos1 == swapPos2:
            swapPos2 = random.randint(0,n-1)
        temp = a_list[swapPos1]
        a_list[swapPos1] = a_list[swapPos2]
        a_list[swapPos2] = temp
        m -= 1

    return a_list


