# Weekly Point Of Sales Transactions Dashboard

```
Author: Turki A. Alsughayyir
```

- [Weekly Point Of Sales Transactions Dashboard](#weekly-point-of-sales-transactions-dashboard)
  - [About the project](#about-the-project)
  - [Technologies used](#technologies-used)
  - [Data](#data)
  - [project file structure](#project-file-structure)
  - [Contributing](#contributing)
  - [License](#license)
  - [About me & Contact information](#about-me--contact-information)
      - [My name is Turki Alsughayyir. Data guy.](#my-name-is-turki-alsughayyir-data-guy)


## About the project 
This project aime to use only pyhton to collect data , visualize it and build a web app around Saudi Arabia Points of Sale Transactions Report.


Since 2016 each week SAMA are publishing a weekly POS transaction report as pdf file containing two tables:
  - Table one: Number/Value of transaction by a sector.
  - Table Two: Number/Value of transaction by city.

  
you can find the reports <a href="[url](https://www.sama.gov.sa/en-US/Indices/Pages/POS.aspx)">Here</a> 
Unfornchaly I only found a part of 2020 weekly reports and 2021 reports strat from 12/06/2020 until current date, please feel free to edit and fix any issue in the crawler script inside the following notebook **./SaudiPointOfsalesTransaction.ipynb**  note, we have to respect the policy and agrement and not cousing any issue or distrbing while recosditing the SAMA site by passing sleep time and keep them at minimal. 

as alternative solution I did found a monthly data from 2016 to 2021 in <a href="[url](https://www.sama.gov.sa/en-US/Indices/Pages/POS.aspx)">SA open data</a> as excel file, whch needed a lot of manual prsessing, you can find it in the **output/historcal-points-of-sale-transactions.xlsx**



## Technologies used
- Python 3
  - web scraping (**beautiful soup**)
  - Automates browsers (**Selenium**)
  - PDF Parsing (**pdfplumber**)
  - Data processing and manipulation (**Pandas**)
  - Data Visualization (**Plotly**)
  - web apps framework (**Streamlit**)  

## Data

You can find all raw data in **output** folder, and below the breack down:
- Generated from SAMA site using the web crawler script
  - **output/full_cities_df.csv**
    - English_City: the name of the city in english, **str type**
    - Arabic_City: the name of the city in english, **str type**
    - Start Date: the strat date of the report, **date type**
    - End Date: the end date of the report, **date type**
    - Number of Transactions: A weekly number of transaction by city, **int type**
    - Value of Transactions: A weekly value of transaction by city, **int type**  
    - location_latitude: for map ploting, in geography, latitude is a geographic coordinate that specifies the north–south position of a point on the Earth's surface, **int type**
    - location_longitude: For map ploting, Longitude is a geographic coordinate that specifies the east–west position of a point on the Earth's surface, or the surface of a celestial body, **int type**
  
  - **output/sectors_df.csv**
    - English_Sector: the name of the sector in english, **str type**
    - Arabic_Sector: the name of the sector in arabic, **str type**
    - Start Date: the strat date of the report, **date type** 
    - End Date: the end date of the report, **date type**
    - Number of Transactions: A weekly number of transaction by sector, **int type**
    - Value of Transactions: A weekly value of transaction by sector, **int type** 
  
- manualy collected from Open Date site
  - **output/historcal-points-of-sale-transactions.xlsx**
    - English_Sector: the name of the sector in english, **str type**
    - Arabic_Sector: the name of the sector in arabic, **str type**
    - Start Date: the strat date of the report, **date type** 
    - End Date: the end date of the report, **date type**
    - Number of Transactions: A weekly number of transaction by sector, **int type**
    - Value of Transactions: A weekly value of transaction by sector, **int type** 
  
  - **output/linechart_hist_bysector.csv** 
    - TODO 
  
## project file structure

TODO

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

TODO


## About me & Contact information

#### My name is Turki Alsughayyir. Data guy.
I'm a multi-disciplined data analyst based out of Riyadh, Saudi Arabia. My experience ranges from Big Data Quality Analyst, Data Analyst, Data Engineering, Business intelligence and and Web Development sometime.

As a data guy I believe in setting ego aside and creating an data prodects that caters to the user's needs. I have a passion for an automating process, designing, and solving complex problems.


Please address personal correspondence to: ``` alsuturki20@gmail.com ```

Unfortunately, I am at times a lousy correspondent — where by “at times” I mean “most of the time”. If I don’t respond to your email, or do so only after an inordinate amount of time has passed you can find me in the water dodging surfers in the crowded pacific ocean trying to catch a couple of waves or on twitter [@AlsuTurki](https://twitter.com/AlsuTurki).

