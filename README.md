# Real Estate Price Analysis using Python

## About the Project

This project analyzes real estate property data using Python to identify pricing patterns and compare properties based on locality, BHK configuration, property type, construction status, RERA approval, and area.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn

## Data Cleaning

- Removed duplicate records
- Cleaned column names
- Converted price, area, and rate-per-square-foot fields into numeric values
- Standardized categorical values
- Converted RERA approval information into Boolean values

## Analysis Performed

The project answers questions such as:

- Which property is the most expensive?
- Which locality has the highest average price?
- Which locality has the highest average price per square foot?
- How do ready-to-move properties compare with under-construction properties?
- Does RERA approval relate to property pricing?
- How does area affect property price?
- Which BHK configuration has the highest average rate per square foot?
- Which property type has the highest average rate per square foot?

## Visualizations

The project includes scatter plots for:

- Area vs Price
- Area vs Rate per Square Foot

## Project Structure

real-estate-price-analysis/
├── data.csv
├── real_estate_analysis.py
└── README.md
