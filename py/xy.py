import pandas as pd

# Load the dataset from CSV
df = pd.read_csv("sales.csv")

# Display original data
print("Original Data:")
print(df)

# -------------------------
# Slice: Filter sales for the year 2024
slice_2024 = df[df['Time'] == 2024]
print("\nSlice (Time = 2024):")
print(slice_2024)

# -------------------------
# Dice: Filter for products TV and Laptop in North region
dice_data = df[(df['Product'].isin(['TV', 'Laptop'])) & (df['Region'] == 'North')]
print("\nDice (Product = TV or Laptop, Region = North):")
print(dice_data)

# -------------------------
# Drilldown: Group by Year and then by Product
drilldown = df.groupby(['Time', 'Product'])['Sales'].sum().reset_index()
print("\nDrilldown (Time -> Product):")
print(drilldown)

# -------------------------
# Rollup: Aggregate sales by Region
rollup_region = df.groupby('Region')['Sales'].sum().reset_index()
print("\nRollup (Total Sales by Region):")
print(rollup_region)

# Aggregate sales by Product
rollup_product = df.groupby('Product')['Sales'].sum().reset_index()
print("\nRollup (Total Sales by Product):")
print(rollup_product)

# -------------------------
# Pivot Table: Products as rows, Time as columns, Sales as values
pivot_table = df.pivot_table(index='Product', columns='Time', values='Sales', aggfunc='sum')
print("\nPivot Table (Products vs Time):")
print(pivot_table)
