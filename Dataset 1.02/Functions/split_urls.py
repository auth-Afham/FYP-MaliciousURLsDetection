import pandas as pd
from urllib.parse import urlsplit

# Load the original CSV file
df = pd.read_csv("2. updated_urls (benign and malicious only).csv")

# Get the number of rows
num_rows = df.shape[0]

print("Total number of rows in the CSV:", num_rows)

# Split the URL into its components and create new columns
df['protocol'] = df['url'].apply(lambda x: urlsplit(x).scheme)
df['domain'] = df['url'].apply(lambda x: urlsplit(x).netloc)
df['path'] = df['url'].apply(lambda x: urlsplit(x).path)
df['query'] = df['url'].apply(lambda x: urlsplit(x).query)
df['fragment'] = df['url'].apply(lambda x: urlsplit(x).fragment)

# Remove the 'url' column if no longer needed
df.drop(columns=['url'], inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv("3. splitted_urls.csv", index=False)

# Get the number of rows
num_rows = df.shape[0]

print("Total number of rows in the CSV:", num_rows)
