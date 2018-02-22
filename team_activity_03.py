"""
CS450 - Machine Learning
A record of all the ugly code used as part of an in-class team activity
Practice using Pandas and Numpy with data sets
"""

import pandas as pd
import numpy as np


data_columns = ["age", "workclass", "final_weight", "education", "education_num",
                "marital_status", "occupation", "relationship", "race", "sex",
                "capital_gain", "capital_loss", "hours_per_week", "native_country", "target"]

data = pd.read_csv("/Users/brycekaline/Downloads/adult.data.txt", names = data_columns, header = None)
data.as_matrix()

age = np.int64(data["age"].mean())
workclass = data["workclass"].mode()[0].strip()
final_weight = np.int64(data["final_weight"].mean())
education = data["education"].mode()[0].strip
education_num = np.int64(data["education_num"].mean())
marital_status = data["marital_status"].mode()[0].strip()
occupation = data["occupation"].mode()[0].strip()
relationship = data["relationship"].mode()[0].strip()
race = data["race"].mode()[0].strip()
sex = data["sex"].mode()[0].strip()
capital_gain = np.int64(data["capital_gain"].mean())
capital_loss = np.int64(data["capital_loss"].mean())
hours_per_week = np.int64(data["hours_per_week"].mean())
native_country = data["native_country"].mode()[0].strip()

list = [age, workclass, final_weight, education, education_num,
                marital_status, occupation, relationship, race, sex,
                capital_gain, capital_loss, hours_per_week, native_country]

print(data.workclass.value_counts())

data["workclass"] = data["workclass"].apply(lambda v: v.replace('?', workclass))

for column in list:
   data["{}".format(column)] = data.column.apply(lambda v: v.replace('?', column))

print(data.workclass.value_counts())

data["workclass"] = data["workclass"].astype("category").cat.codes
data["education"] = data["education"].astype("category").cat.codes
data["marital_status"] = data["marital_status"].astype("category").cat.codes
data["occupation"] = data["occupation"].astype("category").cat.codes
data["relationship"] = data["relationship"].astype("category").cat.codes
data["race"] = data["race"].astype("category").cat.codes
data["sex"] = data["sex"].astype("category").cat.codes
data["native_country"] = data["native_country"].astype("category").cat.codes

#print(data.workclass.unique())
#print(data.marital_status.unique())

#data["workclass"] = data.workclass.apply(lambda v: v.replace("?", "X"))

#print(data.target)
#print(data.workclass.value_counts())

#print(data.mode())

# data["workclass"].value_counts()

# pandas reads txt/csv missing value "?" as " ?"

