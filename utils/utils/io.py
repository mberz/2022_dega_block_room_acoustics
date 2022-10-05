import numpy as np
from scipy.io import loadmat
import pyfar as pf


def ita_ifft(data, signaltype, n_samples=None):
    """ Calculate the IFFT as done in the ITA-Toolbox for MATLAB
    The signal is assumed to be real valued in the time domain, therefore
    only the right sided spectrum is required here. Further, the frequency
    domain data is defined as its effective value inside the ITA-Toolbox
    for MATLAB, requiring a multiplication by sqrt(2) when applying the IFFT.

    Notes
    -----
        Currently only supports even numbers of samples

    Parameters
    ----------
    data : ndarray
        Data in the frequency domain
    signaltype : string
        Signal type, can either be an energy or a power signal

    Returns
    -------
    data : ndarray
        Data in the time domain

    """
    if n_samples is None:
        n_samples = 2*(data.shape[0] - 1)

    n_samples_is_even = ((n_samples % 2) == 0)

    if signaltype == 'power':
        data *= n_samples
        if n_samples_is_even:
            data[-1, :] = data[-1, :] * np.sqrt(2)
            data[1:-2, :] = data[1:-2, :] / np.sqrt(2)
        else:
            data[1:-1, :] = data[1:-1, :] / np.sqrt(2)
    return np.fft.irfft(data, axis=0)


def read_ita(filename):
    """Read .ita audio files. The standard audio file format of the
    ITA-Toolbox for MATLAB. This function returns the time data of the signal
    regardless of the domain the signal was stored in inside the file.

    Notes
    -----
        This function currently only works with .ita files saved in the MATLAB
        file format with versions v4, v6, and v7 to v7.2. Version v7.3 MATLAB
        files are not supported yet.

    Parameters
    ----------
    filename : string
        Name of the file to be read

    Returns
    -------
    data : ndarray, double
        Time data stored in the file
    samplingrate : integer
        Sampling rate of the signal
    type : string
        Signal type, can either be an energy or a power signal

    """
    matfile = loadmat(
        filename, struct_as_record=False, squeeze_me=True, appendmat=False)
    mfiledata = matfile['ITA_TOOLBOX_AUDIO_OBJECT']


    if mfiledata.domain == 'time':
        data = mfiledata.data
        try:
            samplingrate = mfiledata.samplingRate
        except AttributeError:
            times = mfiledata.abscissa
            return pf.TimeData(data.T, np.squeeze(times))

    elif mfiledata.domain == 'freq':
        data = ita_ifft(mfiledata.data, mfiledata.signalType)
        try:
            samplingrate = mfiledata.samplingRate
        except AttributeError:
            freqs = mfiledata.abscissa
            return pf.FrequencyData(data.T, np.squeeze(freqs))

    if mfiledata.signalType == 'energy':
        norm = 'none'
    else:
        norm = 'rms'

    return pf.Signal(data.T, samplingrate, fft_norm=norm)
