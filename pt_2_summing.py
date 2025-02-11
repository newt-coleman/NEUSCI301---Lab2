import numpy as np
import matplotlib.pyplot as plt

freq = np.array([10, 15, 20, 25, 30, 35])

low_res = np.array([None, None, 1.38, 0.90, 0.67, 0.58])
high_res = np.array([None, None, 1.08, 0.73, 0.53, 0.47])

plt.rcParams['font.size'] = 17
plt.plot(freq, low_res, 'o-', label="R = 10M$\Omega$")
plt.plot(freq, high_res, 'o-', label="R= 7.8M$\Omega$")

plt.legend()
plt.xlabel("Stimulus frequency (Hz)")
plt.ylabel("Time to reach threshold")
plt.xticks([20, 25, 30, 35])
plt.show()