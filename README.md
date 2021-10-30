# Weekly Point Of Sales Transactions Dashboard

```
Author: Turki A. Alsughayyir
```

### About the project 
This project aime to collect and visualize the weekly saudi Arabia Points of Sale Transactions report. Since 2016 each week Sama is publishing a weekly POS transaction report as pdf file containing two tables
  - Table one: Number/Value of transaction by a sector.
  - Table Two: Number/Value of transaction by city.


you can find the reports <a href="[url](https://www.sama.gov.sa/en-US/Indices/Pages/POS.aspx)">Here</a> 
Unfornchaly we only found a part of 2020 weekly reports and 2021 reports strat from 12/06/2020 until current date, please feel free to edit and fix any issue in the crawler script inside the following notebook **./SaudiPointOfsalesTransaction.ipynb**  note, we have to respect the policy and agrement and not cousing any issue or distrbing while recosditing the SAMA site by passing sleep time and keep them at minimal. 

as alternative solution I did found a monthly historcal data from 2016 to 2021 in <a href="[url](https://www.sama.gov.sa/en-US/Indices/Pages/POS.aspx)">SA open data</a> as excel file, whch nedd a lot of manual prsessing, you can find it in the **output/historcal-points-of-sale-transactions.xlsx**



### Technologies used
- Python 3
  - web scraping (**beautiful soup**)
  - Automates browsers (**Selenium**)
  - PDF Parsing (**pdfplumber**)
  - Data processing and manipulation (**Pandas**)
  - Data Visualization (**Plotly**)
  - web apps framework (**Streamlit**)  

### Data

You can find all raw data in **output** folder, and below the breack down:
  - **output/full_cities_df.csv**
    - English_City: the name of the city in english, **str type**
    - Arabic_City: the name of the city in english, **str type**
    - Start Date: the strat date of the report, **date type**
    - End Date: the end date of the report, **date type**
    - Week Number: the week number of the year, **int type**
    - Number of Transactions: A weekly number of transaction by city, **int type**
    - Value of Transactions: A weekly value of transaction by city, **int type**  
    - location_latitude: for map ploting, in geography, latitude is a geographic coordinate that specifies the north–south position of a point on the Earth's surface, **int type**
    - location_longitude: For map ploting, Longitude is a geographic coordinate that specifies the east–west position of a point on the Earth's surface, or the surface of a celestial body, **int type**
  
  - **output/sectors_df.csv**
    - English_Sector: the name of the sector in english, **str type**
    - Arabic_Sector: the name of the sector in arabic, **str type**
    - Start Date: the strat date of the report, **date type** 
    - End Date: the end date of the report, **date type**
    - Week Number: the week number of the year, **int type**
    - Number of Transactions: A weekly number of transaction by sector, **int type**
    - Value of Transactions: A weekly value of transaction by sector, **int type** 
  
  - **output/historcal-points-of-sale-transactions.xlsx**
    - English_Sector: the name of the sector in english, **str type**
    - Arabic_Sector: the name of the sector in arabic, **str type**
    - Start Date: the strat date of the report, **date type** 
    - End Date: the end date of the report, **date type**
    - Week Number: the week number of the year, **int type**
    - Number of Transactions: A weekly number of transaction by sector, **int type**
    - Value of Transactions: A weekly value of transaction by sector, **int type** 
  
  - **output/historcal-points-of-sale-transactions.xlsx** Historical data
    - English_Sector: the name of the sector in english, **str type**
    - Arabic_Sector: the name of the sector in arabic, **str type**
    - Date: the strat date of the report, **date type** 
    - Number of Transactions: A monthly number of transaction by sector, **int type**
    - Value of Transactions: A monthly value of transaction by sector, **int type** 
  
  - **output/Grouped_City.csv & output/cities_df.csv** 
    - helper csv files for processing longitude & latitude (data pipline will be optimazed later on and the files we be no longer with us :( 

### project file structure


