# %%
%matplotlib widget
import pyrato
import pyfar as pf
import numpy as np
import matplotlib.pyplot as plt
from utils.io import read_ita
from scipy.signal import find_peaks

# %%
EDC_direct = read_ita('EDC_direct.ita')


# %%
plt.figure()
pf.plot.time(EDC_direct, dB=True, log_prefix=10)
# %%
plt.figure()
pf.plot.time(pf.dsp.average(EDC_direct), dB=True, log_prefix=10)
# %%
# %%
reverberation_times, intercept = pyrato.reverberation_time_linear_regression(
    pf.dsp.average(EDC_direct), return_intercept=True)

# %%
edc_model = 10*np.log10(intercept*np.exp(-13.8*EDC_direct.times/reverberation_times[0]))

plt.figure()
ax = pf.plot.time(pf.dsp.average(EDC_direct), dB=True, log_prefix=10)
ax.plot(EDC_direct.times, edc_model)
