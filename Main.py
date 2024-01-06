#importing all necessary libraries: 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
import numpy as np
'''
#reading csv file: 
data = 'Madrid Daily Weather 1997-2015.csv' 
df = pd.read_csv(data) 
print(df) 
'''
data = pd.read_csv('Madrid Daily Weather 1997-2015.csv')
#print (data)

#convert CET column to datetime format:
data['CET'] = pd.to_datetime(data['CET'])

#set CET column as the index - time-based operations, readability and functionality:
data.set_index('CET', inplace=True)

#max and min temp over time:
'''plt.figure
sns.lineplot(x=data.index, y=data['Max TemperatureC'])
plt.title('Max Temperature Over Time')
plt.xlabel('Year')
plt.ylabel('Max Temperature (C)')
plt.show()
'''



########### STUFF THAT WORKS ###############
plt.figure
sns.lineplot(x=data.index, y=data['Max TemperatureC'], label='Max Temperature')
sns.lineplot(x=data.index, y=data['Min TemperatureC'], label='Min Temperature')
plt.title('Max and Min Temperature Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature (C)')
plt.legend()
plt.show()



#anomaly plot to show trends:
plt.figure(figsize=(12, 6))
mean_temp_reference = data['Mean TemperatureC'].mean()
temperature_anomaly = data['Mean TemperatureC'] - mean_temp_reference
sns.lineplot(x=data.index, y=temperature_anomaly)
plt.title('Temperature Anomaly Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (C)')
plt.show()



#seasonal Decomposition:
from statsmodels.tsa.seasonal import seasonal_decompose
data['Mean TemperatureC'] = data['Mean TemperatureC'].interpolate()

decomposition = seasonal_decompose(data['Mean TemperatureC'], period=12)

plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(data.index, decomposition.trend, label='Trend')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(data.index, decomposition.seasonal, label='Seasonal')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(data.index, decomposition.resid, label='Residual')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(data.index, data['Mean TemperatureC'], label='Original')
plt.legend()

plt.suptitle('Seasonal Decomposition of Mean Temperature')
plt.show()



#heatmap for correlation:
numeric_columns = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_columns.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(12, 10))
cmap = sns.diverging_palette(220, 20, as_cmap=True)
sns.heatmap(correlation_matrix, annot=True, cmap=cmap, mask=mask, vmin=-1, vmax=1, linewidths=.5, fmt=".2f", cbar_kws={'label': 'Correlation'})
plt.xlabel('Features')
plt.ylabel('Features')
plt.title('Correlation Heatmap', fontsize=16)
plt.tight_layout()
plt.show()



#wind direction rose diagram:
wind_data = data.dropna(subset=['WindDirDegrees'])

#create a wind direction rose diagram with gradient colors
plt.figure(figsize=(12, 12))
ax = plt.subplot(111, polar=True)

#convert degrees to radians for polar plot
theta = np.radians(wind_data['WindDirDegrees'])

#set up a colormap
cmap = ListedColormap(plt.cm.Blues(np.linspace(0.2, 1, 36)))

#create a histogram with bars for each 10-degree bin
bars = ax.bar(np.arange(0, 2*np.pi, np.pi/18), np.histogram(theta, bins=36)[0], width=np.pi/18, color=[cmap(i) for i in range(36)])

#add color scale
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap), ax=ax, pad=0.1)
cbar.set_label('Frequency')

#add labels and title
ax.set_theta_direction(-1)  # Clockwise
ax.set_theta_offset(np.pi / 2.0)  # Set 0 degrees at the top
ax.set_rlabel_position(90)
ax.set_yticklabels([])
ax.set_title('Wind Direction Rose Diagram', va='bottom', pad=20)

#add compass direction labels
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
ax.set_xticks(np.arange(0, 2*np.pi, np.pi/4))
ax.set_xticklabels(directions)

plt.show()


'''
#pair plot for multiple variables - ####### looks ugly might not make the final cut ############
sns.pairplot(data[['Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Humidity', ' Mean Humidity']])
plt.suptitle('Pair Plot of Temperature and Humidity', y=1.02)
plt.show()


#facet grid for seasonal analysis - ####### looks ugly might not make the final cut ############
g = sns.FacetGrid(data, col=" Events", col_wrap=3, height=4)
g.map(sns.lineplot, "Mean TemperatureC", "Max Humidity", marker="o", ci=None)
g.set_axis_labels("Mean Temperature (C)", "Max Humidity")
g.set_titles(col_template="{col_name}")
plt.suptitle('Seasonal Analysis of Temperature and Humidity', y=1.02)
plt.show()
'''