import pandas as pd
import matplotlib.pyplot as plt

# Read the data
sales = pd.read_csv("ItemDetails.csv", parse_dates=['date'])
sales.head()
print(sales)

# Describe the data
sales.describe()

# Filter the data
customers = sales[['name', 'net_price', 'date']]
customers.head()

# Group the customers by name and sum their sales
customer_group = customers.groupby('net_price')
sales_totals = customer_group.sum()

# Plot the graph after calculating total sales by each customer. Customer name should be
# on x-axis and total sales in y-axis

customers = sales[['name', 'category', 'net_price', 'date']]
category_group = customers.groupby(['name', 'category']).sum()
# Plot and show the stacked bar chart
stack_bar_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer",figsize=(9, 7))
stack_bar_plot.set_xlabel("Customers")
stack_bar_plot.set_ylabel("Sales")
stack_bar_plot.legend(["Total","Belts","Shirts","Shoes"], loc=9,ncol=4)
plt.show()