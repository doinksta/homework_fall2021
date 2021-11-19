import glob
from tensorflow.python.summary.summary_iterator import summary_iterator
import matplotlib.pyplot as plt


def get_section_results(file, extra=None):
    """
        requires tensorflow==1.12.0
    """
    X = []
    Y = []
    Z = []
    for e in summary_iterator(file):
        for v in e.summary.value:
            if v.tag == 'Train_EnvstepsSoFar':
                X.append(v.simple_value)
            elif v.tag == 'Eval_AverageReturn':
                Y.append(v.simple_value)
            elif extra is not None and v.tag == extra:
                Z.append(v.simple_value)
    return (X, Y, Z) if extra is not None else (X, Y)


root_folder = 'data_final'

# Question 1 Subpart 1 Easy
logdirs = [
'{}/hw5_expl_q1_env1_random_PointmassEasy-v0_18-11-2021_17-00-15/events*'.format(root_folder),
'{}/hw5_expl_q1_env1_rnd_PointmassEasy-v0_18-11-2021_17-00-07/events*'.format(root_folder)
]

labels = [
    'Random Exploration',
    'RND Exploration'
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    plt.plot(X, Y, label=label)

plt.title('Exploration Method vs. Eval Average Return for PointmassEasy')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q1_easy.png')
plt.close()


# Question 1 Subpart 1 Medium
logdirs = [
'{}/hw5_expl_q1_env2_random_PointmassMedium-v0_18-11-2021_17-00-37/events*'.format(root_folder),
'{}/hw5_expl_q1_env2_rnd_PointmassMedium-v0_18-11-2021_17-00-26/events*'.format(root_folder)
]

labels = [
    'Random Exploration',
    'RND Exploration'
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    plt.plot(X, Y, label=label)

plt.title('Exploration Method vs. Eval Average Return for PointmassMedium')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q1_medium.png')
plt.close()


# Question 1 Subpart 2 Medium
logdirs = [
'{}/hw5_expl_q1_alg_med_PointmassMedium-v0_18-11-2021_17-01-11/events*'.format(root_folder),
'{}/hw5_expl_q1_alg_med_rnd_PointmassMedium-v0_18-11-2021_17-01-21/events*'.format(root_folder)
]

labels = [
    'RND2 Exploration',
    'RND Exploration'
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    plt.plot(X, Y, label=label)

plt.title('Exploration Method vs. Eval Average Return for PointmassMedium')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q1_medium2.png')
plt.close()


# Question 1 Subpart 2 Hard
logdirs = [
'{}/hw5_expl_q1_alg_hard_PointmassHard-v0_18-11-2021_17-01-31/events*'.format(root_folder),
'{}/hw5_expl_q1_alg_hard_rnd_PointmassHard-v0_18-11-2021_17-01-41/events*'.format(root_folder)
]

labels = [
    'RND2 Exploration',
    'RND Exploration'
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    plt.plot(X, Y, label=label)

plt.title('Exploration Method vs. Eval Average Return for PointmassHard')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q1_hard2.png')
plt.close()
