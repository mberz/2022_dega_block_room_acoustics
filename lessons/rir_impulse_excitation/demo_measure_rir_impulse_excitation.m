%% Use MSRecord to record impulse responses
%  Record for pre-define duration
MS = itaMSRecord();
MS.samplingRate = ita_preferences('samplingRate');
MS.fftDegree = 19.5;
MS.inputChannels = 1;

%% Rec
RIR_rec = MS.run;
RIR_rec = RIR_rec.ch(1);

%% save to disk
ita_write_ita(ita_ifft(RIR_rec), 'RIR_rec_impulse.ita', 'overwrite')

%%























































%% backup

%% Find peaks of respective room impulse responses
RIR_rec = ita_mpb_filter(RIR_rec, [50, MS.samplingRate/2]);
RIR_rec_normalized = ita_normalize_dat(RIR_rec);
peak_dist = 0.6;
[peaks, time_peaks] = findpeaks(RIR_rec_normalized.timeData, RIR_rec.timeVector, 'MinPeakDistance', peak_dist, 'MinPeakHeight', 10^(-20/20));

%% Plot the estimated peaks and their occurence
RIR_rec.ptd
ZL = zlim();
hold on
for idx=1:numel(time_peaks)
    x = time_peaks(idx);
    plot([x x], [-300, 300], 'k', 'Linewidth', 2, 'Linestyle', '-.')
end

%% Cropping parameters
time_before_impulse = 0.25;
expected_rt = .6;
start_sample_rirs = time_peaks - time_before_impulse;
end_sample_rirs = time_peaks + expected_rt;

%% Crop the RIRs and merge
RIRs_cropped = [itaAudio()];

for idx = 1:numel(time_peaks)
    crop_times = [start_sample_rirs(idx), end_sample_rirs(idx)];
    RIR_cropped = ita_time_crop(RIR_rec, crop_times);
    RIR_norm = ita_normalize_dat(RIR_cropped);
    RIR_norm_shifted = ita_time_shift(RIR_norm, '20db');
    RIRs_cropped(idx) = RIR_norm_shifted;
end

RIRs = merge(RIRs_cropped);
RIRs.ptd

%% Calculate EDCs and T_20s
band = 1000;
RA = ita_roomacoustics(RIRs, 'T20', 'EDC', 'edcmethod', 'nocut', 'freqRange', band*[0.99, 1.01]);
EDC = merge(RA.EDC);

%% Plot the EDCs
EDC.ptd


RT = RA.T20;
%% Plot the T_20 values
figure()
ax1 = subplot(1, 2, 1);
scatter(1:numel(RT.freqData), RT.freqData, 'filled')
grid();
ax = gca();
set(ax, 'XTick', 1:numel(RT.freqData))
xlabel('Measurement No.')
ylabel('T_{20} in s')
ax2 = subplot(1, 2, 2);
boxplot(RT.freqData);
grid();
linkaxes([ax1, ax2], 'y')



%% Save data for later
save(fullfile('data', 'RA_impulse_source.mat'), 'RA');
%%
ita_write_ita(RIR_rec, ['data/RIR_rec_impulse_office.ita'])
