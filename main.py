from experiment import experiment_runner
from data import data_generator
from visualization import visualizer


def main():
    n = [1, 2, 4, 8, 16, 32, 64, 128, 256]

    config = {}
    config['algorithms'] = ['selection_sort', 'shell_sort', 'quick_sort']
    config['runs'] = 100

    data = {'Random Data': 'figures/random_data.png', 'Sorted Data': 'figures/sorted_data.png',
            'Reversed Sorted Data': 'figures/reversed_sorted_data.png',
            'Almost Sorted Data': 'figures/almost_sorted_data.png'}
    i = 0
    for title in data:
        config['data'] = get_sort(title, n)

        results = experiment_runner.run(config)
        visualizer.plot_results(results, title, data[title])
        i += 1


def get_sort(title, n):
    if title == 'Random Data':
        return [data_generator.generate_random_data(j) for j in n]
    elif title == 'Sorted Data':
        return [data_generator.generate_sorted_data(j) for j in n]
    elif title == 'Reversed Sorted Data':
        return [data_generator.generate_reversed_sorted_data(j) for j in n]
    elif title == 'Almost Sorted Data':
        return [data_generator.generate_almost_sorted_data(j, int(j*0.1)) for j in n]


if __name__ == "__main__":
    main()
