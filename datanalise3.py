import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corona_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')
corona_dataset_csv.drop(['Lat', 'Long'], axis=1, inplace=True)
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates
data6 = corona_dataset_aggregated.head()
corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])
world_happiness_report = pd.read_csv("worldwide_happiness_report.csv")
data5 = world_happiness_report.head()
columns_to_dropped = ['Overall rank', 'Score', 'Generosity', 'Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped, axis=1, inplace=True)

data = world_happiness_report.head()
world_happiness_report.set_index(['Country or region'], inplace=True)
data2 = world_happiness_report.join(corona_data).copy()
print(data2)
data3 = data2.corr()
print(data3)

x = data2['GDP per capita']
y = data2['max infection rate']
scatter_plot = plt.scatter(x, np.log(y))
sns.regplot(x, np.log(y))
plt.show()
x = data2['Social support']
y = data2['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
plt.show()

x = data2['Freedom to make life choices']
y = data2['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
plt.show()





