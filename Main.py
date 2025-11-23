import streamlit as st
import pandas as pd   # <-- add this

# ---------------------------------------
# GLOBAL STYLES
# ---------------------------------------
st.markdown("""
    <style>
        /* Reduce space above the main page */
        .block-container {
            padding-top: 2rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------
# LOAD / SHARE DATA & LABELS ONCE
# ---------------------------------------

# 1) Main PWT data (Sheet1)
if "df_panel" not in st.session_state:
    df = pd.read_excel(
        "gdppaneldata.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1"
    )
    st.session_state["df_panel"] = df

# 2) Variable labels from sheet 'VariableInfo'
#    Expected columns: 'variable' and 'label'
if "labels_dict" not in st.session_state:
    varinfo = pd.read_excel(
        "gdppaneldata.xlsx",
        engine="openpyxl",
        sheet_name="VariableInfo"
    )

    # Build dict: {variable_name: label_text}
    labels_dict = dict(zip(varinfo["variable"], varinfo["label_short"]))
    st.session_state["labels_dict"] = labels_dict

# 3) (Optional) track base columns for custom variable logic
if "base_columns" not in st.session_state:
    st.session_state["base_columns"] = st.session_state["df_panel"].columns.tolist()

if "custom_vars" not in st.session_state:
    st.session_state["custom_vars"] = []  # names of user-created variables


# ---------------------------------------
# PAGE SETUP
# ---------------------------------------
about_page = st.Page(
    page="pages/about.py",
    title="This Project",
    default=True
)

lineplot_page = st.Page(
    page="pages/lineplot.py",
    title="Line Plot"
)

connectedscatterplot_page = st.Page(
    page="pages/connectedscatter.py",
    title="Connected Scatter Plot"
)

scatterplot_page = st.Page(
    page="pages/scatterplot.py",
    title="Scatter Plot"
)

customvariable_page = st.Page(
    page="pages/customvariable.py",
    title="Create Own Variables"
)

data_page = st.Page(
    page="pages/getdata.py",
    title="Get PWT Data"
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(
    pages=[
        about_page,
        lineplot_page,
        scatterplot_page,
        connectedscatterplot_page,
        customvariable_page,
        data_page
    ]
)

# --- SIDEBAR FOOTER ---
st.sidebar.text("By Ahmed Pirzada, Bristol University")

# --- RUN NAVIGATION ---
pg.run()
