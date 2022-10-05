function varargout = lab_smooth_edc(varargin)
    sArgs = struct('pos1_edc', 'itaAnything', 'time_constant_samples', 512);
    [edc, sArgs] = ita_parse_arguments(sArgs, varargin);

    bs = round(sArgs.time_constant_samples);
    throwAway = 0;
    nFrames = floor(edc.nSamples/bs);
    tmp = reshape(edc.time((throwAway*bs+1):nFrames*bs),[bs nFrames-throwAway]);
    nFrames = nFrames-throwAway;
    energyVals = mean(tmp.^2);

    times = edc.timeVector(1:bs:nFrames*bs);
    edc_smooth = itaResult(energyVals.', times, 'time');
    edc_smooth.channelUnits = {'Pa^2'};
    varargout{1} = edc_smooth;
end