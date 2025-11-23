import streamlit as st


# ---- PAGE TITLE ----
st.markdown("""
## About This Page

This page offers a simple, interactive way to explore the Penn World Table (PWT) dataset through visualisation. Users can also create their own custom variables based on existing ones in the dataset, allowing for better analysis. The aim is to help students, researchers, and anyone curious about international development compare macroeconomic indicators across countries and over time.
            
The tool allows users to generate three types of visualisations:

- **Line plots**, useful for tracking how a variable evolves over time  
- **Scatter plots**, which show relationships between two indicators  
- **Connected scatter plots**, which trace how two variables move together over time  

These visual tools make it easier to spot patterns such as growth trends, productivity shifts, and long-run changes in living standards. The interface is designed to be straightforward and flexible, enabling users to filter countries, choose variables, adjust time ranges, and switch between linear or log scales.

Overall, this page provides a practical starting point for exploring the PWT dataset without needing to write code—supporting both classroom learning and independent curiosity about macroeconomic data.

---

## Variables in this Dataset

The underlying data come from the Penn World Table (version 11). Each observation corresponds to a country–year, with additional information on regions and income groups coming from dataset on international capital flows compiled by Alfaro, Laura, Sebnem Kalemli-Ozcan and Vadym Volosovych (2014). The table below lists the names and labels of variables available on this page:

| Variable   | Description |
|-----------|-------------|
| `country` | Country name |
| `region`  | Large geographical region |
| `incgroup` | Income groups according to 2008 GNI per capita (World Bank Atlas method) |
| `year`    | Year |
| `rgdpo`   | Output-side real GDP at chained PPPs (million 2021 US dollars) |
| `rgdpna`  | Real GDP at constant 2021 national prices (million 2021 US dollars) |
| `rconna`  | Real consumption at constant 2021 national prices (million 2021 US dollars) |
| `rnna`    | Capital stock at constant 2021 national prices (million 2021 US dollars) |
| `rtfpna`  | Total factor productivity (TFP) at constant national prices (2021 = 1) |
| `ctfp`    | TFP level at current PPPs (USA = 1) |
| `pop`     | Population (in millions) |
| `emp`     | Number of persons engaged (in millions) |
| `avh`     | Average annual hours worked by persons engaged (The Conference Board) |
| `labsh`   | Share of labour compensation in GDP at current national prices |
| `hc`      | Human capital index (see PWT documentation) |
| `csh_c`   | Share of household consumption at current PPPs |
| `csh_i`   | Share of gross capital formation at current PPPs |
| `csh_x`   | Share of merchandise exports at current PPPs |
| `pl_gdpo` | Price level of CGDPo (PPP/XR), price level of US GDPo in 2021 = 1 |
| `pl_c`    | Price level of household consumption, price level of US GDPo in 2021 = 1 |
| `pl_i`    | Price level of capital formation, price level of US GDPo in 2021 = 1 |
| `pl_x`    | Price level of exports, price level of US GDPo in 2021 = 1 |
| `pl_n`    | Price level of the capital stock, price level of US in 2021 = 1 |
| `xr`      | Exchange rate, national currency per US dollar |

""")
