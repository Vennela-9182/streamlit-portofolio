# -*- coding: utf-8 -*-
"""portfolio

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_JQ5abgGUK1GPOfwcAxuhK6gpiFTo00-
"""

import streamlit as st
st.title("My Data Science Portfolio")
st.sidebar.title("Navigation")
options=st.sidebar.selectbox("Select a option",['Home','About me','Projects','Contact'])
if options=='Home':
  st.header("Welcome to my portfolio")
  st.markdown("hello i am datascientist passionate in this protofolio u will see some my datadriven projects feel free to explore")
elif options=='About me':
  st.header("About me")
  st.markdown("""i have strong background in  **Data analysis**,**statistics**.
              I love to solve real world problems skills i have
              - Python, Pandas 
              - SQL Databases
              - Data Visulization(matplotlib,seaborn,plotly)
              - Web Development(Streamlit)
""")
elif options=='Projects':
  st.header("Projects")
  st.subheader("1.EDA on movies dataset")
  st.image("project1.png",Caption="Rating analysis of all movie rating websites")
  st.markdown("""This project will give insights to perform this project i have used Pandas, matplotlib, seaborn, plotly a data visualisation
              - [github link](https://github.com/Vennela-9182/EDA-on-Movies)
  """)
  st.subheader("2.Auto-plot EDA app")
  st.image("Project2.png",Caption="Auto-plot EDA app")
  st.markdown("""This is mainly usefull for non technial people which performs automatic eda
              - [github link](https://github.com/Vennela-9182/Auto_EDA_plots)
  """)
elif options=='Contact':
  st.header("Contact")
  st.markdown(""" - [Linkdin](https://www.linkedin.com/in/siri-vennela-kambalapally-856449323?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
                  - [github](https://github.com/Vennela-9182?tab=repositories)""")