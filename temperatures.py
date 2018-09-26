import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

temps = pd.read_csv(r"<insert path here>\Berkeley Earth\Berkeley time series.csv", usecols=[0, 1, 2, 4])

temps.insert(2, 'day', 1)
temps.insert(3, 'date', pd.to_datetime(temps[['year', 'month', 'day']]))
temps.set_index('date', inplace=True)

temps.plot(y="Monthly anomaly")

figure, ax = plt.subplots()
temps.plot(ax=ax, y="Monthly anomaly")
temps.resample('AS').mean().plot(ax=ax, y="Monthly anomaly")

temps.groupby(temps.index.month).mean().plot(y="Monthly anomaly")