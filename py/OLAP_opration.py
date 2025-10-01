import pandas as pd

data = pd.read_csv('sales.csv')

print("Orignal data:\n",data)

# Slice Opration
slice_data = data[data['Time'] == 2023]
print("\nSlice Opration:\n",slice_data)

# Dice Opration
dice_data = data[(data['Time'] == 2023) & (data['Product'].isin(['TV',"Laptop"]) )]
print("\nDice Opration:\n",dice_data)


# Roll Up
rollup = data.groupby("Product")["Sales"].sum()
print("\nRoll-up: Total Sales by Product")
print(rollup)

# Drill Down
drilldown = data.groupby(["Product", "Region"])["Sales"].sum()
print("\nDrill-down: Sales by Product and Region")
print(drilldown)

# Pivot
pivot = data.pivot_table(values="Sales", index="Product", columns="Region", aggfunc="sum")
print("\nPivot Table: Sales by Product and Region")
print(pivot)