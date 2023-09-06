import seaborn as sns
import pandas as pd

lb_data = pd.read_csv('lovebfile.csv')
print(lb_data)
# print(lb_data.to_string())
print("hello world")

# price = sns.load_dataset(lb_data)
sns.histplot(data=lb_data, x="name", multiple="stack")