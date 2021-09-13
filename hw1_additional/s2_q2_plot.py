import matplotlib.pyplot as plt

iter = range(10)

y_ant = [4239.76611328125, 4211.13720703125, 3582.1630859375, 4675.42333984375, 4644.64404296875, 4624.2470703125,
4771.56396484375, 4744.22705078125, 4642.92431640625, 4658.53271484375
]
y_ant_err = [1171.5499267578125, 1107.8427734375, 1830.81103515625, 78.54283905029297, 56.10521697998047, 75.4908218383789,
71.2324447631836, 98.22396850585938, 94.6432876586914, 63.87786865234375
]

y_hopper = [737.0838623046875, 952.28125, 1620.892822265625, 2446.82958984375, 3718.682373046875, 3716.76025390625,
3763.632080078125, 3771.596923828125, 3783.31298828125, 3649.211669921875
]

y_hopper_err = [318.48919677734375, 232.41075134277344, 406.3905334472656, 731.8165893554688, 34.713985443115234, 36.37590789794922,
8.01700210571289, 9.33271312713623, 6.30246639251709, 456.38433837890625
]

plt.errorbar(iter, y_ant, yerr=y_ant_err, fmt='-o', label='DAgger Agent')
plt.hlines(4713.6533203125, 0, 9, colors=['green'], linestyles=['dashed'], label='Expert Policy')
plt.hlines(4239.77, 0, 9, colors=['red'], linestyles=['dashed'], label='BC Agent')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Return')
plt.title('Ant Task DAgger Iteration vs. Evaluation Return')

plt.legend(bbox_to_anchor=(1.35, 1))

plt.savefig('s2q2_ant.jpg', bbox_inches='tight')
plt.close()

plt.errorbar(iter, y_hopper, yerr=y_hopper_err, fmt='-o', label='DAgger Agent')
plt.hlines(3772.67041015625, 0, 9, colors=['green'], linestyles=['dashed'], label='Expert Policy')
plt.hlines(737.08, 0, 9, colors=['red'], linestyles=['dashed'], label='BC Agent')
plt.xlabel('Iteration #')
plt.ylabel('Evaluation Return')
plt.title('Hopper Task DAgger Iteration vs. Evaluation Return')

plt.legend(bbox_to_anchor=(1.05, 1))

plt.savefig('s2q2_hopper.jpg', bbox_inches='tight')
plt.close()
