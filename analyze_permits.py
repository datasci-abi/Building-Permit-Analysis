import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file (starting from real data rows)
df = pd.read_excel("statemonthly_202503.xls", skiprows=10)

# Rename relevant columns
df = df[['Unnamed: 0', 'Unnamed: 13']]
df.columns = ['State', 'Total']

# Remove non-state rows
df = df[df['State'].notnull()]
df = df[~df['State'].str.contains('Region|Division|United States', na=False)]

# Convert Total to numeric
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

# Drop any remaining NaNs
df = df.dropna(subset=['Total'])

# Add percentage share column
df['Share_%'] = (df['Total'] / df['Total'].sum()) * 100

# ========== INSIGHT 1: Total permits issued nationwide ==========
total_us = df['Total'].sum()
print(f"\n🏗️ Total permits issued nationwide in March 2025: {int(total_us):,}")

# ========== INSIGHT 2: Top 10 states ==========
top_states = df.sort_values(by='Total', ascending=False).head(10)
print("\n📈 Top 10 States by Permits Issued:")
print(top_states[['State', 'Total', 'Share_%']])

# Plot top 10
plt.figure(figsize=(10, 6))
plt.bar(top_states['State'], top_states['Total'])
plt.title("Top 10 States by Building Permits (March 2025)")
plt.xlabel("State")
plt.ylabel("Units Permitted")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ========== INSIGHT 3: Bottom 10 states ==========
bottom_states = df.sort_values(by='Total', ascending=True).head(10)
print("\n📉 Bottom 10 States by Permits Issued:")
print(bottom_states[['State', 'Total', 'Share_%']])

# Plot bottom 10
plt.figure(figsize=(10, 6))
plt.bar(bottom_states['State'], bottom_states['Total'])
plt.title("Bottom 10 States by Building Permits (March 2025)")
plt.xlabel("State")
plt.ylabel("Units Permitted")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ========== Export ==========
df.to_csv("march_2025_permit_insights.csv", index=False)
print("\n✅ Data exported to 'march_2025_permit_insights.csv'")
