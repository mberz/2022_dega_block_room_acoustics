# %%
import os
from glob import glob
import pyfar as pf
from utils.io import read_ita

# %%
data_folder = '../data/'

file_names = glob(data_folder + '*.ita')

for file_name in file_names:
    data = read_ita(file_name)
    pf.io.write_audio(
        data,
        os.path.splitext(file_name)[0] + ".wav"
    )
