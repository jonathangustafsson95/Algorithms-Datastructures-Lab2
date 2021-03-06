from visualization import visualizer
from experiment import experiment_runner
from data import data_generator

n = [1, 2, 4, 8, 16, 32, 64, 128, 256]

config = {}
config['algorithms'] = ['selection_sort', 'shell_sort', 'quick_sort']
config['data'] = [data_generator.generate_random_data(i) for i in n]
config['runs'] = 10

results = experiment_runner.run(config)
visualizer.plot_results(results, 'test')
