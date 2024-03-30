import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load the dataset
relative_data_path = Path('Lab2_Datasets') / 'Lab2d_power.csv'
data_driver_bin = str(relative_data_path.resolve())
data = pd.read_csv(data_driver_bin)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Check for missing values
print("\nChecking for missing values:")
print(data.isnull().sum())

# Perform basic statistical analysis
print("\nBasic statistical analysis:")
print(data.describe())

# Data Cleaning (if necessary)
# Example: Remove rows with missing values
data = data.dropna()

# Perform data visualization
# Example: Plotting histograms for numerical columns
plt.figure(figsize=(10, 6))
sns.histplot(data['Humidity'], bins=20, kde=True)  # Replace 'column_name' with the actual column name
plt.title('Histogram of Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Example: Plotting a boxplot for numerical column
plt.figure(figsize=(8, 5))
# Replace 'category_column' and 'numerical_column' with actual column names
sns.boxplot(x='Humidity', y='WindSpeed', data=data)
plt.title('Boxplot of Numerical Column Grouped by Category Column')
plt.xlabel('Category')
plt.ylabel('Numerical Column')
plt.show()

# Add more visualizations as needed

# Save cleaned dataset (if applicable)
# data.to_csv('cleaned_data.csv', index=False)
