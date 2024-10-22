import pandas as pd
import os

# Read the txt file
txt_df = pd.read_csv("newfile.txt", header=None)
txt_df.columns = ["ID", "Text"]

# Read the CSV file
csv_df = pd.read_csv("./Unit 5/Sample_CSV.csv")

# Merge the DataFrames on the "ID" column
merged_df = pd.merge(csv_df, txt_df, on="ID", how="outer")

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("Merged.csv", index=False)

print("Merged.csv created successfully.")