import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV files with blank lines skipped
july_df = pd.read_csv('july.csv', skip_blank_lines=True)
december_df = pd.read_csv('december.csv', skip_blank_lines=True)

# Step 2: Clean column headers (strip whitespace)
july_df.columns = july_df.columns.str.strip()
december_df.columns = december_df.columns.str.strip()

# Step 3: Drop rows with any missing critical data to avoid misalignment
july_df.dropna(subset=['Month', 'Year', 'Capacity', 'Gross Potential'], inplace=True)
december_df.dropna(subset=['Month', 'Year', 'Capacity', 'Gross Potential'], inplace=True)

# Step 4: Convert columns to correct types (ints)
for df in [july_df, december_df]:
    df['Month'] = df['Month'].astype(int)
    df['Year'] = df['Year'].astype(int)
    df['Capacity'] = df['Capacity'].astype(int)
    df['Gross Potential'] = df['Gross Potential'].astype(int)

# Step 5: Print dataframes
print(july_df)
print()
print(december_df)

# Step 6: Extract month and year from the data (assuming all rows have the same)
july_month = july_df['Month'].iloc[0]
july_year = july_df['Year'].iloc[0]

dec_month = december_df['Month'].iloc[0]
dec_year = december_df['Year'].iloc[0]

# Step 7: Plotting the scatter plots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.scatter(july_df['Gross Potential'], july_df['Capacity'], color='blue')
ax1.set_title(f'{july_month} {july_year}')
ax1.set_xlabel('Gross Potential')
ax1.set_ylabel('Capacity')

ax2.scatter(december_df['Gross Potential'], december_df['Capacity'], color='green')
ax2.set_title(f'{dec_month} {dec_year}')
ax2.set_xlabel('Gross Potential')
ax2.set_ylabel('Capacity')

fig.suptitle('Capacity vs. Gross Potential', fontsize=16)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('subplots.png')
plt.close()
