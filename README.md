# ☕ Monday Coffee — Strategic Expansion Analysis

[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://monday-coffee-strategic-expansion-analysis.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/Analysis-SQL-4479A1?logo=postgresql&logoColor=white)](Solutions.sql)

An end-to-end data analytics project that helps **Monday Coffee** decide where to open its next physical stores in India. It combines online sales performance, customer activity, city population, and estimated rent to identify locations with strong demand and practical operating costs.

## 🔗 Live Demo

Explore the interactive dashboard here: **[Monday Coffee Expansion Dashboard](https://monday-coffee-strategic-expansion-analysis.streamlit.app/)**

## Business Problem

Monday Coffee sells online and wants to expand into physical retail. The question is not simply *which city has the highest revenue?* A promising city should also have a strong customer base, a large potential market, and rent that can be supported by demand.

This analysis answers: **Which cities should be prioritized for the next store openings?**

## What the Dashboard Demonstrates

- **Business scale:** total revenue, active customers, order volume, and average order value.
- **Demand by city:** a revenue comparison across cities to reveal where online traction is strongest.
- **Expansion economics:** customers, estimated monthly rent, revenue per customer, and rent per customer in one view.
- **Sales momentum:** monthly sales trends to understand how demand changes over time.
- **Product demand:** the coffee products customers order most often.
- **Market potential:** population-based estimates of potential coffee consumers alongside existing sales data.

## Key Insights

The final store decision should be validated with neighbourhood-level research, but the analysis highlights three strong candidates:

| City | Why it stands out |
| --- | --- |
| **Pune** | Highest revenue with a low rent-per-customer figure, making it the strongest overall commercial opportunity. |
| **Delhi** | A very large estimated coffee-consuming population and a strong existing customer base. |
| **Jaipur** | Strong customer engagement with favourable operating costs, making it a lower-risk expansion option. |

## Data Model

The project uses four related datasets:

| Dataset | Description |
| --- | --- |
| `city.csv` | City population, estimated rent, and ranking. |
| `customers.csv` | Customer profiles and their home cities. |
| `products.csv` | Coffee product catalogue and prices. |
| `sales.csv` | Order-level transaction data, ratings, and dates. |

## Analysis Questions

The SQL analysis covers the following business questions:

1. How many potential coffee consumers does each city have (assuming 25% of its population drinks coffee)?
2. What was the total revenue in Q4 2023?
3. Which products have the highest order volumes?
4. What is the average customer spend in each city?
5. How do population, potential consumers, and active customers compare by city?
6. What are the top three products in every city?
7. How many unique customers does each city have?
8. How does average sales per customer compare with rent per customer?
9. How is sales changing month to month?
10. Which cities have the strongest overall expansion potential?

## Tech Stack

- **SQL** — joins, CTEs, aggregates, subqueries, and window functions (`DENSE_RANK`, `LAG`).
- **Python + Pandas** — data loading and analytical validation.
- **Streamlit** — interactive dashboard and cloud deployment.

## Project Structure

```text
├── app.py              # Streamlit dashboard
├── run_project.py      # Pandas-based analysis script
├── Schemas.sql         # Database schema
├── Solutions.sql       # SQL business analysis
├── city.csv            # City data
├── customers.csv       # Customer data
├── products.csv        # Product data
├── sales.csv           # Transaction data
└── requirements.txt    # Dashboard dependencies
```

## Run the Dashboard Locally

```bash
git clone https://github.com/vivekperka7-spec/Monday-Coffee-Strategic-Expansion-Analysis.git
cd Monday-Coffee-Strategic-Expansion-Analysis
pip install -r requirements.txt
streamlit run app.py
```

## Run the SQL Analysis

1. Create the tables using `Schemas.sql`.
2. Import the CSV files in this order: `city`, `products`, `customers`, then `sales`.
3. Run `Solutions.sql` to generate the analysis reports.

## Author

**Vivek Perka**

Turning data into confident expansion decisions, one city at a time.
