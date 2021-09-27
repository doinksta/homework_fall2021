import matplotlib.pyplot as plt
import pandas as pd
import os

if not os.path.exists('plots/'):
    os.makedirs('plots/')

# Experiment 1 SB
filenames = [
    'experiment_csv/run-q1_sb_no_rtg_dsa_CartPole-v0_26-09-2021_14-38-45-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q1_sb_rtg_dsa_CartPole-v0_26-09-2021_14-40-05-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q1_sb_rtg_na_CartPole-v0_26-09-2021_14-41-30-tag-Eval_AverageReturn.csv'
]

labels = ['no_rtg_dsa', 'rtg_dsa', 'rtg_na']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('CartPole Evaluation Average Return vs Iteration (Small Batch)')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp1_sb.png', bbox_inches='tight')
plt.close()

# Experiment 1 LB
filenames = [
    'experiment_csv/run-q1_lb_no_rtg_dsa_CartPole-v0_26-09-2021_14-43-00-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q1_lb_rtg_dsa_CartPole-v0_26-09-2021_14-47-51-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q1_lb_rtg_na_CartPole-v0_26-09-2021_14-50-29-tag-Eval_AverageReturn.csv'
]

labels = ['no_rtg_dsa', 'rtg_dsa', 'rtg_na']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('CartPole Evaluation Average Return vs Iteration (Large Batch)')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp1_lb.png', bbox_inches='tight')
plt.close()

# Experiment 2
filenames = [
    'experiment_csv/run-q2_b160_r1e-2_InvertedPendulum-v2_26-09-2021_17-34-09-tag-Eval_AverageReturn.csv'
]

labels = ['b=160, r=1e-2']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('InvertedPendulum Evaluation Average Return vs Iteration (b=160, r=1e-2)')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp2.png', bbox_inches='tight')
plt.close()
