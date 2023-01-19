# sGrids

Streamlit + AgGrid = Real time edit to Source 

### Decription

This is a small project to create Streamlit dashboards capable of 
- Editing a csv and saving to source in real time
- Displaying dynamically generated clickable buttons in cells for opening links
- (more features to come)

### How to run locally

- Create conda env / pip venv
- Install `streamlit` -> follow https://pypi.org/project/streamlit/
- Install `streamlit-aggrid` -> follow https://pypi.org/project/streamlit-aggrid/
- Add this `editable_grid.py` and `data.csv` to same folder
- In terminal/prompt, activate environment and navigate to folder
- Run `streamlit run editable_grid.py`

### How to run via github

- (Download Data)[https://github.com/Akshaysehgal2005/sGrids/blob/main/data.csv]
- Navigate to folder with download
- Run `streamlit run https://github.com/Akshaysehgal2005/sGrids/blob/main/editable_grid.py`
