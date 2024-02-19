import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("bonus_data.db")
cursor = connection.cursor()

cursor.execute("SELECT data FROM Temperatura")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperatura FROM Temperatura")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature,
                             labels={"x": "Dssate", "y": "Temperature (C)"})

st.plotly_chart(figure)