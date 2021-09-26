import pandas as pd
import matplotlib.pyplot as plt

# read data
all_data = pd.read_csv('all_data.csv')

# Question 5 : What product sold the most? Why do you think it sold the most?

# Solution 1 ***************
product_gr = all_data.groupby('Product')

product_amount = product_gr.sum()['Quantity Ordered'].sort_values(ascending=False)

product_sold_most = list(product_gr.sum()['Quantity Ordered'].sort_values(ascending=False).index)

product_name = product_amount.index[:10]
product_sold_amount = product_amount.values[:10]

plt.bar(product_name, product_sold_amount)
plt.xlabel('Product Name')
plt.xticks(rotation=30)
plt.ylabel('Amount Sold')
plt.legend()
plt.title('Most Sold Product')
plt.tight_layout()
plt.show()


# Solution 2 ***************
product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered'].sort_values(ascending=False)

products = [product for product, df in product_group]

x_value = quantity_ordered.index
y_value = quantity_ordered.values
# plt.bar(x_value[:10], y_value[:10])  # 상위 10개
plt.bar(x_value, y_value)
plt.xticks(products, rotation='vertical', size=8)
plt.xlabel('Product')
plt.ylabel('Quantity Ordered')
plt.tight_layout()
plt.show()

prices = all_data.groupby('Product').mean()['Price Each']
price_list = [prices[x] for x in x_value]

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
# ax1.bar(x_value[:10], y_value[:10], color='g') # 상위 10개
# ax2.plot(x_value[:10], price_list[:10], 'b-')
# ax1.set_xticklabels(x_value[:10], rotation='vertical', size=8)
ax1.bar(x_value, y_value, color='g')
ax2.plot(x_value, price_list, 'b-')
ax1.set_xticklabels(x_value, rotation='vertical', size=8)

ax1.set_xlabel('Product')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price Each ($)', color='b')

plt.tight_layout()
plt.show()
