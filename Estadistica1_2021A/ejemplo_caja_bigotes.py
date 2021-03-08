import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

csv_data = pd.read_csv("C:\\Users\\likyb\\Documents\\GitHub\\Uninorte\\Estadistica1_2021A\\TGLS.csv")
print(csv_data.head())

OpenList = csv_data.Open.tolist()
ax=sns.boxplot(x=OpenList)
plt.show()