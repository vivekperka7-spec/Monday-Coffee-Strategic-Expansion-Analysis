"""Interactive dashboard for the Monday Coffee expansion analysis."""

from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).parent


@st.cache_data
def load_data():
    city = pd.read_csv(ROOT / "city.csv")
    customers = pd.read_csv(ROOT / "customers.csv")
    products = pd.read_csv(ROOT / "products.csv")
    sales = pd.read_csv(ROOT / "sales.csv", parse_dates=["sale_date"])
    return city, customers, products, sales


def city_metrics(city, customers, sales):
    transactions = sales.merge(customers[["customer_id", "city_id"]], on="customer_id")
    summary = transactions.groupby("city_id").agg(
        total_revenue=("total", "sum"),
        active_customers=("customer_id", "nunique"),
        transactions=("sale_id", "count"),
    ).reset_index()
    metrics = city.merge(summary, on="city_id", how="left").fillna(0)
    metrics["estimated_coffee_consumers"] = metrics["population"] * 0.25
    metrics["avg_revenue_per_customer"] = (
        metrics["total_revenue"] / metrics["active_customers"].replace(0, pd.NA)
    ).fillna(0)
    metrics["rent_per_customer"] = (
        metrics["estimated_rent"] / metrics["active_customers"].replace(0, pd.NA)
    ).fillna(0)
    return metrics


st.set_page_config(page_title="Monday Coffee Expansion", page_icon="☕", layout="wide")

city, customers, products, sales = load_data()
metrics = city_metrics(city, customers, sales)

st.title("☕ Monday Coffee: Strategic Expansion Dashboard")
st.caption("Sales and market analysis for selecting the next physical store locations.")

min_date, max_date = sales["sale_date"].min().date(), sales["sale_date"].max().date()
date_range = st.sidebar.date_input("Sales period", value=(min_date, max_date), min_value=min_date, max_value=max_date)

if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    filtered_sales = sales[sales["sale_date"].between(start_date, end_date)]
else:
    filtered_sales = sales

filtered_metrics = city_metrics(city, customers, filtered_sales)
total_revenue = filtered_sales["total"].sum()
active_customers = filtered_sales["customer_id"].nunique()
average_order = filtered_sales["total"].mean()

first, second, third, fourth = st.columns(4)
first.metric("Total revenue", f"₹{total_revenue:,.0f}")
second.metric("Active customers", f"{active_customers:,}")
third.metric("Orders", f"{len(filtered_sales):,}")
fourth.metric("Average order value", f"₹{average_order:,.0f}" if pd.notna(average_order) else "—")

left, right = st.columns((1.35, 1))
with left:
    st.subheader("Revenue by city")
    revenue_chart = filtered_metrics.sort_values("total_revenue", ascending=False).set_index("city_name")["total_revenue"]
    st.bar_chart(revenue_chart)
with right:
    st.subheader("Recommended expansion cities")
    st.dataframe(
        filtered_metrics.sort_values(["total_revenue", "rent_per_customer"], ascending=[False, True])
        [["city_name", "total_revenue", "active_customers", "estimated_rent", "rent_per_customer"]]
        .head(3)
        .rename(columns={
            "city_name": "City", "total_revenue": "Revenue", "active_customers": "Customers",
            "estimated_rent": "Monthly rent", "rent_per_customer": "Rent / customer",
        }),
        hide_index=True,
        column_config={
            "Revenue": st.column_config.NumberColumn(format="₹%d"),
            "Monthly rent": st.column_config.NumberColumn(format="₹%d"),
            "Rent / customer": st.column_config.NumberColumn(format="₹%.2f"),
        },
        use_container_width=True,
    )

monthly_sales = filtered_sales.assign(month=filtered_sales["sale_date"].dt.to_period("M").astype(str)).groupby("month")["total"].sum()
st.subheader("Monthly sales trend")
st.line_chart(monthly_sales)

products_sold = (
    filtered_sales.merge(products[["product_id", "product_name"]], on="product_id")
    .groupby("product_name")["sale_id"].count().sort_values(ascending=False).head(10)
)
st.subheader("Top products by orders")
st.bar_chart(products_sold)

st.subheader("City market potential")
potential = filtered_metrics[[
    "city_name", "population", "estimated_coffee_consumers", "total_revenue",
    "active_customers", "avg_revenue_per_customer", "estimated_rent", "rent_per_customer",
]].sort_values("total_revenue", ascending=False)
st.dataframe(
    potential,
    hide_index=True,
    use_container_width=True,
    column_config={
        "city_name": "City", "population": st.column_config.NumberColumn("Population", format="%d"),
        "estimated_coffee_consumers": st.column_config.NumberColumn("Est. coffee consumers", format="%d"),
        "total_revenue": st.column_config.NumberColumn("Revenue", format="₹%d"),
        "active_customers": st.column_config.NumberColumn("Active customers", format="%d"),
        "avg_revenue_per_customer": st.column_config.NumberColumn("Revenue / customer", format="₹%.2f"),
        "estimated_rent": st.column_config.NumberColumn("Monthly rent", format="₹%d"),
        "rent_per_customer": st.column_config.NumberColumn("Rent / customer", format="₹%.2f"),
    },
)

st.info("Recommendation: prioritize Pune, Delhi, and Jaipur after validating neighbourhood-level demand, site availability, and operating costs.")
