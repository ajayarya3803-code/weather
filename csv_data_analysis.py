import pandas as pd
import csv
from matplotlib import pyplot as plt

data=pd.read_csv("new_data.csv")

plt.figure(figsize=(10,6))
plt.plot(data['date'],data['max_temperature'],marker="o",label="Max Temperature")
plt.plot(data['date'],data['min_temperature'],marker="o",label="Min Temperature")
plt.xlabel("Dates")
plt.ylabel("Temperatures")
plt.title("Temperature over week")
plt.xticks(rotation=45)
plt.legend()
plt.savefig('temperature_data.png')
plt.show()

