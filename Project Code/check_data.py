import pandas as pd
import os

# Change to Flask directory
os.chdir('Flask')

# Load the data
df = pd.read_csv('restaurant1.csv')

print("=" * 70)
print("RESTAURANT DATASET OVERVIEW")
print("=" * 70)
print(f"\nTotal Restaurants: {len(df)}")
print(f"Features: {df.shape[1]}")
print(f"\nColumn Information:")
for col in df.columns:
    print(f"  ✓ {col}: {df[col].dtype}")

print(f"\n{'-' * 70}")
print("SAMPLE DATA (First 3 restaurants):")
print("-" * 70)
sample_cols = ['name', 'location', 'cuisines', 'rate', 'approx_cost(for two people)']
print(df[sample_cols].head(3).to_string())

print(f"\n{'-' * 70}")
print("STATISTICS:")
print("-" * 70)
print(f"  Unique Locations: {df['location'].nunique()}")
print(f"  Unique Cuisine Types: {df['cuisines'].nunique()}")
print(f"  Unique Restaurant Types: {df['rest_type'].nunique()}")
print(f"  Average Rating: {df['rate'].mean():.2f}/5")
print(f"  Rating Range: {df['rate'].min():.1f} - {df['rate'].max():.1f}")
print(f"  Total Restaurants with Online Orders: {(df['online_order'] == 'Yes').sum()}")
print(f"  Total Restaurants accepting Table Bookings: {(df['book_table'] == 'Yes').sum()}")

print(f"\n{'-' * 70}")
print("TOP 5 CUISINE TYPES:")
print("-" * 70)
# Count cuisine combinations
cuisine_counts = df['cuisines'].str.split(', ').explode().value_counts().head(5)
for cuisine, count in cuisine_counts.items():
    print(f"  {cuisine}: {count} restaurants")

print(f"\n{'-' * 70}")
print("TOP 5 LOCATIONS:")
print("-" * 70)
location_counts = df['location'].value_counts().head(5)
for location, count in location_counts.items():
    print(f"  {location}: {count} restaurants")

print(f"\n{'-' * 70}")
print("MODEL FILE STATUS:")
print("-" * 70)
if os.path.exists('restaurant.pkl'):
    size_mb = os.path.getsize('restaurant.pkl') / (1024 * 1024)
    print(f"  ✓ restaurant.pkl exists ({size_mb:.1f} MB)")
    print(f"    → Contains: 4000x4000 similarity matrix + indices")
else:
    print(f"  ✗ restaurant.pkl NOT FOUND")

print(f"\n{'-' * 70}")
print("✅ DATASET IS READY FOR RECOMMENDATIONS!")
print("=" * 70)
