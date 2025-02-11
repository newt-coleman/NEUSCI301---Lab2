import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

steps = np.array([0,1,2,3])
v_max = np.array([61.16, 70-38.35, 70-52.14, 70 - 57.66])

def sumSquaredError(a,b,r):
    y = lambda t: a + b*np.exp(r*t)    # Define the model y
    error = sum(np.abs(y(steps) - v_max)**2)     # Compute the error using sum-of-squared error
    return error

adapter = lambda p: sumSquaredError(p[0], p[1], p[2])
guess = np.array([0, 61.16, 1])

fit = scipy.optimize.fmin(adapter, guess)
print(fit)

t = np.linspace(0, 4)
lam = np.sqrt(22/10)
plt.plot(steps, v_max, 'o')
plt.plot(t, fit[0] + fit[1]*np.exp(fit[2]*t), label="Fitted exponential", color = 'tab:blue')
plt.plot(t, 61.16*np.exp(-t/lam), "--", label="Predicted exponential")
plt.xticks(steps)
plt.legend()
plt.show()

plt.rcParams['font.size'] = 13
time = np.array([0.262, 0.55, 0.101])
plt.bar([1, 2, 3], time, tick_label = ["Low $R_a$", "Simultaneous input", "Proximal input"])
plt.xlabel("Conditions to overcome threshold")
plt.ylabel("Time to reach threshold (s)")
plt.show()