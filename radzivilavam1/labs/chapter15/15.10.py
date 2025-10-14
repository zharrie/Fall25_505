import pandas as pd

# Read file name from user input
filename = input().strip()

# Read the TSV file into a pandas dataframe
df = pd.read_csv(filename, sep='\t')

# Display students and grades in descending order of Final scores
print(df.sort_values(by="Final", ascending=False).to_string())

# Output max scores
print("\nMax Scores:")
print(df[["Midterm1", "Midterm2", "Final"]].max(numeric_only=True).to_string())

# Output median scores
print("\nMedian Scores:")
print(df[["Midterm1", "Midterm2", "Final"]].median(numeric_only=True).to_string())

# Output average scores
print("\nAverage Scores:")
print(df[["Midterm1", "Midterm2", "Final"]].mean(numeric_only=True).to_string())

# Output standard deviation
print("\nStandard Deviation:")
print(df[["Midterm1", "Midterm2", "Final"]].std(numeric_only=True).to_string())
