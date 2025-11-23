import streamlit as st


# ---- PAGE TITLE ----
st.markdown("""
## About This Project

This page offers a simple, interactive way to explore the Penn World Table (PWT) dataset through visualisation. Users can also create their own custom variables based on existing ones in the dataset, allowing for better analysis. The aim is to help students, researchers, and anyone curious about international development compare macroeconomic indicators across countries and over time. 
                     
The tool allows users to generate three types of visualisations:

- **Line plots**, useful for tracking how a variable evolves over time  
- **Scatter plots**, which show relationships between two indicators  
- **Connected scatter plots**, which trace how two variables move together over time  

These visual tools make it easier to spot patterns such as growth trends, productivity shifts, and long-run changes in living standards. The interface is designed to be straightforward and flexible, enabling users to filter countries, choose variables, adjust time ranges, and switch between linear or log scales.

Overall, this page provides a practical starting point for exploring the PWT dataset without needing to write code—supporting both classroom learning and independent curiosity about macroeconomic data.

---
            
The Penn World Table version 11 is originally hosted by the University of Groningen and can be found [here](https://www.rug.nl/ggdc/productivity/pwt/). For more information on the dataset, please refer to the following paper:
            
- Feenstra, Robert C., Robert Inklaar and Marcel P. Timmer (2015), "The Next Generation of the Penn World Table" American Economic Review, 105(10), 3150-3182, available for download at www.ggdc.net/pwt

""")
