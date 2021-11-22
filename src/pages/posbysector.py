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
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)    
    title = """
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic&display=swap" rel="stylesheet" type="text/css"/>
    <style> bdi {font-family: 'IBM Plex Sans Arabic';}
    div { direction: LTR; text-align: center;
    .css-hi6a2p {padding-top: 0rem;}
    </style>
    <div><h2><bdi>نقاط البيع الاسبوعية لكل قطاع</bdi></h2></div>
    """
    st.write(title , unsafe_allow_html=True, )
    
    @st.cache
    def load_data():
        df = pd.read_csv('./output/sectors_df.csv', encoding="utf8")
        return df

    sectors_df = load_data()

    # resample weekly data to monthly 
    try:
        start_date, end_date = st.date_input('اختر الفترة :', [])
        if start_date < end_date:
            pass
        else:
            st.error('للاسف لا يوجد بيانات كافية لهذه الفترة.')
        ## Sanity check
        sectors_df['Date']= pd.to_datetime(sectors_df['Date']).dt.date
        #greater than the Date and smaller than the end date
        mask = (sectors_df['Date'] > start_date) & (sectors_df['Date'] <= end_date)
        sectors_df = sectors_df.loc[mask]
    except:
        pass


    # Number of Transactions by city 
    sectors_df = sectors_df.sort_values('Number of Transactions')
    mask = (sectors_df['Arabic_Sector'] != 'الإجمالي')
    sectors_df = sectors_df.loc[mask]
    
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
    x = sectors_df['Arabic_Sector'],
    y = sectors_df['Number of Transactions'],
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
    title = 'عدد العمليات لكل قطاع',
    xaxis = dict(title = 'القطاع'),
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
    components.html(HtmlFile.read(),height=600,width = 800, scrolling=True)


    # value of transaction by sector   
    sectors_df = sectors_df.sort_values('Value of Transactions')

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
    pio.write_html(fig_dict, file = 'html_files/sectors_df_bar_1.html', validate=False)
    HtmlFile = open(f'html_files/sectors_df_bar_1.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600,width = 800, scrolling=True)


    ## Pie Chart

    sectors_df['Value of Transactions'] = sectors_df['Value of Transactions'].replace(',','', regex=True)
    sectors_df['Value of Transactions'] = sectors_df['Value of Transactions'].astype(float)
    fig = px.pie(sectors_df, values='Value of Transactions', names='Arabic_Sector')
    fig.update_layout(title_text='نسبة قيمة العمليات لكل قطاع', title_x=0.5)
    fig.write_html(file = 'html_files/cities_df_pie.html', validate=False)
    HtmlFile = open(f'html_files/cities_df_pie.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, width = 800, scrolling=False)





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
        label=" حمل البيانات كـCSV",
        data=csv,
        file_name='pos-sectors-data.csv',
        mime='text/csv',)







