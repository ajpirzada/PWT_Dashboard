import streamlit as st
import pandas as pd

# ---------- Load / share data ----------
if "df_panel" not in st.session_state:
    df = pd.read_excel(
        io="gdppaneldata.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
    )
    st.session_state["df_panel"] = df
    # store the original columns so we know what is "base" vs "custom"
    st.session_state["base_columns"] = df.columns.tolist()

df_panel = st.session_state["df_panel"]

if "base_columns" not in st.session_state:
    st.session_state["base_columns"] = df_panel.columns.tolist()

if "custom_vars" not in st.session_state:
    st.session_state["custom_vars"] = []  # names of user-created variables

base_columns = st.session_state["base_columns"]
custom_vars = st.session_state["custom_vars"]

# labels_dict loaded in Main.py from VariableInfo; fallback to empty if not present
labels_dict = st.session_state.get("labels_dict", {})

st.write("### Preview of data")
st.dataframe(df_panel.head())


# ---------- Show numeric columns with labels ----------
st.write("### Current numeric columns")

numeric_cols = df_panel.select_dtypes(include="number").columns.tolist()

rows = []
for col in numeric_cols:
    label = labels_dict.get(col, col)          # use label if available, else name
    is_custom = "Yes" if col in custom_vars else "No"
    rows.append({"Variable": col, "Label": label, "Custom?": is_custom})

st.dataframe(pd.DataFrame(rows), hide_index=True)


# ---------- Create custom variable ----------
st.write("### Create a custom variable")

# ---------- Examples of formulas ----------
with st.expander("Examples of formulas you can use"):
    st.markdown("""
    **Basic arithmetic**
    - gdp_pc = `rgdpo / pop`    (GDP per capita)
    - lab_prod = `rgdpo / emp`  (Labor productivity)
    - participation_rate = `(emp / pop) * 100`  (Participation rate in %)

    **Growth rates**
    - gdp_growth = `(rgdpna - rgdpna.shift(1)) / rgdpna.shift(1) * 100` (annual growth rate in %)

    **Moving averages**
    - rgdpo_ma3 = `rgdpo.rolling(3).mean()`   (3-year moving average)

    **Lags and leads**
    - rgdpo_lag = `rgdpo.shift(1)`   (lag 1 year)
    - rgdpo_lead = `pop.shift(-1)`    (lead 1 year)

    **Index numbers**
    - `rgdpo / rgdpo.iloc[0] * 100`

    These expressions follow pandas `.eval()` rules.
    """)


custom_name = st.text_input("New variable name (no spaces):", value="")
custom_expr = st.text_input("Formula:", value="")

if st.button("Add variable"):
    if not custom_name.strip():
        st.error("Please enter a variable name.")
    elif custom_name in df_panel.columns:
        st.error("A column with that name already exists.")
    elif not custom_expr.strip():
        st.error("Please enter a formula.")
    else:
        try:
            df_panel[custom_name] = df_panel.eval(custom_expr)
            st.session_state["df_panel"] = df_panel

            if custom_name not in st.session_state["custom_vars"]:
                st.session_state["custom_vars"].append(custom_name)

            st.success(f"Variable `{custom_name}` created.")
        except Exception as e:
            st.error(f"Could not create variable: {e}")


# ---------- Remove custom variables ----------
st.write("### Remove custom variables")

if not st.session_state["custom_vars"]:
    st.info("No custom variables have been created yet.")
else:
    to_remove = st.multiselect(
        "Select custom variables to remove:",
        options=st.session_state["custom_vars"],
    )

    if st.button("Remove selected variables"):
        removed = []
        for col in to_remove:
            if col in df_panel.columns:
                df_panel.drop(columns=[col], inplace=True)
                removed.append(col)

        # update shared df and custom_vars list
        st.session_state["df_panel"] = df_panel
        st.session_state["custom_vars"] = [
            c for c in st.session_state["custom_vars"] if c not in removed
        ]

        if removed:
            st.success(f"Removed: {', '.join(removed)}")
        else:
            st.warning("No variables were removed.")

st.write("Custom variables currently available:")
st.write(st.session_state["custom_vars"])
