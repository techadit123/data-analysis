 #Identify and Handle Missing Values
import pandas as pd

# Load data
df = pd.read_csv("your_file.csv")

# Identify missing values
missing_values = df.isnull().sum()

# Example: Drop rows with missing values
df_clean = df.dropna()

# Or: Fill missing values
df['column_name'].fillna('default_value', inplace=True)
#Remove Duplicate Rows

df = df.drop_duplicates()
#Standardize Text Values (e.g., gender, country)


# Example: Gender
df['gender'] = df['gender'].str.strip().str.lower().replace({'female': 'f', 'male': 'm'})

# Example: Country
df['country'] = df['country'].str.title()
#Convert Date Formats
df['date_column'] = pd.to_datetime(df['date_column'], dayfirst=True)  # for dd-mm-yyyy
#Rename Column Headers (clean and uniform)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
#Check and Fix Data Types
df['age'] = df['age'].astype(int)
df['date_column'] = pd.to_datetime(df['date_column'])








