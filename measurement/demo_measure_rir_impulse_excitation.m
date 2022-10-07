%% Use MSRecord to record impulse responses
%  Record for pre-defined duration
MS = itaMSRecord();
MS.samplingRate = ita_preferences('samplingRate');
MS.fftDegree = 20;
MS.inputChannels = 1;

%% Rec
RIR_rec = MS.run;
RIR_rec = RIR_rec.ch(1);

%% save to disk
ita_write_ita(ita_ifft(RIR_rec), 'RIR_rec_impulse.ita', 'overwrite')
