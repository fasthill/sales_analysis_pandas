import pandas as pd
import matplotlib.pyplot as plt

# read data
all_data = pd.read_csv('all_data.csv')

# Question 3 : What time should we display advertisement to maximize likelihood of customer's buying product?

# convert to date to datetime format
all_data['Order Date Datetime'] = pd.to_datetime(all_data['Order Date'], format='%m/%d/%y %H:%M')
all_data['Hour'] = all_data['Order Date Datetime'].dt.hour
all_data['Minute'] = all_data['Order Date Datetime'].dt.minute

hours = [hour for hour, df in all_data.groupby('Hour')]

all_gr = all_data.groupby(['Hour'])
plt.plot(hours, all_gr.count())
plt.title('Order Count on Hours')
plt.grid()
plt.xticks(hours)
plt.ylabel('Order Count')
plt.xlabel('Hour')
plt.tight_layout()
plt.show()
hour_max = all_gr.count()['Order ID'].idxmax()  # get any column

hour_order = list(all_gr.count()['Order ID'].sort_values(ascending=False).index)

# We recommend around 7 pm (max order), 12 pm (2nd max)

