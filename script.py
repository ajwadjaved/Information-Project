import pandas as pd

# Read the CSV file
df = pd.read_csv('historical_tuition.csv')

# Extract the year from the 'year' column
df['year'] = df['year'].str.extract('(\d{4})')

# Convert 'year' column to numeric
df['year'] = pd.to_numeric(df['year'])

# Remove the years 2009 and 2012
df = df[~df['year'].isin([2009, 2012])]

# Rearrange the columns
df = df[['year', 'type', 'tuition_type', 'tuition_cost']]

# Sort the DataFrame by 'year'
df_sorted = df.sort_values(by='year')

# Save the sorted and rearranged data back to a new CSV file
df_sorted.to_csv('updated_historical_tuition.csv', index=False)
