## Graphs and Tables

To generate all graphs and tables, run
```
python visualize.py
```

## Question 1

Command used:
```
python cs285/scripts/run_hw3_dqn.py --env_name MsPacman-v0 --exp_name q1
```

## Question 2

Commands used:
```
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_1 --seed 1
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_2 --seed 2
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_3 --seed 3
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_1 --double_q --seed 1
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_2 --double_q --seed 2
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_3 --double_q --seed 3
```

## Question 3

The hyperparameter varied was the lander exploration schedule. To vary this, the `lander_exploration_schedule` function
was modified. Specifically, the multiplier on `num_timesteps` was changed (by default, it is 0.1).
- For `q3_hparam0`, default values were used (multiplier 0.1)
- For `q3_hparam1`, the multiplier for `num_timesteps` was changed to 0.2
- For `q3_hparam2`, the multiplier for `num_timesteps` was changed to 0.3
- For `q3_hparam3`, the multiplier for `num_timesteps` was changed to 0.4

Commands used:
```
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam0
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam1
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam2
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam3
```