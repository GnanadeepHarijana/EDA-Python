# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Loading the dataset from a CSV file
dataset = pd.read_csv('superstore.csv')

# Displaying the first 5 rows of the dataset
print(dataset.head(5))

# Displaying the last 5 rows of the dataset
print(dataset.tail(5))

# Checking for missing values in the dataset
print(dataset.isnull().sum())

# Filling missing values in the 'Country' column with 'United States'
dataset['Country'] = dataset['Country'].fillna('United States')

# Checking for missing values after filling 'Country'
print(dataset.isnull().sum())

# Filling missing 'Postal Code' for Burlington, Vermont with 5401
dataset.loc[(dataset['City'] == 'Burlington') & 
            (dataset['State'] == 'Vermont') & 
            (dataset['Postal Code'].isnull()), 'Postal Code'] = 5401

# Checking for missing values after fixing 'Postal Code'
print(dataset.isnull().sum())

# Displaying count of each order priority
print(dataset['Order Priority'].value_counts())

# Plotting count of order priorities
sns.countplot(x="Order Priority", data=dataset)
plt.title("Count of Order priority")
plt.show()

# Displaying count of each shipping mode
print(dataset['Ship Mode'].value_counts())

# Counting shipping mode occurrences
ship_counts = dataset['Ship Mode'].value_counts()

# Creating a pie chart for ship mode distribution
plt.pie(ship_counts, labels=ship_counts.index, autopct='1%.1f%%')
plt.title("Ship Mode Distribution")
plt.show()

# Plotting ship mode count by category
sns.countplot(x="Ship Mode", data=dataset, hue="Category")
plt.title("ShipMode According to Category")
plt.show()

# Plotting distribution of customer segments
sns.countplot(x="Segment", data=dataset)
plt.title("Customer Segment Distribution")
plt.show()

# Plotting distribution of product categories
sns.countplot(x="Category", data=dataset)
plt.title("Category  Distribution")
plt.show()

# Plotting sub-category distribution within Furniture category
sns.countplot(x="Category", data=dataset[dataset["Category"] == "Furniture"], hue="Sub-Category")
plt.title("Furniture Category Distribution")
plt.show()

# Plotting sub-category distribution within Office Supplies category
sns.countplot(x="Category", data=dataset[dataset["Category"] == "Office Supplies"], hue="Sub-Category")
plt.title("Office Supplies Category Distribution")
plt.show()

# Plotting sub-category distribution within Technology category
sns.countplot(x="Category", data=dataset[dataset["Category"] == "Technology"], hue="Sub-Category")
plt.title("Technology Category Distribution")
plt.show()

# Converting 'Order Date' to datetime format
dataset["Order Date"] = pd.to_datetime(dataset["Order Date"], format='%d-%m-%Y')

# Extracting year from 'Order Date' and creating a new column 'Order Year'
dataset["Order Year"] = dataset["Order Date"].dt.year

# Displaying dataset summary info
dataset.info()

# Counting number of orders per year
print(dataset["Order Year"].value_counts())

# Plotting order count per year
sns.countplot(x="Order Year", data=dataset)
plt.title("Order Year Distribution")
plt.show()

# Plotting total sales per category
sns.barplot(x="Category", y="Sales", data=dataset, estimator="sum")
plt.title("Sales According to Category")
plt.show()

# Plotting total sales per region
sns.barplot(x="Region", y="Sales", data=dataset, estimator="sum")
plt.title("Sales According to Region")
plt.show()
