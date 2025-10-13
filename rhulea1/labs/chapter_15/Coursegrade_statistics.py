import pandas as pd

file_name = input()

#Read in file_name as a dataframe
df = pd.read_csv(file_name, sep="\t")

df["Lname"] = df["Lname"].str.strip()
df["Fname"] = df["Fname"].str.strip()

#Output rows by descending Final scores
df_sorted = df.sort_values(by="Final", ascending=False)
print(df_sorted.to_string())

print("\nMax Scores:")
#Output the max scores of each assignment
print(df.max(numeric_only=True).to_string())

print("\nMedian Scores:")
#Output the median scores of each assignment
print(df.median(numeric_only=True).to_string())

print("\nAverage Scores:")
#Output the average scores of each assignment.
print(df.mean(numeric_only=True).to_string())

print("\nStandard Deviation:")
#Output the standard devation of each assignment.
print(df.std(numeric_only=True).to_string())
