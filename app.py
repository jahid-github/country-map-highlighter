import streamlit as st
import plotly.express as px

st.title("Country Map Highlighter")

country = st.text_input("Enter the country name:")

if country:
    data = {
        'Country': [country],
        'Values': [100]
    }
    fig = px.choropleth(
        data,
        locations='Country',
        locationmode='country names',
        color='Values',
        color_continuous_scale='Inferno',
        title=f'Country Map Highlighting {country}'
    )
    st.plotly_chart(fig)
