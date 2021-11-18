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
            if v.tag == 'Train_EnvstepsSoFar':
                X.append(v.simple_value)
            elif v.tag == 'Eval_AverageReturn':
                Y.append(v.simple_value)
    return X, Y


root_folder = 'data_final'

# Question 1 Subpart 1 Easy
logdirs = [
'{}/hw5_expl_q1_env1_random_PointmassEasy-v0_17-11-2021_17-03-27/events*'.format(root_folder),
'{}/hw5_expl_q1_env1_rnd_PointmassEasy-v0_17-11-2021_17-03-19/events*'.format(root_folder)
]

labels = [
    'Epsilon Greedy Exploration',
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
'{}/hw5_expl_q1_env2_random_PointmassMedium-v0_17-11-2021_17-16-10/events*'.format(root_folder),
'{}/hw5_expl_q1_env2_rnd_PointmassMedium-v0_17-11-2021_17-15-55/events*'.format(root_folder)
]

labels = [
    'Epsilon Greedy Exploration',
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
'{}/hw5_expl_q1_alg_med_PointmassMedium-v0_18-11-2021_00-05-11/events*'.format(root_folder),
'{}/hw5_expl_q1_alg_med_rnd_PointmassMedium-v0_18-11-2021_00-11-49/events*'.format(root_folder)
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
'{}/hw5_expl_q1_alg_hard_PointmassHard-v0_18-11-2021_00-05-21/events*'.format(root_folder),
'{}/hw5_expl_q1_alg_hard_rnd_PointmassHard-v0_18-11-2021_00-09-15/events*'.format(root_folder)
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
