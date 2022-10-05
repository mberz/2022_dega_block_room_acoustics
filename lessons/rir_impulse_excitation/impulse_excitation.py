# %%
%matplotlib widget
import pyrato
import pyfar as pf
import numpy as np
import matplotlib.pyplot as plt
from utils.io import read_ita
from scipy.signal import find_peaks

# %%
RIRs_impulse = read_ita('RIR_rec_impulse.ita')
sampling_rate = RIRs_impulse.sampling_rate
RIRs_impulse = pf.dsp.normalize(RIRs_impulse)
# %%
plt.figure()
pf.plot.time(RIRs_impulse, dB=True)
# %%
peak_distance = 0.6*sampling_rate
peaks = find_peaks(
    np.squeeze(RIRs_impulse.time),
    threshold=10**(-20/20),
    distance=peak_distance)[0]

t_peaks = peaks/sampling_rate

# %%
plt.figure()
ax = pf.plot.time(RIRs_impulse, dB=True)
for t_peak in t_peaks:
    ax.axvline(t_peak, linestyle=':', color='k')

# %%
time_before_impulse = 0.1
expected_rt = .6
start_sample_rirs = ((t_peaks - time_before_impulse)*sampling_rate).astype(int)

n_samples = np.min(
    np.diff(np.r_[0, start_sample_rirs, RIRs_impulse.n_samples]))
data = np.zeros((len(peaks), n_samples), float)

for ch, start_sample in enumerate(start_sample_rirs):
    end_sample = start_sample + n_samples
    data[ch] = RIRs_impulse.time[0, start_sample:end_sample]

RIRs_cropped = pf.Signal(data, sampling_rate)
# %%
plt.figure()
pf.plot.time(RIRs_cropped, dB=True)


# %%
bands = [250, 1e3, 4e3]
band = bands[1]
RIRs_bandpass = pf.dsp.filter.fractional_octave_bands(
    RIRs_cropped, 1, freq_range=np.array([0.9, 1.1])*band)
# %%
plt.figure()
pf.plot.time(RIRs_bandpass, dB=True)
# %%

int_times = pyrato.intersection_time_lundeby(RIRs_bandpass[0], freq=band)[0]
edcs = pyrato.energy_decay_curve_chu_lundeby(RIRs_bandpass, freq=band, normalize=True)

# %%
plt.figure()
ax = pf.plot.time(edcs, log_prefix=10, dB=True)
ax.set_xlim(0, np.min(int_times))
# %%
reverberation_times = pyrato.reverberation_time_linear_regression(edcs)
# %%
rt_mean = np.mean(reverberation_times)
rt_std = np.std(reverberation_times)

plt.figure()
ax = plt.axes()
ax.scatter(np.arange(0, reverberation_times.size), reverberation_times)
ax.scatter(reverberation_times.size, rt_mean, color='k', label=f'Mean: {rt_mean:.2f} s')
ax.errorbar(reverberation_times.size, rt_mean, rt_std, color='k', barsabove=True, label=f'Std: $\pm${rt_std:.2f} s')
ax.grid(True)
ax.legend()
# ax.set_ylim(0.3, 1)

# %%
print(f"Relative std. {(rt_std/rt_mean*100):.2f} %")
# %%

