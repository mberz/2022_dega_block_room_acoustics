

MS = itaMSTF;
MS.samplingRate = ita_preferences('samplingRate');
MS.fftDegree = 16;
MS.inputChannels = 1;
MS.outputChannels = 1;
MS.outputamplification = -30;


%
decay_time_to_record = 1.5; % T60 is roughly 6 seconds
time_constant_smoothing = 0.2/20; % 1s/20 ISO 354
smoothing_filter_samples = round(time_constant_smoothing*MS.samplingRate);

%%
MS.outputamplification = -1;


%%
[edc_noise_10_smoothed, recorded_decay] = lab_measure_edc_direct(MS, decay_time_to_record, 'n_averages', 10, 'smoothing_filter_samples', smoothing_filter_samples);

%%
ita_write_ita(edc_noise_10_smoothed, 'EDC_direct.ita', 'overwrite')
ita_write_ita(recorded_decay, 'recorded_decay.ita', 'overwrite')


%%

edc_noise = merge(edc_noise_1, edc_noise_3, edc_noise_10);
ita_plot_time_dB(edc_noise, 'linewidth', 2)

%%
lab_reverberation_time_regression_manual(edc_noise_3)

%%
m = -83.2704
n = 5

edc = -60
T_20 = (edc - n)/m;