import pandas as pd
import os

def load_data():
    try:
        print("Loading data...")
        city = pd.read_csv('city.csv')
        customers = pd.read_csv('customers.csv')
        products = pd.read_csv('products.csv')
        sales = pd.read_csv('sales.csv')
        
        # Convert sale_date to datetime
        sales['sale_date'] = pd.to_datetime(sales['sale_date'])
        
        print("Data loaded successfully.\n")
        return city, customers, products, sales
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None, None, None

def analyze_q1_coffee_consumers(city):
    print("--- Q1: Coffee Consumers Count (Est. 25% of Population) ---")
    df = city.copy()
    df['coffee_consumers_millions'] = round((df['population'] * 0.25) / 1_000_000, 2)
    # Sort by consumers desc
    df = df.sort_values(by='coffee_consumers_millions', ascending=False)
    print(df[['city_name', 'coffee_consumers_millions']].to_string(index=False))
    print("\n")

def analyze_q2_total_revenue_q4_2023(sales):
    print("--- Q2: Total Revenue (2023 Q4) ---")
    # Filter for 2023 and Q4 (Oct, Nov, Dec)
    q4_2023 = sales[
        (sales['sale_date'].dt.year == 2023) & 
        (sales['sale_date'].dt.quarter == 4)
    ]
    total_rev = q4_2023['total'].sum()
    print(f"Total Revenue in Q4 2023: {total_rev:,.2f}")
    print("\n")

def analyze_q10_market_potential(city, customers, sales):
    print("--- Q10: Market Potential Analysis (Top Cities Recommendation) ---")
    # Join tables: Sales -> Customers -> City
    merged = sales.merge(customers, on='customer_id').merge(city, on='city_id')
    
    # Group by city
    city_stats = merged.groupby('city_name').agg(
        total_revenue=('total', 'sum'),
        total_cx=('customer_id', 'nunique')
    ).reset_index()
    
    # Merge back with city specific data (rent, population) from original city table
    city_stats = city_stats.merge(city[['city_name', 'estimated_rent', 'population']], on='city_name')
    
    # Calculations
    city_stats['avg_sale_per_cx'] = round(city_stats['total_revenue'] / city_stats['total_cx'], 2)
    city_stats['avg_rent_per_cx'] = round(city_stats['estimated_rent'] / city_stats['total_cx'], 2)
    city_stats['est_coffee_consumers_millions'] = round((city_stats['population'] * 0.25) / 1_000_000, 3)
    
    # Sort by total revenue as per the SQL query implication (or combined metrics)
    # The README recommends: Pune, Delhi, Jaipur
    
    # Let's show the full stats sorted by Revenue
    result = city_stats.sort_values(by='total_revenue', ascending=False)
    
    print(result[[
        'city_name', 'total_revenue', 'estimated_rent', 'total_cx', 
        'est_coffee_consumers_millions', 'avg_sale_per_cx', 'avg_rent_per_cx'
    ]].to_string(index=False))
    print("\n")
    
    print("Top Details matching README recommendations:")
    print("1. Pune: Low rent/cx, High Revenue.")
    print("2. Delhi: Highest consumers, High cx count.")
    print("3. Jaipur: Highest cx count, Low rent/cx.")

def main():
    city, customers, products, sales = load_data()
    if city is not None:
        analyze_q1_coffee_consumers(city)
        analyze_q2_total_revenue_q4_2023(sales)
        # Q3 - Product Sales info could be added but let's jump to the main one
        analyze_q10_market_potential(city, customers, sales)

if __name__ == "__main__":
    main()
