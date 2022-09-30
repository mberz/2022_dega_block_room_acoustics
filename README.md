# Install

To create the environment run:

```
conda env create -f environment.yml --prefix ./env/2022_dega_block_room_acoustics/
```

and activate using:

```
conda activate ./env/2022_dega_block_room_acoustics
```

The specific environment (potentially very OS specific) can be exported

```
conda env export --prefix ./env/2022_dega_block_room_acoustics --file exact_environment.yml
```

and updated:

```
conda env update --prefix ./env/2022_dega_block_room_acoustics --file exact_environment.yml  --prune
```
