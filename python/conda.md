#### Conda

Both the full [anaconda distribution](https://www.anaconda.com/download) and [miniconda](https://docs.anaconda.com/free/miniconda/) can use conda to manage updates etc.

A full guide to using conda is available [here](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-conda.html#)

To update conda itself use:
```
conda update conda
```

To update all the packages currently installed use:

```
conda update --all
```
This will pull from all the channels currently defined in the .condarc file.

Both anaconda and miniconda can also use pip to install or update packages
