import glob
from tensorflow.python.summary.summary_iterator import summary_iterator
import matplotlib.pyplot as plt


def get_section_results(file):
    """
        requires tensorflow==1.12.0
    """
    X = []
    Y = []
    for e in summary_iterator(file):
        for v in e.summary.value:
            if v.tag == 'Train_AverageReturn':
                X.append(v.simple_value)
            elif v.tag == 'Eval_AverageReturn':
                Y.append(v.simple_value)
    return X, Y


root_folder = 'data_final'

# Question 2
logdir = '{}/hw4_q2_obstacles_singleiteration_obstacles-cs285-v0_03-11-2021_00-55-32/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]

X, Y = get_section_results(eventfile)
plt.plot(0, X[0], label='Train_AverageReturn', marker='o')
plt.plot(0, Y[0], label='Eval_AverageReturn', marker='o')
plt.title('Train and Eval Average Return for Obstacles')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q2.png')
plt.close()
