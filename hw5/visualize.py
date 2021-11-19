import glob
from tensorflow.python.summary.summary_iterator import summary_iterator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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


# Question 2 Subpart 1
logdirs = [
'{}/hw5_expl_q2_cql_PointmassMedium-v0_18-11-2021_16-18-12/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_PointmassMedium-v0_18-11-2021_16-21-29/events*'.format(root_folder)
]

labels = [
    'CQL',
    'DQN'
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y, Z = get_section_results(eventfile, 'Exploitation_Data_q-values')
    plt.plot(X, Y, label=label)

plt.title('Exploration Method vs. Eval Average Return for PointmassMedium')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q2_learn1.png')
plt.close()

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y, Z = get_section_results(eventfile, 'Exploitation_Data_q-values')
    plt.plot(X[3:], Z, label=label)

plt.title('Exploration Method vs. In-Dataset Q-Values for PointmassMedium')
plt.xlabel('Iteration #')
plt.ylabel('Q Value')
plt.legend()

plt.savefig('plots/q2_qval1.png')
plt.close()


# Question 2 Subpart 2 CQL
logdirs = [
'{}/hw5_expl_q2_cql_numsteps_5000_PointmassMedium-v0_18-11-2021_17-48-10/events*'.format(root_folder),
'{}/hw5_expl_q2_cql_numsteps_8000_PointmassMedium-v0_18-11-2021_17-48-18/events*'.format(root_folder),
'{}/hw5_expl_q2_cql_numsteps_11000_PointmassMedium-v0_18-11-2021_17-48-25/events*'.format(root_folder),
'{}/hw5_expl_q2_cql_numsteps_14000_PointmassMedium-v0_18-11-2021_17-48-31/events*'.format(root_folder)
]

labels = [
    'CQL 5000 Steps',
    'CQL 8000 Steps',
    'CQL 11000 Steps',
    'CQL 14000 Steps',
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    plt.plot(X, Y, label=label)

plt.title('CQL Number of Exploration Steps vs. Eval Average Return for PointmassMedium')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q2_explore_cql.png')
plt.close()


# Question 2 Subpart 2 DQN
logdirs = [
'{}/hw5_expl_q2_dqn_numsteps_5000_PointmassMedium-v0_18-11-2021_17-48-41/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_numsteps_8000_PointmassMedium-v0_18-11-2021_17-48-48/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_numsteps_11000_PointmassMedium-v0_18-11-2021_17-48-56/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_numsteps_14000_PointmassMedium-v0_18-11-2021_17-49-05/events*'.format(root_folder)
]

labels = [
    'DQN 5000 Steps',
    'DQN 8000 Steps',
    'DQN 11000 Steps',
    'DQN 14000 Steps',
]

for logdir, label in zip(logdirs, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    plt.plot(X, Y, label=label)

plt.title('DQN Number of Exploration Steps vs. Eval Average Return for PointmassMedium')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q2_explore_dqn.png')
plt.close()


# Question 2 Subpart 2 Table
logdirs_cql = [
'{}/hw5_expl_q2_cql_numsteps_5000_PointmassMedium-v0_18-11-2021_17-48-10/events*'.format(root_folder),
'{}/hw5_expl_q2_cql_numsteps_8000_PointmassMedium-v0_18-11-2021_17-48-18/events*'.format(root_folder),
'{}/hw5_expl_q2_cql_numsteps_11000_PointmassMedium-v0_18-11-2021_17-48-25/events*'.format(root_folder),
'{}/hw5_expl_q2_cql_numsteps_14000_PointmassMedium-v0_18-11-2021_17-48-31/events*'.format(root_folder),
]
logdirs_dqn = [
'{}/hw5_expl_q2_dqn_numsteps_5000_PointmassMedium-v0_18-11-2021_17-48-41/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_numsteps_8000_PointmassMedium-v0_18-11-2021_17-48-48/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_numsteps_11000_PointmassMedium-v0_18-11-2021_17-48-56/events*'.format(root_folder),
'{}/hw5_expl_q2_dqn_numsteps_14000_PointmassMedium-v0_18-11-2021_17-49-05/events*'.format(root_folder)
]

cql_vals = []
dqn_vals = []

for logdir, label in zip(logdirs_cql, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    cql_vals.append(max(Y))

for logdir, label in zip(logdirs_dqn, labels):
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    dqn_vals.append(max(Y))

#define figure and axes
fig, ax = plt.subplots()

#hide the axes
plt.gca().axis('off')
plt.gca().axis('tight')

plt.table(cellText=[cql_vals, dqn_vals],
          rowLabels=['CQL', 'DQN'],
          colLabels=['5000 Steps', '8000 Steps', '11000 Steps', '14000 Steps'],
          loc='center'
        )

plt.title('Number of Exploration Steps vs. Max Eval Average Return')

plt.tight_layout()

plt.savefig('plots/q2_explore_table.png')
plt.close()

