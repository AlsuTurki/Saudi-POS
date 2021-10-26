"""This page is for searching and viewing the point of sales by sector """

import streamlit as st

import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import streamlit.components.v1 as components
import datetime as dt
import random

def app():
    """Writes content to the app"""
    st.sidebar.title("نقاط البيع لكل قطاع")

    sectors_df = pd.read_csv('/Users/turki/Desktop/SaudiPointOfSales-staging/output/sectors_df.csv', encoding="utf8")

    # resample weekly data to monthly 
    years_months_values = [(d['Start Date'].year, d['Start Date'].month) for d in sectors_df.index]
    year, month = years_months_values[0]
    date_value = st.empty()
    month_slider = st.empty()
    def render_slider(year, month):

        month_value = month_slider.slider(
            "",
            min_value=0,
            max_value=len(years_months_values),
            value=years_months_values.index((year, month)),
            format="",
        )
        year, month = years_months_values[month_value]
        d = date(year, month, 1)
        date_value.subheader(f"Month: {d:%Y}-{d:%m}")
        return year, month

    # Bar chart city 
    sectors_df = sectors_df.sort_values('Value of Transactions')

    aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

    agg = []
    agg_func = []
    for i in range(0, len(aggs)):
        agg = dict(
            args=['transforms[0].aggregations[0].func', aggs[i]],
            label=aggs[i],
            method='restyle'
        )
        agg_func.append(agg)


    data = [dict(
    type = 'bar',
    x = sectors_df['Arabic_Sector'],
    y = sectors_df['Value of Transactions'],
    mode = 'markers',
    marker = dict(color = 'rgb(68, 68, 68)'),
    transforms = [dict(
        type = 'aggregate',
        aggregations = [dict(
            target = 'y', func = 'sum', enabled = True)
        ]
    )]
    )]

    layout = dict(
    title = 'قيمة العمليات لكل قطاع',
    xaxis = dict(title = 'القطاع'),
    yaxis = dict(title = 'قيمة العمليات'),
    updatemenus = [dict(
            x = 0.85,
            y = 1.15,
            xref = 'paper',
            yref = 'paper',
            yanchor = 'top',
            active = 1,
            showactive = False,
            buttons = agg_func
    )]
    )

    fig_dict = dict(data=data, layout=layout)
    pio.write_html(fig_dict, file = 'html_files/sectors_df_bar.html', validate=False)
    HtmlFile = open(f'html_files/sectors_df_bar.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, scrolling=True)


    #convert_df to csv
    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(sectors_df)

    #Show & downloade raw data 
    if st.checkbox('البيانات الخام لكل قطاع'):
        st.subheader('البيانات الخام')
        st.write(sectors_df)
        st.download_button(
        label="CSV حمل البيانات كـ",
        data=csv,
        file_name='pos-sectors-data.csv',
        mime='text/csv',)






