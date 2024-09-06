import pandas as pd

#countries_data = pd.read_csv('data/countries.csv', sep=';')
#print (countries_data)

#data = pd.read_csv('https://github.com/Yuri-VN/IDE/blob/main/data/countries.csv')
#print (data)

melb_data_fe = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data_fe.csv')
#print(melb_data_fe.head())

melb_data_fe['Date'] = pd.to_datetime(melb_data_fe['Date'])
popula_quarter = melb_data_fe['Date'].dt.quarter.value_counts()
print (popula_quarter)