import matplotlib
import matplotlib.pyplot as plt
import math
import os
matplotlib.use('TkAgg')


def plot_results(results, title, filename=None):

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for key in results:
        ops = []
        n = []
        time = []

        for i in range(len(results[key])):
            ops.append(results[key][i]['ops'])
            n.append(results[key][i]['n'])
            time.append(results[key][i]['time'])

        ax1.plot(n, ops, label=key)
        ax2.plot(n, time, label=key)

    ax1.set_title('Time complexity')
    ax1.set_ylabel('ops (#)')
    ax1.set_xlabel('size (n)')
    ax1.plot(n, constant(n), label='constant', linestyle='dashed')
    ax1.plot(n, logarithmic(n), label='logarithmic', linestyle='dashed')
    ax1.plot(n, linear(n), label='linear', linestyle='dashed')
    ax1.plot(n, quadratic(n), label='quadratic', linestyle='dashed')
    ax1.legend()

    ax2.set_title('Time')
    ax2.set_ylabel('Time (s)')
    ax2.set_xlabel('size (n)')
    ax2.legend()

    fig.suptitle(title)

    plt.show()

    if filename:
        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.mkdir(os.path.dirname(filename))
        fig.savefig(filename)


def constant(n):
    return [0 for i in range(len(n))]


def logarithmic(n):
    return [math.log2(i) for i in n]


def linear(n):
    return [i for i in n]


def quadratic(n):
    return [i**2 for i in n]

