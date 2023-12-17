import pandas as pd

# Load the original CSV file into a DataFrame
original_file = "1. malicious_phish (original).csv"
df = pd.read_csv(original_file)

# Define a function to categorize types into "benign" and "malicious"
def categorize_type(row):
    if row["type"] in ["defacement", "malware", "phishing"]:
        return "malicious"
    else:
        return "benign"

# Apply the categorization function to create a new column "category"
df["category"] = df.apply(categorize_type, axis=1)

# Drop the original "type" column
df.drop(columns=["type"], inplace=True)

# Save the updated DataFrame to a new CSV file
new_file = "2. updated_urls (benign and malicious only).csv"
df.to_csv(new_file, index=False)
