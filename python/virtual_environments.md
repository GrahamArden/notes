### Using Python Virtual Environments 

- Create a virtual environment in the directory ```.venv```

```bash
python -m venv .venv
```

- Activate the virtual environment

```bash
.venv\Scripts\activate
```

- Change to the DVH_tools subdirectory and run ```pip install``` against the requirements file

```bash
python -m pip install -r requirements.txt
```

- To deactivate the virtual environment and return to the base distribution run:
```bash
deactivate
```
