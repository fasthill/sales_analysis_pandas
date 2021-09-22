import pandas as pd
import matplotlib.pyplot as plt

# read data
all_data = pd.read_csv('all_data.csv')

# Question 1 : What was the best month for sales? How much was earned that month?

# add sales column
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

gr = all_data.groupby('Month')
results = gr.sum()['Sales']
months = gr.sum().index

plt.plot(gr.sum().index, results)

plt.bar(months, results)

plt.title('Sales Plot')
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()
