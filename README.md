# Penn World Table (PWT) Data Viewer

This project is an interactive **Streamlit** application designed to help users explore the **Penn World Table (PWT) Version 11** dataset. 

It enables students, researchers, and general users to visualise macroeconomic indicators across countries and over time—without writing any code. Users can also create their own custom variables based on existing ones in the dataset, allowing for better analysis.

The app provides an intuitive interface for generating:

- **Line plots** to track variables over time
- **Scatter plots** to examine relationships between two indicators
- **Connected scatter plots** to visualise how two variables evolve jointly
- **Custom computed variables** created directly within the app
- **Flexible filtering** by country, region, year, and axis scale (linear/log)

This tool is intended primarily for **education and exploratory data analysis**, giving users a friendly way to engage with international macroeconomic data.

---

## 📊 Key Features

- Multi-page Streamlit interface with structured navigation
- Automatic loading of variable **labels** from a dedicated sheet
- User-generated variables with add/remove functionality
- Clean Plotly visualisations with hover details
- Filters for countries, regions, years, and axis scales
- Integrated “About this Project” section inside the app

---

## 📁 Project Structure


```text
Main.py
pages/
    about.py
    lineplot_mod.py
    scatterplot_mod.py
    connectedscatter_mod.py
    customvariable.py
gdppaneldata.xlsx
```
