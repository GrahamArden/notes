### Installing the ODN ProKnow Toolkit

- Downlaod the DVH tool (currently available from the fork at [Marcus's Github page](https://github.com/MTyyger/YHODN-ProKnow-Toolkit))
- Extract into a suitable directory
- Make a copy of the T&F group repository in the `prowknow_scripting_tandf` directory
- Open a terminal, navigate to the repository and to the `DVH_tool` subdirectory

- Create a virtual environmet to run the tool in (it does requrie a number of non standard libraries)
```
python -m venv venv
```

- Activate the virtual environment
```
venv\Scripts\activate
```

- Change to the DVH_tools subdirectory and run ```pip install``` against the requirements file

```
python -m pip install -r requirements.txt
```
- Run streamlit with the `stremlit_dvh_tool.py` script
```
streamlit run streamlit_dvh_tool.py
```
