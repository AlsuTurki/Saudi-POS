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
    <div><h2><bdi>نقاط البيع الشهرية لكل قطاع</bdi></h2></div>
    """
    st.write(title , unsafe_allow_html=True, )

    @st.cache
    def load_data():
        df = pd.read_csv('./output/Monthly_pos_by_Sector.csv')
        return df

    historcal_sectors_df = load_data()

    # resample weekly data to monthly 
    try:
        start_date, end_date = st.date_input('اختر الفترة :', [])
        if start_date < end_date:
            pass
        else:
            st.error('للاسف لا يوجد بيانات كافية لهذه الفترة.')
        ## Sanity check
        historcal_sectors_df['Date']= pd.to_datetime(historcal_sectors_df['Date']).dt.date
        #greater than the Date and smaller than the end date
        mask = (historcal_sectors_df['Date'] > start_date) & (historcal_sectors_df['Date'] <= end_date)
        historcal_sectors_df = historcal_sectors_df.loc[mask]
    except:
        pass



    # Number of Transactions by city 
    historcal_sectors_df = historcal_sectors_df.sort_values('Number of Transactions')
    mask = (historcal_sectors_df['Arabic_Sector'] != 'الإجمالي')
    historcal_sectors_df = historcal_sectors_df.loc[mask]

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
    x = historcal_sectors_df['Arabic_Sector'],
    y = historcal_sectors_df['Number of Transactions'],
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
    title = 'عدد العمليات الشهرية لكل قطاع',
    xaxis = dict(title = 'القطاع'),
    yaxis = dict(title = 'عدد العمليات الشهرية'),
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
    components.html(HtmlFile.read(),height=600, width = 800, scrolling=True)

    # value of transaction by sector   
    historcal_sectors_df = historcal_sectors_df.sort_values('Value of Transactions')

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
    x = historcal_sectors_df['Arabic_Sector'],
    y = historcal_sectors_df['Value of Transactions'],
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
    title = 'قيمة العمليات الشهرية لكل قطاع',
    xaxis = dict(title = 'القطاع'),
    yaxis = dict(title = 'قيمة العمليات الشهرية'),
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
    pio.write_html(fig_dict, file = 'html_files/historcal_sectors_df_1.html', validate=False)
    HtmlFile = open(f'html_files/historcal_sectors_df_1.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, width = 800, scrolling=True)





    historcal_sectors_df_line = pd.read_csv('./output/linechart_hist_bysector.csv')
    #historcal_sectors_df_line['Date'] = pd.to_datetime(historcal_sectors_df_line["Date"].dt.strftime('%d %b %y'))

    # set up ONE trace
    fig = px.line(x=historcal_sectors_df_line['Date'], y=historcal_sectors_df_line['المنافع العامة'])

    updatemenu = []
    buttons = []

    # button with one option for each dataframe
    for col in historcal_sectors_df_line.columns:
        if col != "Date":
            buttons.append(dict(method='restyle',
                                label=col,
                                visible=True,
                                args=[{'y':[historcal_sectors_df_line[col]],
                                    'x':[historcal_sectors_df_line['Date']],
                                    'type':'scatter'}, [0]],
                                )
                        )

    # some adjustments to the updatemenus
    updatemenu = []
    your_menu = dict()
    updatemenu.append(your_menu)

    updatemenu[0]['buttons'] = buttons
    updatemenu[0]['direction'] = 'down'
    updatemenu[0]['showactive'] = True
    updatemenu[0]['yanchor'] = 'top'
    updatemenu[0]['x'] = 0.85
    updatemenu[0]['x'] = 1.15
    

    # add dropdown menus to the figure
    fig.update_layout(showlegend=False, updatemenus=updatemenu)
    fig.update_xaxes(title_text = 'التاريخ',  tickformat = '%Y-%m-%d', tickmode = 'auto')
    fig.update_yaxes(title_text = 'العدد')
    fig.update_layout(title_text='عدد العمليات للقطاع على كل شهر', title_x=0.5)
    pio.write_html(fig, file = 'html_files/historcal_sectors_df_2.html', validate=False)
    HtmlFile = open(f'html_files/historcal_sectors_df_2.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, width = 800, scrolling=False)

    # Line chart 


    fig = px.line(historcal_sectors_df_line,
    x = historcal_sectors_df_line['Date'],
    y=["أخرى","الاتصالات","الأثاث","الأجهزة الإلكترونية والكهربائية","الأطعمة والمشروبات","الترفية والثقافة","التعليم","الصحة","الفنادق","المجوهرات","المطاعم والمقاهي","الملابس والأحذية","المنافع العامة","المواصلات","سلع وخدمات متنوعة","مواد التشييد والبناء"],)
    fig.update_layout(title_text='عدد العمليات لكل قطاع على كل شهر', title_x=0.5)
    pio.write_html(fig, file = 'html_files/historcal_sectors_df_2.html', validate=False)
    HtmlFile = open(f'html_files/historcal_sectors_df_2.html','r',encoding='utf-8')
    components.html(HtmlFile.read(),height=600, width = 800, scrolling=False)

    ## Pie Chart

    historcal_sectors_df['Value of Transactions'] = historcal_sectors_df['Value of Transactions'].replace(',','', regex=True)
    historcal_sectors_df['Value of Transactions'] = historcal_sectors_df['Value of Transactions'].astype(float)
    fig = px.pie(historcal_sectors_df, values='Value of Transactions', names='Arabic_Sector')
    fig.update_layout(title_text='نسبة قيمة العمليات لكل قطاع', title_x=0.5)
    fig.update_xaxes(title_text = 'التاريخ', tickformat="%b\n%Y", ticklabelmode="period")
    fig.write_html(file = 'html_files/historcal_pie_df_3.html', validate=False)
    st.plotly_chart(fig)



    #convert_df to csv
    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(historcal_sectors_df)


    #Show & downloade historcal raw data 
    if st.checkbox('البيانات الشهرية الخام لكل قطاع'):
        st.subheader('البيانات الشهرية الخام')
        st.write(historcal_sectors_df)
        st.download_button(
        label=" حمل البيانات كـCSV",
        data=csv,
        file_name='hist-pos-sectors-data.csv',
        mime='text/csv',)






