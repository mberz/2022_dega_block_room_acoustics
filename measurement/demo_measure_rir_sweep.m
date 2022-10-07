%% Create the measurement setup
MS = itaMSTF;
MS.inputChannels = 1;
MS.outputChannels = 1;
MS.outputamplification = 5;
MS.fftDegree = 17;


% Run 3 sweep measurements
num_averages = 3;

RIRs = [itaAudio()];

for idx = 1:num_averages
    RIRs(idx) = MS.run;
    pause(0.5);
end

RIRs = merge(RIRs);

%% write files to disk
ita_write_ita(ita_ifft(RIRs), '../data/rir_sweep_fft_17.ita', 'overwrite')
