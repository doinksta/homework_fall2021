import matplotlib.pyplot as plt
import pandas as pd
import os

if not os.path.exists('plots/'):
    os.makedirs('plots/')

# Question 1
filenames = [
    'experiment_csv/run-q1_MsPacman-v0_19-10-2021_13-50-42-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q1_MsPacman-v0_19-10-2021_13-50-42-tag-Train_BestReturn.csv'
]

labels = ['Average Train Return', 'Best Mean Return']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    data = data[data['Step'] <= 1000000]
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('MsPacMan Train Average Returns vs. Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Train Average Return')
plt.gca().ticklabel_format(axis='x', format='sci', scilimits=(0, 0))

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/q1.png', bbox_inches='tight')
plt.close()

# Question 2
filenames_dqn = [
    'experiment_csv/run-q2_dqn_1_LunarLander-v3_19-10-2021_20-05-00-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q2_dqn_2_LunarLander-v3_19-10-2021_20-05-34-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q2_dqn_3_LunarLander-v3_19-10-2021_20-05-49-tag-Train_AverageReturn.csv'
]
filenames_ddqn = [
    'experiment_csv/run-q2_doubledqn_1_LunarLander-v3_19-10-2021_20-06-41-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q2_doubledqn_2_LunarLander-v3_19-10-2021_20-06-50-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q2_doubledqn_3_LunarLander-v3_19-10-2021_20-06-59-tag-Train_AverageReturn.csv'
]

x = None
dqn_y = None
ddqn_y = None

for filename in filenames_dqn:
    data = pd.read_csv(filename)
    x = data['Step']
    if dqn_y is None:
        dqn_y = data['Value']
    else:
        dqn_y += data['Value']

dqn_y /= len(filenames_dqn)

for filename in filenames_ddqn:
    data = pd.read_csv(filename)
    x = data['Step']
    if ddqn_y is None:
        ddqn_y = data['Value']
    else:
        ddqn_y += data['Value']

ddqn_y /= len(filenames_ddqn)

labels = ['DQN Average Train Return', 'DDQN Average Train Return']

for y, label in zip([dqn_y, ddqn_y], labels):
    plt.plot(x, y, label=label)

plt.title('LunarLandar Train Average Returns vs. Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Train Average Return')
plt.gca().ticklabel_format(axis='x', format='sci', scilimits=(0, 0))

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/q2.png', bbox_inches='tight')
plt.close()


# Question 3
filenames = [
    'experiment_csv/run-q3_hparam0_LunarLander-v3_19-10-2021_22-36-16-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q3_hparam1_LunarLander-v3_19-10-2021_23-29-34-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q3_hparam2_LunarLander-v3_19-10-2021_23-29-55-tag-Train_AverageReturn.csv',
    'experiment_csv/run-q3_hparam3_LunarLander-v3_19-10-2021_23-30-15-tag-Train_AverageReturn.csv'
]

labels = ['Exploration Duration Multiplier 0.1 (Default)', 'Exploration Duration Multiplier 0.2', 'Exploration Duration Multiplier 0.3', 'Exploration Duration Multiplier 0.4']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('Varied Exploration Time LunarLander Train Average Returns vs. Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Train Average Return')
plt.gca().ticklabel_format(axis='x', format='sci', scilimits=(0, 0))

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/q3.png', bbox_inches='tight')
plt.close()


# Question 4
filenames = [
    'experiment_csv/run-q4_ac_1_1_CartPole-v0_20-10-2021_14-22-56-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_1_100_CartPole-v0_20-10-2021_14-23-07-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_10_10_CartPole-v0_20-10-2021_14-23-09-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_100_1_CartPole-v0_20-10-2021_14-23-23-tag-Eval_AverageReturn.csv'
]

labels = ['NTU 1, NGSPTU 1', 'NTU 1, NGSPTU 100', 'NTU 10, NGSPTU 10', 'NTU 100, NGSPTU 1']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('Varied Target Updates and Gradient Steps CartPole Train Average Returns vs. Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Train Average Return')
plt.gca().ticklabel_format(axis='x', format='sci', scilimits=(0, 0))

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/q4.png', bbox_inches='tight')
plt.close()