# sGrids

Streamlit + AgGrid = Real time edit to Source 

## Decription

This is a small project to create Streamlit dashboards capable of 
- Editing a csv and saving to source in real time
- Displaying dynamically generated clickable buttons in cells for opening links
- (more features to come)

## Setup environment

- Create conda env / pip venv
- Run `pip install -r requirements.txt`
(You may need to run `xcode-select --install` before the above step for Mac)

Or, from scratch - 

- Create conda env / pip venv
- Install `streamlit` -> follow https://pypi.org/project/streamlit/
- Install `streamlit-aggrid` -> follow https://pypi.org/project/streamlit-aggrid/

## How to run 

For running locally, 

- Clone the repo
- In terminal/prompt, activate environment and navigate to folder
- Run `streamlit run editable_grid.py`

or to run via github, 

- [Download Data](https://github.com/Akshaysehgal2005/sGrids/blob/main/data.csv)
- In terminal/prompt, activate environment and navigate to folder with download
- Run `streamlit run https://github.com/Akshaysehgal2005/sGrids/blob/main/editable_grid.py`

