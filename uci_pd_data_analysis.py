# Access UCI Data Set To Run This

# I will be using my Google Drive to access all imported data for this project
# Links and files will be posted for access in the 'Resources' folder

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

uciRead = pd.read_csv("/content/drive/MyDrive/Parkinson's Research/Datasets/uci-pd-data.csv", index_col = "Unnamed: 0")

uciRead["Demographic information"] = pd.to_numeric(uciRead["Demographic information"], errors="coerce") # The "Age (Years)" subcolumn causes Pandas to interpret the greater column as text
uciRead["Medication.5"] = pd.to_numeric(uciRead["Medication.5"], errors="coerce")

youngProfiles = uciRead[uciRead["Demographic information"] < 50] # Give me all healthy and diagnosed profiles below the age of 50
middleProfiles = uciRead.loc[(uciRead["Demographic information"] >= 50) & (uciRead["Demographic information"] < 65) & (uciRead["Medication"] == "No") & (uciRead["Medication.3"] == "No") & (uciRead["Medication.5"] == 0)] # Give me all healthy and diagnosed profiles between 50 and 65
olderProfiles = uciRead[uciRead["Demographic information"] >= 65]

# Commands to make searching for cohorts easier

# print(youngProfiles.to_string())

command = input("Command: ")

if command == "Young Cohort":
  try:
    print(youngProfiles.to_string())
  except KeyError:
    print(f"{command} does not exist")

elif command == "Middle Cohort":
  try:
    print(middleProfiles.to_string())
  except KeyError:
    print(f"{command} does not exist")

elif command == "Older Cohort":
  try:
    print(olderProfiles.to_string())
  except KeyError:
    print(f"{command} does not exist")