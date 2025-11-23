import pandas as pd
import plotly.express as px
import streamlit as st


# --- LOAD / SHARE DATA ----
df_panel = st.session_state["df_panel"]
labels_all = st.session_state.get("labels_dict", {})

# All numeric columns available for X/Y (exclude 'year' so it’s not selectable)
numeric_cols = [
    col for col in df_panel.select_dtypes(include="number").columns
    if col != "year"
]

if not numeric_cols:
    st.error("No numeric variables available for plotting.")
    st.stop()

# Helper: get display label for any column
def get_label(col: str) -> str:
    # labels_all comes from VariableInfo sheet (via Main.py)
    return labels_all.get(col, col)

# Helper: map a chosen label back to the column name
def get_code_from_label(label: str) -> str:
    # search only among numeric_cols (the ones in the dropdown)
    for col in numeric_cols:
        if get_label(col) == label:
            return col
    # fallback: if user somehow selected a raw column name
    if label in df_panel.columns:
        return label
    raise KeyError(f"Label '{label}' not found among numeric columns.")


# ---- Sidebar ----
st.sidebar.header("Please Filter Here:")

country = st.sidebar.multiselect(
    "Select the Country:",
    options=sorted(df_panel["country"].unique()),
    default=['Pakistan', 'India', 'Bangladesh']
)

variable_label = st.sidebar.selectbox(
    "Select Y-axis variable:",
    options=[get_label(v) for v in numeric_cols],
    index=0
)

start_year, end_year = st.sidebar.select_slider(
    "Select Year Range:",
    options=sorted(df_panel["year"].unique()),
    value=(df_panel["year"].min(), df_panel["year"].max())
)

# Convert label → actual column name
variable = get_code_from_label(variable_label)
label_var = get_label(variable)

# --- Filtered dataframe ---
df_selection = df_panel.query(
    "country in @country & year >= @start_year & year <= @end_year"
)

if df_selection.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# ---- Axis scale ----
yscale = st.sidebar.radio(
    "Y-axis scale:",
    options=["Linear", "Log"],
    index=0
)

# VISUALISATION: Line Plot
fig = px.line(
    df_selection.dropna(subset=[variable]),
    x="year",
    y=variable,
    color="country"
)

fig.update_layout(
    template="plotly_white",
    title={
        'text': f"{label_var} over time",
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=28)
    },
    xaxis_title=" ",
    yaxis_title=label_var,
    legend=dict(title='', orientation='v', x=0.02, y=1)
)

fig.update_layout(
    yaxis_type="log" if yscale == "Log" else "linear"
)

fig.add_annotation(
    text="SOURCE: Penn World Table, Version 11",
    xref="paper", yref="paper",
    x=0, y=-0.2,
    showarrow=False,
    font=dict(size=12)
)

st.plotly_chart(fig, use_container_width=True)
