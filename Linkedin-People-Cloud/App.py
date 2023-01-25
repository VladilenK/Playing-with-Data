import pandas as pd

# I have data saved from Linkedin: number of people if "Search for" in "Region" 

# cloud_people = pd.read_csv("Linkedin_People_Cloud.csv", index_col="Search for")
cloud_people = pd.read_csv("Linkedin_People_Cloud.csv")
cloud_people.insert(0, "SfR", "tbd")
cloud_people["SfR"] = cloud_people["Search for"] + " in " + cloud_people["Region"]
cloud_people = cloud_people.set_index(["SfR"])
cloud_people = cloud_people.transpose()

print(cloud_people.head(7))
# print(cloud_people.info())
# print(cloud_people.describe())

