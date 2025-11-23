import pandas as pd 
import plotly.express as px # pip install plotly
import streamlit as st # pip install streamlit


# ---- PAGE TITLE ----
st.markdown(
    "<h1 style='text-align: center;'>Penn World Table Data Viewer</h1>",
    unsafe_allow_html=True
)


# ---- READ DATA ----
df_panel = pd.read_excel(
    io='gdppaneldata.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1'
)


# ---- Helper: multiselect with 'All' option ----
def multiselect_with_all(label, options, key):
    """
    Streamlit multiselect with an 'All' option.

    - If 'All' is selected OR nothing is selected → returns full list.
    - Otherwise → returns the selected subset.
    """
    options = list(options)
    display_options = ["All"] + options

    selected = st.sidebar.multiselect(
        label,
        options=display_options,
        default=["All"],
        key=key,
    )

    if "All" in selected or len(selected) == 0:
        return options
    else:
        # remove 'All' if user somehow left it with others
        return [x for x in selected if x != "All"]


# ---- Sidebar ----
st.sidebar.header("Please Filter Here:")

country = multiselect_with_all(
    "Select the Country:",
    options=sorted(df_panel["country"].unique()),
    key="country_filter"
)

region = multiselect_with_all(
    "Select the Region:",
    options=df_panel["region"].unique(),
    key="region_filter"
)

year = multiselect_with_all(
    "Select the Year:",
    options=sorted(df_panel["year"].unique()),
    key="year_filter"
)   

# --- Filtering Dataframe based on selections ---
df_selection = df_panel.query(
    "country == @country & region == @region & year == @year"
)


# --- DISPLAY DATAFRAME ---
st.dataframe(df_selection)