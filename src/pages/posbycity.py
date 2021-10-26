"""This page is for searching and viewing the point of sales by sector """

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import streamlit.components.v1 as components
import datetime

def app():
    """Writes content to the app"""
    st.write("نقاط البيع لكل مدينة")

    Grouped_City = pd.read_csv('/Users/turki/Desktop/SaudiPointOfSales-staging/output/Grouped_City.csv', encoding="utf8")
    #map 
    px.set_mapbox_access_token('pk.eyJ1IjoiYWxzdXR1cmtpIiwiYSI6ImNrdjUzOXM4cTAzZmIydnBqMWh1cms0a2MifQ.HDRkBwCGJl3wMaWzsyMtDQ')
    fig = px.scatter_mapbox(Grouped_City, lat="location_latitude", lon="location_longitude",
                        hover_name='English_City',
                        color="Value of Transactions", 
                        size="Value of Transactions", zoom=4,
                        #text = Grouped_City['text'],
                  color_continuous_scale= px.colors.sequential.Blugrn, size_max=30)
    st.plotly_chart(fig)
 

    cities_df = pd.read_csv('/Users/turki/Desktop/SaudiPointOfSales-staging/output/cities_df.csv', encoding="utf8")
    #convert_df to csv
    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

  




    # Number of Transactions by city 
    cities_df = cities_df.sort_values('Number of Transactions')

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
    x = cities_df['Arabic_City'],
    y = cities_df['Number of Transactions'],
    mode = 'markers',
    marker = dict(color = 'rgb(40, 66, 153)'),
    transforms = [dict(
        type = 'aggregate',
        aggregations = [dict(
            target = 'y', func = 'sum', enabled = True)
        ]
    )]
    )]

    layout = dict(
    title = 'عدد العمليات لكل مدينة',
    xaxis = dict(title = 'المدينة'),
    yaxis = dict(title = 'عدد العمليات'),
    hovermode="x",
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
    pio.write_html(fig_dict, file = '/Users/turki/Desktop/SaudiPointOfSales-staging/html_files/numoftrans_cities_df_bar.html', validate=False)
    HtmlFile = open(f'/Users/turki/Desktop/SaudiPointOfSales-staging/html_files/numoftrans_cities_df_bar.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, scrolling=True)


    # Value of Transactions by city 
    cities_df = cities_df.sort_values('Value of Transactions')

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
    x = cities_df['Arabic_City'],
    y = cities_df['Value of Transactions'],
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
    title = 'قيمة العمليات لكل مدينة',
    xaxis = dict(title = 'المدينة'),
    yaxis = dict(title = 'قيمة العمليات'),
    hovermode="x",
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
    pio.write_html(fig_dict, file = '/Users/turki/Desktop/SaudiPointOfSales-staging/html_files/cities_df_bar.html', validate=False)
    HtmlFile = open(f'/Users/turki/Desktop/SaudiPointOfSales-staging/html_files/cities_df_bar.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, scrolling=True)





    csv = convert_df(cities_df)

        #Show & downloade raw data 
    if st.checkbox('البيانات الخام لكل قطاع'):
        st.subheader('البيانات الخام')
        st.write(cities_df)
        st.download_button(
        label="CSV حمل البيانات كـ",
        data=csv,
        file_name='pos-sectors-data.csv',
        mime='text/csv',)

