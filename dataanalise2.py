import pandas as pd
import matplotlib.pyplot as plt

corona_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')
corona_dataset_csv.drop(['Lat', 'Long'], axis=1, inplace=True)
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.loc['China'].diff().plot()
plt.show()