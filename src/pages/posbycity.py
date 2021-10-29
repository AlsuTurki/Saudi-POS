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
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    title = """
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic&display=swap" rel="stylesheet" type="text/css"/>
    <style> bdi {font-family: 'IBM Plex Sans Arabic';}
    div { direction: RTL;}
    .css-hi6a2p {padding-top: 0rem;}
    </style>
    <div><h2><bdi>نقاط البيع لكل مدينة</bdi></h2></div>
    """
    st.write(title , unsafe_allow_html=True, )

    cities_df = pd.read_csv('./output/full_cities_df.csv', encoding="utf8")

    ## Range selector
    try:
        start_date, end_date = st.date_input('اختر الفترة :', [])
        if start_date < end_date:
            pass
        else:
            st.error('للاسف لا يوجد بيانات كافية لهذه الفترة.')
        ## Sanity check
        cities_df['Start Date']= pd.to_datetime(cities_df['Start Date']).dt.date
        #greater than the start date and smaller than the end date
        mask = (cities_df['Start Date'] > start_date) & (cities_df['Start Date'] <= end_date)
        cities_df = cities_df.loc[mask]

    except:
        pass
    #map 
    px.set_mapbox_access_token('pk.eyJ1IjoiYWxzdXR1cmtpIiwiYSI6ImNrdjUzOXM4cTAzZmIydnBqMWh1cms0a2MifQ.HDRkBwCGJl3wMaWzsyMtDQ')
    fig = px.scatter_mapbox(cities_df, lat="location_latitude", lon="location_longitude",
                        hover_name='Arabic_City',
                        color="Value of Transactions", 
                        size="Value of Transactions", zoom=4,
                  color_continuous_scale= px.colors.sequential.Blugrn, size_max=30)
    st.plotly_chart(fig)
 
  




    # Number of Transactions by city 
    cities_df = cities_df.sort_values('Number of Transactions')

    aggs = ["count","sum","avg","median","mode","rms","stddev"]

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
    pio.write_html(fig_dict, file = './html_files/numoftrans_cities_df_bar.html', validate=False)
    HtmlFile = open(f'./html_files/numoftrans_cities_df_bar.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, scrolling=True)


    # Value of Transactions by city 
    cities_df = cities_df.sort_values('Value of Transactions')

    aggs = ["count","sum","avg","median","mode","rms","stddev"]

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
    pio.write_html(fig_dict, file = './html_files/cities_df_bar.html', validate=False)
    HtmlFile = open('./html_files/cities_df_bar.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, scrolling=True)


    #convert_df to csv
    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')


    csv = convert_df(cities_df)

        #Show & downloade raw data 
    if st.checkbox('البيانات الخام لكل قطاع'):
        st.subheader('البيانات الخام')
        st.write(cities_df)
        st.download_button(
        label=" حمل البيانات كـCSV",
        data=csv,
        file_name='pos-sectors-data.csv',
        mime='text/csv',)


