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

# Experiment 3
filenames = [
    'experiment_csv/run-q3_b40000_r0.005_LunarLanderContinuous-v2_26-09-2021_23-30-31-tag-Eval_AverageReturn.csv'
]

labels = ['PG Agent']

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('LunarLander Evaluation Average Return vs Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp3.png', bbox_inches='tight')
plt.close()

# Experiment 4 search
filenames = [
    'experiment_csv/run-q4_search_b10000_lr0.005_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-07-06-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b10000_lr0.01_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-07-28-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b10000_lr0.02_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-07-48-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b30000_lr0.005_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-08-02-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b30000_lr0.01_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-08-18-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b30000_lr0.02_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-08-32-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b50000_lr0.005_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-08-51-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b50000_lr0.01_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-09-02-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_search_b50000_lr0.02_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-09-13-tag-Eval_AverageReturn.csv'
]

labels = [
    'b=10000, lr=0.005',
    'b=10000, lr=0.01',
    'b=10000, lr=0.02',
    'b=30000, lr=0.005',
    'b=30000, lr=0.01',
    'b=30000, lr=0.02',
    'b=50000, lr=0.005',
    'b=50000, lr=0.01',
    'b=50000, lr=0.02'
]

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('HalfCheetah Hyperparameter Search Evaluation Average Return vs Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp4_search.png', bbox_inches='tight')
plt.close()

# Experiment 4 optimal param trials
filenames = [
    'experiment_csv/run-q4_b50000_r0.02_HalfCheetah-v2_27-09-2021_03-34-21-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_b50000_r0.02_rtg_HalfCheetah-v2_27-09-2021_03-34-37-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_b50000_r0.02_nnbaseline_HalfCheetah-v2_27-09-2021_03-34-48-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q4_b50000_r0.02_rtg_nnbaseline_HalfCheetah-v2_27-09-2021_03-35-01-tag-Eval_AverageReturn.csv'
]

labels = [
    'no rtg, no nn_baseline',
    'rtg, no nn_baseline',
    'no rtg, nn_baseline',
    'rtg, nn_baseline'
]

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('HalfCheetah Optimal Parameter Trials Evaluation Average Return vs Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp4_opt.png', bbox_inches='tight')
plt.close()

# Experiment 5
filenames = [
    'experiment_csv/run-q5_b2000_r0.001_lambda0_Hopper-v2_27-09-2021_02-59-10-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q5_b2000_r0.001_lambda0.95_Hopper-v2_27-09-2021_02-59-17-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q5_b2000_r0.001_lambda0.99_Hopper-v2_27-09-2021_02-59-23-tag-Eval_AverageReturn.csv',
    'experiment_csv/run-q5_b2000_r0.001_lambda1_Hopper-v2_27-09-2021_02-59-06-tag-Eval_AverageReturn.csv'
]

labels = [
    'lambda=0',
    'lambda=0.95',
    'lambda=0.99',
    'lambda=1'
]

for filename, label in zip(filenames, labels):
    data = pd.read_csv(filename)
    plt.plot(data['Step'], data['Value'], label=label)

plt.title('Hopper Evaluation Average Return vs Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Average Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('plots/exp5.png', bbox_inches='tight')
plt.close()
