import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# Show data
print(df.head())

# 1. Monthly Sales Trend
plt.figure()
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.show()

# 2. Monthly Profit Analysis
plt.figure()
plt.bar(df['Month'], df['Profit'], color='green')
plt.title('Monthly Profit Analysis')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('profit_analysis.png')
plt.show()

# Insights
print(f"Total Sales: {df['Sales'].sum()}")
print(f"Total Profit: {df['Profit'].sum()}")
print(f"Best Sales Month: {df.loc[df['Sales'].idxmax(), 'Month']}")