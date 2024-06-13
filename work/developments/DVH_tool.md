### Installing the YHODN ProKnow Toolkit

- Downlaod the DVH tool (I have a [fork of the repository here](https://github.com/GrahamArden/YHODN-ProKnow-Toolkit))
- Extract into a suitable directory
- Make a copy of the T&F group repository in the `prowknow_scripting_tandf` directory
- Open a terminal, navigate to the repository and to the `DVH_tool` subdirectory
- Create a virtual environmet to run the tool in (it does requrie a number of non standard libraries)

```bash
python -m venv venv
```

- Activate the virtual environment

```bash
venv\Scripts\activate
```

- Change to the DVH_tools subdirectory and run ```pip install``` against the requirements file

```bash
python -m pip install -r requirements.txt
```
- Edit the config file: `Configs/DHH_tool_config.toml` to give the location for your `credentials.json` file
- Create folders for `logs` and `Output` folders. Note the capitalisation of "Output"
- Run streamlit with the `stremlit_dvh_tool.py` script
```bash
streamlit run streamlit_dvh_tool.py
```
- The tool will run, but give an error due to the use of nested double quotes. Edit the appropriate file `streamlit_dvh_tool.py`
- Reload the streamlit page
- There will then be another error due to not being able to find the nhs_proknow modules. Correct this and reload.
- To deactivate the virtual environment and return to the base distribution run:
```bash
deactivate
```
