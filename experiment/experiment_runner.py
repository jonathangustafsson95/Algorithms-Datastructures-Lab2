import time
from algorithm import selection_sort
from algorithm import shell_sort
from algorithm import quick_sort


def get_algorithm(s):
    if s == "selection_sort":
        return (selection_sort)
    elif s == "shell_sort":
        return (shell_sort)
    else:
        return (quick_sort)


def run(config):
    results = {}

    for i in config['algorithms']:
        results[i] = []
        algorithm = get_algorithm(i)

        for j in range(len(config['data'])):
            count = 0
            start = time.time()

            for k in range(config['runs']):
                copy = config['data'][j].copy()
                count += algorithm.sort(copy)

            end = time.time()

            ops = count / config['runs']
            n = len(config['data'][j])
            elapsedTime = end - start

            results[i].append({'ops': ops, 'n': n, 'time': elapsedTime})

    return results


