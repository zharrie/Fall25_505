import pandas as pd

# Input the file name (only once)
filename = input()

# Read the .tsv file
df = pd.read_csv(filename, sep='\t')

# Output rows by descending Final scores
print(df.sort_values(by='Final', ascending=False))

# Output max scores
print("Max Scores:")
print(df.max(numeric_only=True))

# Output median scores
print("Median Scores:")
print(df.median(numeric_only=True))

# Output average scores
print("Average Scores:")
print(df.mean(numeric_only=True))

# Output standard deviation of scores
print("Standard Deviation:")
print(df.std(numeric_only=True))
