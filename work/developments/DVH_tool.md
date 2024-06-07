### Installing the ODN ProKnow Toolkit

- Downlaod the DVH tool (I have a [fork of the repository here](https://github.com/GrahamArden/YHODN-ProKnow-Toolkit))
- Extract into a suitable directory
- Make a copy of the T&F group repository in the `prowknow_scripting_tandf` directory
- Open a terminal, navigate to the repository and to the `DVH_tool` subdirectory

- Create a virtual environmet to run the tool in (it does requrie a number of non standard libraries)

```bash
python -m venv venv
```

- Activate the virtual environment
- 
```bash
venv\Scripts\activate
```

- Change to the DVH_tools subdirectory and run ```pip install``` against the requirements file

```bash
python -m pip install -r requirements.txt
```
- Run streamlit with the `stremlit_dvh_tool.py` script
```bash
streamlit run streamlit_dvh_tool.py
```
- To deactivate the virtual environment and return to the base distribution run:
```bash
deactivate
```
