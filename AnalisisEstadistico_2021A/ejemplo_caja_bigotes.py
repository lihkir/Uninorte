import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

csv_data = pd.read_csv("C:\\Users\\likyb\\Documents\\GitHub\\Uninorte\\AnalisisEstadistico_2021A\\volcano_data_2010.csv")
print(csv_data.head())

LongitudeList = csv_data.Longitude.tolist()
ax=sns.boxplot(x=LongitudeList)
plt.show()