*******Project Title********
# Classic Car Market Data Pipeline and Price Prediction # 

## System Architecture overview

This project builds an end-to-end data pipeline to collect, process, and analyze classic car market data from Classiccar.com website.

Web Scraping (Python + BeautifulSoup)
        ↓
Raw Dataset (CSV)
        ↓
Data cleaning (Feature engineering)
        ↓
Azure Data Factory Pipeline
        ↓
Azure SQL Database
        ↓
Machine Learning Price Prediction Model


# The goal of the project is to:

- collect real market listing data

- build a structured dataset

- create a data pipeline using Azure

- develop a machine learning model to estimate vehicle values

## Project workflow
1. Data Collection

Vehicle listings are scraped from classiccars.com using Python and BeautifulSoup.

Fields collected:

-Year

-Make

-Model

-Transmission

-Odometer

-Price

-Location

2.Feature Engineering

-Vehicle condition was standardized using odometer ranges:

-Mileage	Condition
< 10,000	Concourse
< 50,000	Excellent
< 100,000	Good
100,000+	Fair
 
 Data Collection Script

        The scraper is located in:

        scripts/classiccars_pipeline.py

        This script performs:
        
        a. Web scraping of classic car listings from classiccars.com
        b. Extraction of vehicle attributes such as year, make, model, price, mileage, and condition
        c. Dataset creation in CSV format
        d. Feature engineering to derive vehicle condition categories
   
3. Data Pipeline

The cleaned dataset is ingested into Azure Data Factory, which orchestrates the data pipeline.

Pipeline tasks:

Data ingestion

Transformation

Loading into Azure SQL Database

        # Azure Data Factory Pipeline

        The project uses Azure Data Factory to orchestrate the ETL pipeline.

        Pipeline tasks include:
        
        • Ingesting scraped CSV data  
        • Transforming vehicle data  
        • Loading processed data into Azure SQL Database  
        
        Pipeline definition is available here:
        
        azure_data_factory/pipelines/classic_car_pipeline.json

4. Data Storage

The processed data is stored in Azure SQL tables for querying and downstream analysis.

5. Machine Learning Model

The dataset is used to train a price prediction model that estimates classic car market value based on vehicle attributes.

## Skills Demonstrated

• Web scraping with Python  
• Data cleaning and feature engineering  
• Cloud ETL pipeline design  
• Azure Data Factory orchestration  
• SQL data storage  
• Machine learning modeling  
• End-to-end data pipeline development

# Technologies Used

-Python

-Pandas

-BeautifulSoup

-Azure Data Factory

-Azure SQL

-Docker

-Machine Learning

# Project Screenshot

# Business Problem

Classic car values fluctuate significantly based on condition, rarity, and market demand.

This project builds a data pipeline that collects real marketplace listings and uses machine learning to estimate vehicle market values.

# Future Improvements

-Power BI dashboard for market trends

-Improved ML model using gradient boosting

-geographic price analysis

-automated pipeline orchestration
