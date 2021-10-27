"""This page is for searching and viewing the point of sales by sector """

import streamlit as st

import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import datetime as dt

def app():
    """Writes content to the app"""
    st.sidebar.title("نقاط البيع لكل قطاع")

    sectors_df = pd.read_csv('./output/sectors_df.csv', encoding="utf8")

    # resample weekly data to monthly 
    try:
        start_date, end_date = st.date_input('اختر الفترة :', [])
        if start_date < end_date:
            pass
        else:
            st.error('للاسف لا يوجد بيانات كافية لهذه الفترة.')
        ## Sanity check
        sectors_df['Start Date']= pd.to_datetime(sectors_df['Start Date']).dt.date
        #greater than the start date and smaller than the end date
        mask = (sectors_df['Start Date'] > start_date) & (sectors_df['Start Date'] <= end_date)
        sectors_df = sectors_df.loc[mask]
    except:
        pass

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






