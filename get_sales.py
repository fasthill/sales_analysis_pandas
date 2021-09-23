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


# Question 2 : What city had the highest number of sales
# add city column
def get_city(address):
    return address.split(',')[1].strip()
# all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1].strip())


def get_state(address):
    return address.split(',')[2].split()[0]


# all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' ' + get_state(x))
all_data['City'] = all_data['Purchase Address'].apply(lambda x: f'{get_city(x)} ({get_state(x)})')

sales_city_gr = all_data.groupby('City')
sales_city = sales_city_gr.sum()['Sales']

city = sales_city_gr.sum().index

plt.plot(city, sales_city, 'r')
plt.bar(city, sales_city)

plt.title('Sales Plot')
plt.xticks(city, rotation='vertical', size=8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City')

plt.tight_layout()
plt.show()

max_city = sales_city_gr.sum()['Sales'].idxmax()
