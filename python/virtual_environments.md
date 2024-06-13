### Using Python Virtual Environments 

- Navigate to the folder containing your python code
- Create a virtual environment in the directory ```.venv```

```bash
python -m venv .venv
```

- Activate the virtual environment

```bash
.venv\Scripts\activate
```

- If the source code folder contains a `requirements.txt` file, run ```pip install``` against the requirements file

```bash
python -m pip install -r requirements.txt
```

- To deactivate the virtual environment and return to the base distribution run:
```bash
deactivate
```
