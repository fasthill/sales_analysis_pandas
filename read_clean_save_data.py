import pandas as pd
import os

# merging 12 months sales data into a single file
all_month_data = pd.DataFrame()
files = [pd.read_csv('./Sales_Data/'+file) for file in os.listdir('./Sales_Data')]
for file in files:
    all_month_data = pd.concat([all_month_data, file], ignore_index=True)

# add month columns, clear rows with nan and non-data type elements
all_month_data = all_month_data.dropna(how='all')  # nan 제거
all_month_data = all_month_data[all_month_data['Order Date'] != 'Order Date']  # delete non-data rows

all_month_data['Month'] = all_month_data['Order Date'].str[0:2]
all_month_data['Month'] = all_month_data['Month'].astype('int32')

all_month_data['Order Date (datetime)'] = pd.to_datetime(all_month_data['Order Date'], format='%m/%d/%y %H:%M')

all_month_data.to_csv('all_data.csv', index=False)
