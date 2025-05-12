# %%
# importing libararies
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

# loading data
out_come_by_major = pd.read_excel("College-labor-data.xlsx", sheet_name="outcomes by major")
wages= pd.read_excel("College-labor-data.xlsx", sheet_name="wages")
underemployed = pd.read_excel("College-labor-data.xlsx", sheet_name="underemployed")
unemployed = pd.read_excel("College-labor-data.xlsx", sheet_name="unemployed")


#creating the dashboard
st.set_page_config(
    page_title="New York Graduate Employment Data",
    page_icon=":bar_chart:",
    layout="wide"
)


with st.sidebar:
    selected = st.radio("Main Menu", ["Home", "Wages", "Underemployment", "Unemployment", "Outcomes by Major"])

if selected == "Home":
    st.title(selected)
    st.markdown("""
# 🎓 Explore Graduate Employment & Wage Trends by Major

Gain insight into how different college majors have influenced career outcomes across the decades. Visualize employment rates and wage trends based on real data.

---

## 📊 About this Application

This interactive dashboard explores the employment rates and average wages of college graduates by major, spanning multiple decades. It is designed to help students, educators, and policymakers understand how academic choices align with long-term career outcomes.

### 🔍 Key Features:
- Interactive visualizations by **major** and **year**
- **Wage comparisons** across time
- **Employment trends** by discipline
- Insights for **informed academic and career planning**

---

## 👥 About Our Team

We are a group of students from **Baruch College**, passionate about data storytelling and higher education analytics. 

**Team Members**:
- Iskandar Bagirov  
- Mansoora Rokitma  
- Raushanna Nazmodin  
- Aribell Acosta  
- David Riad  
- Alexander Voronin  
- Brandon Nordin  

Through this project, we aim to empower current and prospective students to make informed academic and career decisions by providing **data-driven insights** into employment and wage trends by major.
""")

elif selected == "Wages":
    st.title(selected)
    st.markdown("""
    ### 📄 Wage Overview (1990–2024)
    This chart visualizes **wage trends in New York** from 1990 to 2024, based on education levels. 
    It includes income percentiles (25th, median, and 75th) for individuals with a **bachelor’s degree** as well as 
    median wages for those with a **high school diploma**. Use the dropdown above to customize the data shown.
    """)
    view_option = st.radio("Select View Option", ("Table", "Graph"))
    if view_option =="Graph":
        wages = wages.set_index('Date')
        col_options = list(wages.columns)
        options = st.multiselect('Select the year(s) to display:', options=col_options, default=col_options)

        fig = px.line(wages, x=wages.index, y=options)
        fig.update_layout(
            title="Wages by Year",
            xaxis_title="Year",
            yaxis_title="Wage",
            legend_title="Degree"
        )
        st.plotly_chart(fig)
    else:
        st.write(wages)

elif selected == "Underemployment":
    st.title(selected)
    st.markdown("""
        ### 📊 Underemployment Overview (1990–2024)
        This visualizes **underemployment trends in New York** from 1990 to 2024, based on recent graduates and college graduates. 
        """)
    
    view_option = st.radio("Select View Option", ("Table", "Graph"))
    if view_option == "Table":
        st.markdown("""### 📊 Underemployment Overview (1990–2024)""")
        st.write(underemployed)
    else:
        underemployed = underemployed.set_index('Date')
        col_options = list(underemployed.columns)
        options = st.multiselect('Options:', options=col_options, default=col_options)

        fig = px.line(underemployed, x=underemployed.index, y=options)
        fig.update_layout(
            title="Underemployment by Year",
            xaxis_title="Year",
            yaxis_title="Underemployment Rate",
            legend_title="Degree"
        )
        st.plotly_chart(fig)

elif selected == "Unemployment":
    st.title(selected)
    st.markdown("""
        ### 📊 Unemployment Overview (1990–2024)""")
    view_option = st.radio("Select View Option", ("Table", "Graph"))
    if view_option == "Table":
        st.write(unemployed)
    else:
        unemployed = unemployed.set_index('Date')
        col_options = list(unemployed.columns)
        options = st.multiselect('Options:', options=col_options, default=col_options)

        fig = px.line(unemployed, x=unemployed.index, y=options)
        fig.update_layout(
            title="Unemployment by Year",
            xaxis_title="Year",
            yaxis_title="Unemployment Rate",
            legend_title="Degree"
        )
        st.plotly_chart(fig)
        
elif selected == "Outcomes by Major":
    st.title(selected)
    st.markdown("""
        ### 📊 Outcomes by Major Overview (1990–2024)
        This visualizes **outcomes by major trends in New York** from 1990 to 2024, based on recent graduates and college graduates. 
        """)
    view_option = st.radio("Select View Option", ("Table", "Graph"))
    if view_option == "Table":
        st.write(out_come_by_major)
    else:
        selected_major = st.multiselect("Select Major(s):", options=out_come_by_major["Major"], default=["Information Systems & Management", "Mathematics", "Biology"])
        filtered = out_come_by_major[out_come_by_major["Major"].isin(selected_major)]
        
        metrics = out_come_by_major.columns[1:]  # Exclude the "Major" column
        selected_metric = st.selectbox("Select Metric:", metrics)
        fig = px.bar(filtered, x="Major", y=selected_metric, color="Major")
        st.plotly_chart(fig)