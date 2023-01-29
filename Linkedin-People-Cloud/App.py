"""..."""
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt 
# %matplotlib inline

# I have data saved from Linkedin: number of people if "Search for" in "Region" 

# cloud_people = pd.read_csv("Linkedin_People_Cloud.csv", index_col=["Search for", "Region"])
cloud_people = pd.read_csv("Linkedin_People_Cloud.csv")
cloud_people.insert(0, "SfR", "tbd")
cloud_people["SfR"] = cloud_people["Search for"] + " in " + cloud_people["Region"]
cloud_people = cloud_people.set_index(["SfR"])
cloud_people = cloud_people.transpose().dropna()

print(cloud_people.head(5))
print(cloud_people.tail(5))
print(cloud_people.info())
print(cloud_people.describe())

# print(cloud_people)


# bb = data.DataReader(name = "BB", data_source = "yahoo", start = "2007-01-01", end = "2021-01-01")

# cloud_people.plot()
# cloud_people.plot(y = '"SharePoint" in Global' )
print(cloud_people['"SharePoint" in Global'])
# cloud_people['"SharePoint" in Global'].plot()

s = [1,2,2,3,4,5]



