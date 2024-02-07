### Developments

I am currently working on the use of [Proknow](proknow/README.md) and am a memnber of the [ProKnow scripting Task and Finish group](https://github.com/nhs-proknow)

As part of this we are looking at installing [miniconda](../python/conda.md) within the VLAN so that scripts can be run directly against both ARIA and Proknow

Miniconda was chosen, rather than using the full anaconda distribution as it has a much small footprint and we can install only the necessary packages

In addition to the base libraries we would require

- Juyter, both notebook and lab frontends
- Spyder
- The packages [listed here](https://github.com/nhs-proknow/proknow-scripting-tandf/blob/main/requirements.txt) which include the [Python ProKnow SDK](https://proknow-python.readthedocs.io/en/latest/)

Note that because the VLAN has no connection to the internet it would need to be used [offline](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/installing-with-conda.html#installing-conda-packages-offline)


[up](README.md)
[top](../README.md)
