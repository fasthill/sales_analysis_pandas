import pandas as pd
import os
from datetime import datetime
import numpy as np

# merging 12 months sales data into a single file

all_month_data = pd.DataFrame()
files = [pd.read_csv('./Sales_Data/'+file) for file in os.listdir('./Sales_Data')]
for file in files:
    all_month_data = pd.concat([all_month_data, file], ignore_index=True)
all_month_data.to_csv('all_data.csv', index=False)

# read data
all_data = pd.read_csv('all_data.csv')

# add month columns
all_data = all_data.dropna(how='all') # nan 제거
all_data = all_data[all_data['Order Date'] != 'Order Date']

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

# Question 1 : What was the best month for sales? How much was earned that month?
all_data['Order Date (datetime)'] = pd.to_datetime(all_data['Order Date'], format='%m/%d/%y %H:%M')

print("1")
# dd = datetime.strptime(all_month_data['Order Date'][0],'%m/%d/%y %H:%M')
# dd1 = pd.to_datetime(all_month_data['Order Date'], format='%m/%d/%y %H:%M')
# all_month_data['Order Date (datetime)'] = pd.to_datetime(all_month_data['Order Date'],'%m/%d/%y %H:%M')

