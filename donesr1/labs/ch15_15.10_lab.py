import pandas as pd

# Step 1: Read the TSV file from user input
file_name = input()
df = pd.read_csv(file_name, sep='\t')

# Step 2: Output students' names and grades in descending order of Final scores
print(df.sort_values(by='Final', ascending=False).to_string())

print("\nMax Scores:")
print(df.max(numeric_only=True).to_string())

print("\nMedian Scores:")
print(df.median(numeric_only=True).to_string())

print("\nAverage Scores:")
print(df.mean(numeric_only=True).to_string())

print("\nStandard Deviation:")
print(df.std(numeric_only=True).to_string())
