import pandas as pd

# Load data
df = pd.read_csv('data/marketing_data.csv')

# KPIs
df['CTR'] = df['clicks'] / df['impressions']
df['Conversion Rate'] = df['conversions'] / df['clicks']
df['Cost per Conversion'] = df['spend'] / df['conversions']

# Summary
summary = df.groupby('campaign')[['CTR', 'Conversion Rate', 'Cost per Conversion']].mean()
print("Campaign Performance Summary:\n", summary)

# Detect anomalies (high CTR)
threshold = df['CTR'].mean() + 2*df['CTR'].std()
anomalies = df[df['CTR'] > threshold]
print("\nAnomalies:\n", anomalies)