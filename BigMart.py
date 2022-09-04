import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = pd.read_csv('BigMartSalesData.csv')
# Check the basic data
print(dataset.head())
print(dataset.info())

# Copy of dataset
data = dataset.copy()
# Get sales for the year 2011
data = data.drop(data[data.Year != 2011].index)

# Plotting the sales data for year 2011
total = data.groupby('Month').agg({'Amount': np.sum})
print(total)
data.groupby('Month').agg({'Amount': np.sum}).plot(kind='line', color='red')
plt.xlabel('Year of 2011')
plt.ylabel('Total Sales')
plt.title('Sales per month')
plt.show()

# # Plot Total Sales Per Month for Year 2011 as Bar Chart
data.groupby('Month').agg({'Amount': np.sum}).plot(kind='bar', color='orange')
plt.xlabel('Year of 2011')
plt.ylabel('Total Sales')
plt.title('Sales Per Month in 2011')
plt.show()

# Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
plt.figure(figsize=(5, 5))
sales_country = data.groupby('Country').agg({'Amount': np.sum})
plt.pie(sales_country.values, labels=sales_country.index, autopct='%1.1f%%')
plt.show()

# Plot Scatter Plot for the invoice amounts and see the concentration of amount.
# In which range most of the invoice amounts are concentrated

sales_invoice = dataset.groupby('InvoiceNo').agg({'Amount': np.sum})
print(sales_invoice)
plt.scatter(sales_invoice.values, sales_invoice.values, color='magenta')
plt.grid(True)
plt.show()
