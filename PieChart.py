# Plot a pie-chart of the number of models released by every manufacturer,
# recorded in the data provide. Also mention the name of the manufacture with
# the largest releases.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Cars.csv', delimiter=',')
print(df)

df['count'] = df.groupby('Make')['Make'].transform('count')
df.drop_duplicates('Make', inplace=True)
df.sort_values(by='count', ascending=False, inplace=True)
# Based on the count obtain we will plot our graph.
plt.figure(figsize=(50, 8))
ax1 = plt.subplot(121, aspect='equal')
df.plot(kind='pie', y='count', ax=ax1, autopct='%1.1f%%', startangle=90, shadow=False,
        labels=df['Make'], legend=False,
        fontsize=10)
plt.show()
