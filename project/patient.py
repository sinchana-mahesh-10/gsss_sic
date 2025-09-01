import pandas as pd
from datetime import datetime

# Step 1: Load Dataset
df = pd.read_csv('patient_admissions.csv')

# Step 2: Check Data Quality
print("Missing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nDuplicate Rows:", df.duplicated().sum())

# Step 3: Handle Missing Values
# Fill missing Diagnosis with "Unknown"
df['Diagnosis'] = df['Diagnosis'].fillna('Unknown')

# Fill missing DischargeDate with today's date (simulate ongoing admission)
today = pd.to_datetime('today').normalize()
df['DischargeDate'] = df['DischargeDate'].fillna(today)

# Step 4: Data Type Conversion
df['AdmissionDate'] = pd.to_datetime(df['AdmissionDate'])
df['DischargeDate'] = pd.to_datetime(df['DischargeDate'])

# Step 5: Create Derived Column - StayDuration
df['StayDuration'] = (df['DischargeDate'] - df['AdmissionDate']).dt.days

# Step 6: Filter Data - Cardiology patients with StayDuration > 5
filtered_df = df[(df['Department'] == 'Cardiology') & (df['StayDuration'] > 5)]
print("\nFiltered Cardiology Patients with StayDuration > 5:\n", filtered_df)

# Step 7: Group and Aggregate
# a. Number of admissions per Department
admission_counts = df['Department'].value_counts()
print("\nAdmission Counts by Department:\n", admission_counts)

# b. Average stay duration per Department
avg_stay = df.groupby('Department')['StayDuration'].mean()
print("\nAverage Stay Duration by Department:\n", avg_stay)

# Step 8: Sort by StayDuration (Descending)
sorted_df = df.sort_values(by='StayDuration', ascending=False)
print("\nTop Patients by Stay Duration:\n", sorted_df[['PatientID', 'Name', 'StayDuration']])

# Step 9: Remove Duplicates (based on PatientID and AdmissionDate)
df = df.drop_duplicates(subset=['PatientID', 'AdmissionDate'])

# Step 10: Export Transformed Data
df.to_csv('transformed_admissions.csv', index=False)
print("\nTransformed data saved to 'transformed_admissions.csv'")
