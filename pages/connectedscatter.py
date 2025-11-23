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

# Choose X / Y from all numeric variables
# Try to default to something sensible if present
if "pop" in numeric_cols:
    default_x_index = numeric_cols.index("pop")
else:
    default_x_index = 0

if "emp" in numeric_cols:
    default_y_index = numeric_cols.index("emp")
elif len(numeric_cols) > 1:
    default_y_index = 1
else:
    default_y_index = 0

variablex_label = st.sidebar.selectbox(
    "Select X-axis variable:",
    options=[get_label(v) for v in numeric_cols],
    index=0
)


variabley_label = st.sidebar.selectbox(
    "Select Y-axis variable:",
    options=[get_label(v) for v in numeric_cols],
    index=1 if len(numeric_cols) > 1 else 0
)

start_year, end_year = st.sidebar.select_slider(
    "Select Year Range:",
    options=sorted(df_panel["year"].unique()),
    value=(df_panel["year"].min(), df_panel["year"].max())
)

# Convert labels → actual column names
variablex = get_code_from_label(variablex_label)
variabley = get_code_from_label(variabley_label)

label_x = get_label(variablex)
label_y = get_label(variabley)

# --- Filter data ---
df_selection = df_panel.query(
    "country in @country & year >= @start_year & year <= @end_year"
)

if df_selection.empty:
    st.warning("No data for the selected filters.")
    st.stop()

# ---- Axis scales ----
xscale = st.sidebar.radio(
    "X-axis scale:",
    options=["Linear", "Log"],
    index=0,
)

yscale = st.sidebar.radio(
    "Y-axis scale:",
    options=["Linear", "Log"],
    index=0,
)

# ---- CONNECTED SCATTER (time-annotated line) ----
fig = px.line(
    df_selection.dropna(subset=[variablex, variabley]),
    x=variablex,
    y=variabley,
    color="country",
    text="year"   # year labels on the path
)

fig.update_layout(
    template="plotly_white",
    margin=dict(t=140),     # extra top margin for title
    title={
        'text': f"{label_y} and {label_x}",
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        #'font': dict(size=28),
    },
    xaxis_title=label_x,
    yaxis_title=label_y,
    legend=dict(title='',
                bgcolor="rgba(0,0,0,0)",
                bordercolor="rgba(0,0,0,0)",
                orientation='h',   # horizontal
                x=0.5,             # centered horizontally
                xanchor='center',  # anchor to center
                y=1.15             # positioned just below the title
                ),
    xaxis_type="log" if xscale == "Log" else "linear",
    yaxis_type="log" if yscale == "Log" else "linear",
)

fig.update_traces(textposition="bottom right", textfont_size=6)

fig.add_annotation(
    text="SOURCE: Penn World Table, Version 11",
    xref="paper", yref="paper",
    x=0, y=-0.3,
    showarrow=False,
    #font=dict(size=12),
)

# Show the Plot
st.plotly_chart(fig) #, use_container_width=True)


# --- Download filtered data as CSV ---
df_export = df_selection[["country", "year", variablex, variabley]].dropna(
    subset=[variablex, variabley]
)

csv_data = df_export.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Plot Data (CSV)",
    data=csv_data,
    file_name="pwt_connectedscatter_data.csv",
    mime="text/csv",
)