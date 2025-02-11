import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

v_vs_a = pd.read_csv("pt_1_vvsa.csv")

incur_10 = np.array(v_vs_a["10_inject"].dropna())
maxv_10 = np.array(v_vs_a["10_mV"].dropna())
incur_5 = np.array(v_vs_a["5_inject"].dropna())
maxv_5 = np.array(v_vs_a["5_mV"].dropna())
print(incur_10)
m_10, c_10 = np.polyfit(maxv_10, incur_10, 1)
m_5, c_5 = np.polyfit(maxv_5, incur_5, 1)

plt.rcParams['font.size'] = 16
plt.plot(maxv_10, incur_10, 'o', color='tab:blue', label="R = 10M$\Omega$")
# plt.plot(maxv_10, m_10*incur_10 + c_10, color='tab:blue')
plt.plot(maxv_5, incur_5, 'o', color='tab:orange', label="R = 5M$\Omega$")
# plt.plot(maxv_5, m_5*incur_5 + c_5, color='tab:orange')

print("Conductance w/ 10mohm: " + str(m_10))
print("Conductance w/ 5mohm: " + str(m_5))

plt.xlabel("Maximum voltage deflection (mV)")
plt.ylabel("Injected current (nA)")
plt.legend()
plt.show()

taus = np.array([0.604, 0.554, 0.512])
taus = taus - 0.5

plt.bar([0.5, 1, 1.5], taus, width =0.4, tick_label = ["10M$\Omega$ 10$\mu$F", "5M$\Omega$ 10$\mu$F", "10M$\Omega$ 1$\mu$F"])
plt.xlabel("RC components")
plt.ylabel("Time constant (s)")
plt.show()