import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('iphone_price.csv')

# Display the first few rows of the dataset
print(data.head())

# Plot the data
plt.plot(data['version'], data['price'], marker='o')  # Adding markers for clarity
plt.title('iPhone Price by Version')
plt.xlabel('iPhone Version')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent label cut-off
plt.show()
