import pandas as pd

file_name = input()

df = pd.read_csv(file_name, sep='\t')
df.columns = df.columns.str.strip()

df['Lname'] = df['Lname'].str.strip()
df['Fname'] = df['Fname'].str.strip()

df_sorted = df.sort_values(["Final"], ascending=False)
print(df_sorted.to_string())

print("\nMax Scores:")
print(df.max(numeric_only=True).to_string())

print("\nMedian Scores:")
print(df.median(numeric_only=True).to_string())

print("\nAverage Scores:")
print(df.mean(numeric_only=True).to_string())

print("\nStandard Deviation:")
print(df.std(numeric_only=True).to_string())
