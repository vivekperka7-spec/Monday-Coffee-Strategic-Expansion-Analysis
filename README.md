# Monday Coffee Strategic Expansion Analysis

**Author**: P Vivek

## Project Overview
This project focuses on analyzing the sales data of Monday Coffee, an online coffee retailer, to identify key opportunities for physical store expansion. By leveraging data analytics techniques, the study evaluates consumer demand, sales performance, and market potential across major Indian cities to recommend the optimal locations for new store openings.

The primary objective is to derive actionable insights that balance high sales potential with operational cost efficiency.

## Database Structure
The analysis is based on a relational database consisting of four primary tables:

1. **City**: Contains data on city population, estimated rent, and ranking.
2. **Customers**: Stores distinct customer profiles and their associated cities.
3. **Products**: Lists the coffee products available for sale along with their pricing.
4. **Sales**: The transactional record of all sales, linking customers, products, and sales dates.

## Key Business Questions Analyzed
The project addresses ten critical questions to guide the expansion strategy. Below are the key areas of focus:

1.  **Consumer Demographics**: Estimation of potential coffee consumers per city based on population data.
2.  **Revenue Performance**: Calculation of total revenue generated across all cities, specifically focusing on the last quarter of 2023.
3.  **Product Popularity**: Analysis of sales volume for each coffee product.
4.  **Customer Spend Behavior**: Determination of the average sales amount per customer in each city.
5.  **City Metrics**: Aggregation of population, rent, and estimated consumer data.
6.  **Top Selling Products**: Identification of the top-performing products within each specific city.
7.  **Customer Base Analysis**: measurement of unique customer counts per city.
8.  **Cost-Benefit Analysis**: Comparison of average revenue per customer against average rent per customer.
9.  **Sales Trajectory**: Calculation of monthly sales growth rates.
10. **Market Potential Index**: A comprehensive scoring to identify the top three cities based on a weighted analysis of sales, rent, and customer volume.

## Strategic Recommendations
Based on the comprehensive data analysis, the following cities are recommended for the immediate phase of store expansion:

*   **Pune**: Identified as a high-priority location due to its exceptional balance of high total revenue and low average rent per customer, suggesting strong profitability.
*   **Delhi**: Represents the largest total addressable market with the highest number of estimated coffee consumers and total active customers.
*   **Jaipur**: Recommended for its strong customer engagement and favorable operational costs (lowest average rent), providing a low-risk entry point.

## Technical Implementation
The project utilizes SQL for data extraction, joining, and aggregation. Key technical concepts applied include:
*   Complex Joins and Subqueries
*   Common Table Expressions (CTEs)
*   Window Functions (RANK, DENSE_RANK, LAG)
*   Data Aggregation (GROUP BY, SUM, COUNT, AVG)

## How to Run
1.  **Database Setup**: Execute the `Schemas.sql` script to create the database structure and tables.
2.  **Data Import**: Load the provided CSV files (`city.csv`, `customers.csv`, `products.csv`, `sales.csv`) into the respective tables.
3.  **Analysis**: Run the queries in `Solutions.sql` to generate the reports.
4.  **Python Alternative**: A Python script (`run_project.py`) is also included to replicate the SQL analysis using the Pandas library for quick verification.

## Interactive Dashboard

The project includes a Streamlit dashboard that makes the analysis easy to explore in a browser.

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy

Deploy `app.py` from this GitHub repository with [Streamlit Community Cloud](https://share.streamlit.io/). Select the `main` branch and use `app.py` as the entrypoint. The included `requirements.txt` installs the dashboard dependencies automatically.
