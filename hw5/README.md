## Question 1 Subpart 1

Commands used:
```
python cs285/scripts/run_hw5_expl.py --env_name PointmassEasy-v0 --use_rnd \
--unsupervised_exploration --exp_name q1_env1_rnd

python cs285/scripts/run_hw5_expl.py --env_name PointmassEasy-v0 \
--unsupervised_exploration --exp_name q1_env1_random

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--unsupervised_exploration --exp_name q1_env2_rnd

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 \
--unsupervised_exploration --exp_name q1_env2_random
```

## Question 1 Subpart 2

Commands used:
```
python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 \
--unsupervised_exploration --use_custom --exp_name q1_alg_med

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 \
--unsupervised_exploration --use_rnd --exp_name q1_alg_med_rnd

python cs285/scripts/run_hw5_expl.py --env_name PointmassHard-v0 \
--unsupervised_exploration --use_custom --exp_name q1_alg_hard

python cs285/scripts/run_hw5_expl.py --env_name PointmassHard-v0 \
--unsupervised_exploration --use_rnd --exp_name q1_alg_hard_rnd
```

## Question 2 Subpart 1

Commands used:
```
python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --exp_name q2_dqn \
--use_rnd --unsupervised_exploration --offline_exploitation --cql_alpha=0

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --exp_name q2_cql \
--use_rnd --unsupervised_exploration --offline_exploitation --cql_alpha=0.1
```


## Question 2 Subpart 2

Commands used:
```
python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=5000 --offline_exploitation --cql_alpha=0.1 \
--unsupervised_exploration --exp_name q2_cql_numsteps_5000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=8000 --offline_exploitation --cql_alpha=0.1 \
--unsupervised_exploration --exp_name q2_cql_numsteps_8000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=11000 --offline_exploitation --cql_alpha=0.1 \
--unsupervised_exploration --exp_name q2_cql_numsteps_11000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=14000 --offline_exploitation --cql_alpha=0.1 \
--unsupervised_exploration --exp_name q2_cql_numsteps_14000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=5000 --offline_exploitation --cql_alpha=0.0 \
--unsupervised_exploration --exp_name q2_dqn_numsteps_5000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=8000 --offline_exploitation --cql_alpha=0.0 \
--unsupervised_exploration --exp_name q2_dqn_numsteps_8000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=11000 --offline_exploitation --cql_alpha=0.0 \
--unsupervised_exploration --exp_name q2_dqn_numsteps_11000

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--num_exploration_steps=14000 --offline_exploitation --cql_alpha=0.0 \
--unsupervised_exploration --exp_name q2_dqn_numsteps_14000
```


## Question 2 Subpart 3

Commands used:
```
python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--unsupervised_exploration --offline_exploitation --cql_alpha=0.02 \
--exp_name q2_alpha_0.02

python cs285/scripts/run_hw5_expl.py --env_name PointmassMedium-v0 --use_rnd \
--unsupervised_exploration --offline_exploitation --cql_alpha=0.5 \
--exp_name q2_alpha_0.5
```