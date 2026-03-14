# Data-Engineering-Project
Using Python scrape the data from classiccars.com , create a data pipeline in Azure data factory to load it into data warehouse and visualize the data.

*******Project Title********
# Classic Car Market Data Pipeline and Price Prediction
* Overview *

# This project builds an end-to-end data pipeline to collect, process, and analyze classic car market listings.

# The goal of the project is to:

- collect real market listing data

- build a structured dataset

- create a data pipeline using Azure

- develop a machine learning model to estimate vehicle values

# Data Source

Vehicle listings were scraped from:

classiccars.com

# The dataset includes:

-Year

-Make

-Model

-Transmission

-Odometer

-Price

-Location

-Condition

# Project Architecture
Web Scraping (Python + BeautifulSoup)
        ↓
Raw Dataset (CSV)
        ↓
Feature Engineering
        ↓
Azure Data Factory Pipeline
        ↓
Azure SQL Database
        ↓
Machine Learning Price Prediction Model


# Technologies Used

-Python

-Pandas

-BeautifulSoup

-Azure Data Factory

-Azure SQL

-Docker

-Machine Learning

# Feature Engineering

-Vehicle condition was standardized using odometer ranges:

-Mileage	Condition
< 10,000	Concourse
< 50,000	Excellent
< 100,000	Good
100,000+	Fair

# Future Improvements

-Power BI dashboard for market trends

-Improved ML model using gradient boosting

-geographic price analysis

-automated pipeline orchestration
