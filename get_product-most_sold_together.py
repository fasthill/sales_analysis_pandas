import pandas as pd

# read data
all_data = pd.read_csv('all_data.csv')

# Question ４ : What products are most often sold together?

df = all_data[all_data['Order ID'].duplicated(keep=False)]

# Solution 1
product_list = df.groupby('Order ID')['Product'].apply(list)

product_dup = {}
for p_l1 in product_list:
    for p_l in p_l1:
        num = 0
        for p_l2 in product_list:
            if p_l in p_l2:
                num = num + 1
    product_dup[p_l] = num

product_dup_most = list(pd.Series(product_dup).sort_values(ascending=False).index)

# Solution 2
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID', 'Grouped']].drop_duplicates()

# https://stackoverflow.com/questions/52195887/counting-unique-pairs-of-numbers-into-a-python-dictionary
from itertools import combinations
from collections import Counter

count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

for key, value in count.most_common(10):
    print(key, value)
