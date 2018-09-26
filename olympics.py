import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


summer = pd.read_csv(r"<insert path here>\Olympics\summer.csv")
country_data = pd.read_csv(r"<insert path here>\Olympics\country-data.csv")

# explore
summer.count()
summer['Year'].count()
summer.groupby('Athlete').nunique()['Athlete'].count()

# medal counts - run these in the terminal or use print() to see output
summer['Athlete'].value_counts()  # num of rows
summer[summer['Gender']=='Women']
summer[summer['Gender']=='Women']['Athlete'].value_counts()
summer[summer['Gender']=='Women']['Athlete'].value_counts()[:1]

# groupby - run these in the terminal or use print() to see output
summer.groupby(['Athlete', 'Medal'])  # -> GroupBy object
summer.groupby(['Athlete', 'Medal']).count()
summer.groupby(['Athlete', 'Medal'])['Sport'].count()

# Highest number of each medal type
medals = summer.groupby(['Athlete', 'Medal'])['Sport'].count().reset_index().sort_values(by='Sport')
medals = medals.drop_duplicates(subset=['Medal'],keep='last')
medals.columns=['Athlete', 'Medal', 'Count']
print(medals)


# relationships between medal score, gdp and population

# add a score column, default 0
summer['score'] = 0
# other method: summer['score'][summer['Medal'] == 'Gold'] = 4  # setting a value on the copy of a slice
summer.loc[summer['Medal'] == 'Gold', 'score'] = 4
summer.loc[summer['Medal'] == 'Silver', 'score'] = 2
summer.loc[summer['Medal'] == 'Bronze', 'score'] = 1

# score for each country
score_all = summer.groupby(['Country']).sum()['score']
score_all.reset_index().sort_values(by='score')

# add as column to country data
country_data = country_data.merge(score_all.to_frame(), left_on='Code', right_on='Country')

# Regular scatter plot
plt.plot(country_data['Population'], country_data['score'], 'g.')  # other example styles: 'b*', 'rx'
plt.xlabel(r'Population', fontsize = 15)
plt.ylabel(r'Medal Score', fontsize = 15)
plt.show()

# Scatter with log axes
plt.plot(country_data['Population'], country_data['score'], 'g.')
plt.xscale('log'); plt.yscale('log')
plt.xlabel(r'Population', fontsize = 15)
plt.ylabel(r'Medal Score', fontsize = 15)
plt.show()
