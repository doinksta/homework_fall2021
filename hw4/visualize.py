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

# Question 3 obstacles
logdir = '{}/hw4_q3_obstacles_obstacles-cs285-v0_03-11-2021_02-14-27/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]

X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Eval_AverageReturn', marker='o')
plt.title('Train and Eval Average Return for Obstacles')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q3_obs.png')
plt.close()

# Question 3 reacher
logdir = '{}/hw4_q3_reacher_reacher-cs285-v0_03-11-2021_11-32-01/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]

X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Eval_AverageReturn', marker='o')
plt.title('Train and Eval Average Return for Reacher')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q3_reach.png')
plt.close()

# Question 3 cheetah
logdir = '{}/hw4_q3_cheetah_cheetah-cs285-v0_03-11-2021_11-58-38/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]

X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Eval_AverageReturn', marker='o')
plt.title('Train and Eval Average Return for Cheetah')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q3_cheetah.png')
plt.close()

# Question 4 ensemble
logdir = '{}/hw4_q4_reacher_ensemble1_reacher-cs285-v0_03-11-2021_11-04-27/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Ensemble Size 1 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Ensemble Size 1 Eval_AverageReturn', marker='o')

logdir = '{}/hw4_q4_reacher_ensemble3_reacher-cs285-v0_03-11-2021_11-04-32/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Ensemble Size 3 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Ensemble Size 3 Eval_AverageReturn', marker='o')

logdir = '{}/hw4_q4_reacher_ensemble5_reacher-cs285-v0_03-11-2021_11-04-21/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Ensemble Size 5 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Ensemble Size 5 Eval_AverageReturn', marker='o')

plt.title('Ensemble Size vs. Train and Eval Average Return for Reacher')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q4_ensemble.png')
plt.close()

# Question 4 cand
logdir = '{}/hw4_q4_reacher_numseq100_reacher-cs285-v0_03-11-2021_02-16-23/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Candidate Sequences 100 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Candidate Sequences 100 Eval_AverageReturn', marker='o')

logdir = '{}/hw4_q4_reacher_numseq1000_reacher-cs285-v0_03-11-2021_11-04-36/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Candidate Sequences 1000 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Candidate Sequences 1000 Eval_AverageReturn', marker='o')

plt.title('Number of Candidate Action Sequences vs. Train and Eval Average Return for Reacher')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q4_cand.png')
plt.close()

# Question 4 horizon
logdir = '{}/hw4_q4_reacher_horizon5_reacher-cs285-v0_03-11-2021_02-15-24/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Horizon 5 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Horizon 5 Eval_AverageReturn', marker='o')

logdir = '{}/hw4_q4_reacher_horizon15_reacher-cs285-v0_03-11-2021_02-15-43/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Horizon 15 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Horizon 15 Eval_AverageReturn', marker='o')

logdir = '{}/hw4_q4_reacher_horizon30_reacher-cs285-v0_03-11-2021_11-23-58/events*'.format(root_folder)
eventfile = glob.glob(logdir)[0]
X, Y = get_section_results(eventfile)
plt.plot(range(len(X)), X, label='Horizon 30 Train_AverageReturn', marker='o')
plt.plot(range(len(Y)), Y, label='Horizon 30 Eval_AverageReturn', marker='o')

plt.title('Horizon Length vs. Train and Eval Average Return for Reacher')
plt.xlabel('Iteration #')
plt.ylabel('Average Return')
plt.legend()

plt.savefig('plots/q4_horizon.png')
plt.close()
