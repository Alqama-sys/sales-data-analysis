import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("sales_data.csv")

print("Dataset Preview:")
print(data.head())

# Create total sales column
data["Total_Sales"] = data["Quantity"] * data["Price"]

# ----------------------------
# Sales by Category
# ----------------------------
category_sales = data.groupby("Category")["Total_Sales"].sum()
print("\nTotal Sales by Category:")
print(category_sales)

# Plot category sales
category_sales.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Total Sales by Category")
plt.show()

# ----------------------------
# Sales by Region (NEW)
# ----------------------------
region_sales = data.groupby("Region")["Total_Sales"].sum()
print("\nTotal Sales by Region:")
print(region_sales)

# Plot region sales
region_sales.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Total Sales by Region")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("sales_data.csv")

# Show first rows
print("Dataset Preview:")
print(data.head())

# Create total sales column
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Total sales by category
category_sales = data.groupby("Category")["Total_Sales"].sum()
print("\nSales by Category:")
print(category_sales)

# Plot sales by category
category_sales.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Total Sales by Category")
plt.show()


