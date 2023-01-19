import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, JsCode


# df = pd.DataFrame(
#     {   "col":[1,2],
#         "url": [
            
#             f'<form action="https://google.com" target="_blank"><input type="submit" value="Click Here" /></form>',
#             f'<form action="https://google.com" target="_blank"><input type="submit" value="Click Here" /></form>'
#         ],
#         "label": ["question", "question"]
#     }
# )


df = pd.DataFrame(
    {   "col":[1,2],
        "url": ["https://google.com","https://stackoverflow.com"],
        "label": ["question", "question"]
    }
)

#cellrender1 = lambda x: '<form action="{x}" target="_blank"><input type="submit" value="Click Here" /></form>'


cellRenderer1 = JsCode('''function(params) {return '<form action='+params.value+'
                                                          target="_blank"><input type="submit" 
                                                          value="Link to file" /></form>'}'''
                     )

#"https://www.google.com/' + params.value + '"

# cellRenderer2 = JsCode('''function(params) {return '<a href="https://www.google.com" target="_blank">params.value</a>'}''')
# cellRenderer3 = JsCode('''function(params) {return '<input type="button" 
#                                                            onclick="location.href=params.value;" 
#                                                            value="Go to Google" />'}'''
#                       )


# cellRenderer4 = JsCode('''function(params) {return '<a href='+params.value+' target="_blank">'+ params.value+'</a>'}''')


grid_options = {
    "columnDefs": [
        {
            "headerName": "col",
            "field": "col",
            "editable": True,
        },
        {
            "headerName": "url",
            "field": "url",
            "editable": False,
            "cellRenderer": cellRenderer1,
            "autoHeight":True
        },
        {
            "headerName": "label",
            "field": "label",
            "editable": False,
        },
    ],
}

AgGrid(df, grid_options, allow_unsafe_jscode=True)



#st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)










# import streamlit as st
# import pandas as pd
# from st_aggrid import AgGrid

# df = pd.DataFrame(['http://google.com', 
#                    'http://duckduckgo.com'])

# df = pd.DataFrame({"col1": [1, 2, 3], "col2": ['http://google.com', 'http://google.com', 'http://google.com']})

# grid_options = {
#     "columnDefs": [
#         {
#             "headerName": "col1",
#             "field": "col1",
#             "editable": True,
#         },
#         {
#             "headerName": "col2",
#             "field": "col2",
#             "editable": False,
#         },
#     ],
# }


# AgGrid(df, grid_options)