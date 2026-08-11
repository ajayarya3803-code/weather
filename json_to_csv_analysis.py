import pandas as pd
import json


def read_file():
    with open("daily_data.json",'r') as f:
        data=json.load(f)
        # for i in data:
        #     print(i)
        df=pd.DataFrame(data['daily'])
        # print(df)
        df.rename(columns={"temperature_2m_max":"max_temperature",
                           "temperature_2m_min":"min_temperature",
                           "time":"date"},inplace=True)
        print(df)
        # print(df.info())

        # df['date']=pd.to_datetime(df['date']) #converted the type of date column to datetime

        # print(df.isnull().sum()) #check for null values

        df.to_csv("new_data.csv",index=False)
    return df
        

if __name__=="__main__":
    read_file()

         