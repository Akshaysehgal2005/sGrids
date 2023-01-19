# from st_aggrid import AgGrid, GridUpdateMode, DataReturnMode, GridOptionsBuilder
# import pandas as pd
# import streamlit as st

# st.set_page_config(layout="wide")

# df = pd.read_csv('data.csv')

# gb = GridOptionsBuilder.from_dataframe(df)
# gb.configure_default_column(editable=True)   

# out = AgGrid(df, 
#              update_mode = GridUpdateMode.VALUE_CHANGED, 
#              #data_return_mode = DataReturnMode.AS_INPUT,
#              gridOptions=gb.build(),
#              #reload_data=True
#              )

# df = out['data']
# df.to_csv('data.csv', index=False)

# st.write()

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

#df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})  # Original csv
df = pd.read_csv('sample.csv')

grid_options = {
    "columnDefs": [
        {
            "headerName": "col1",
            "field": "col1",
            "editable": True,
        },
        {
            "headerName": "col2",
            "field": "col2",
            "editable": False,
        },
    ],
}

grid_return = AgGrid(df, grid_options, key='df', allow_unsafe_jscode=True)
df = grid_return["data"]

df.to_csv('sample.csv', index=False) #Overwrite sample.csv

## CHECK IF SAMPLE CSV IS UPDATED ##
df = pd.read_csv('sample.csv')
st.write(df)