import pandas as pd
import numpy as np
df = pd.read_csv("preprocessing.csv")
print("Original Data:\n", df)
if "ID" in df.columns:
    df = df.drop(columns=["ID"])
df = df.dropna(thresh=3)  
num_cols = [col for col in ["Age", "Salary", "Experience"] if col in df.columns]
for col in num_cols:
    mean_val = df[col].mean()
    df[col] = df[col].fillna(mean_val)
cat_cols = [col for col in ["Name", "Department"] if col in df.columns]
for col in cat_cols:
    mode_val = df[col].mode()[0]
    df[col] = df[col].fillna(mode_val)
for col in cat_cols:
    df[col] = df[col].astype("category").cat.codes
for col in num_cols:
    mean = df[col].mean()
    std = df[col].std()
    df[col] = (df[col] - mean) / std
if "Salary" in df.columns:
    df = df[np.abs(df["Salary"]) < 3]
print("\nPreprocessed Data:\n", df)
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data saved to cleaned_data.csv")
