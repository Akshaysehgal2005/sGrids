import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, JsCode

st.set_page_config(layout='wide')

st.title('Editable tables with link buttons')
st.markdown('- This is a demo for an editable table, with the field "CHECKED" set to editable. On any edit, the table is saved directly to source in realtime (data.csv)')
st.markdown('- The code also contains clickable buttons loaded as JS functions in each cell of "LINK" column')

#Load data
df = pd.read_csv('data.csv')

#JS button function
cellRenderer1 = JsCode('''
                       function(params) 
                           {
                           return '<form action='+params.value+' target="_blank">
                                       <input type="submit" value="Link to file" />
                                   </form>'
                           }
                       '''
                     )

#Build grid options dictionary
def build_gb(df, hidden=[], editable=[], buttons=[]):
    coldefs = [{'headerName':i,'field':i} for i in df.columns if i not in hidden]
    _ = [i.update({'editable':True}) for i in coldefs if i['field'] in editable]
    _ = [i.update({'cellRenderer':cellRenderer1.js_code, 
                   'autoHeight': True}) for i in coldefs if i['field'] in buttons]
    grid_options = {"columnDefs": coldefs}
    return grid_options

hidden = ['incidents_85_99', 'fatal_accidents_85_99', 'fatalities_85_99']
editable = ['Checked']
buttons = ['Link']
grid_options = build_gb(df, hidden, editable, buttons)

#Generate table
grid_return = AgGrid(df, grid_options, key='df', allow_unsafe_jscode=True, fit_columns_on_grid_load=True)

#Save to source on edit
df = grid_return["data"]
df.to_csv('data.csv', index=False)