import matplotlib.pyplot as plt

x = [500 + 50 * i for i in range(15)]
y = [471.43, 553.94, 811.19, 536.71, 610.69, 1069.88, 1008.02, 620.74, 770.20, 867.55, 737.08, 1080.35, 768.32, 466.55, 825.02]
y_err = [153.02, 259.99, 386.39, 250.98, 261.13, 252.26, 258.79, 245.49, 313.64, 305.06, 318.49, 220.50, 227.65, 98.10, 316.78]

plt.errorbar(x, y, yerr=y_err, fmt='--', ecolor='green')
plt.plot(x, y, marker='o')
plt.xlabel('Number of Training Gradient Steps')
plt.ylabel('Evaluation Return')
plt.title('Training Gradient Steps vs. Evalulation Return')

plt.savefig('s1q3.jpg')
