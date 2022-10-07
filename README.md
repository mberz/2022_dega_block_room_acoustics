# Accompanying Notebooks for the Tutorial on Acoustic Measurements
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mberz/2022_dega_block_room_acoustics/HEAD?labpath=index.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/mberz/2022_dega_block_room_acoustics/blob/main/index.ipynb)

The notebooks can be run interactively or simply viewed in a static version.

1. [Interactive online access](https://mybinder.org/v2/gh/mberz/2022_dega_block_room_acoustics/HEAD?labpath=index.ipynb). It may take a couple of minutes to start the online environment.
2. [Static online access](https://nbviewer.org/github/mberz/2022_dega_block_room_acoustics/blob/main/index.ipynb). There's no wait time here, but it's not interactive.



## License and Contributing

The content is provided as [Open Educational Resource](https://en.wikipedia.org/wiki/Open_educational_resources). The Jupyter notebooks and respective Python code are licensed under the open source [MIT license](https://opensource.org/licenses/MIT); Audio (*.ita and *.wav) files are licensed under the [Creative Commons 4.0](https://creativecommons.org/licenses/by/4.0/) license.


##  Local Installation using conda

To create the environment and open locally run the following commands in the terminal:

```
conda env create -f environment.yml --prefix ./env/2022_dega_block_room_acoustics/
conda activate ./env/2022_dega_block_room_acoustics
jupyter lab index.ipynb
```
