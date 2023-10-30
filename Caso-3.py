import pandas as pd
# Filtrar 
condition_shared = df_airbnb['room_type'] == 'Shared room'
condition_budget = df_airbnb['price'] <= 50
df_filtered = df_airbnb[condition_shared & condition_budget]
df_sorted = df_filtered.sort_values(['price', 'overall_satisfaction'], ascending=[True, False])
top_10_properties = df_sorted.head(10)

print(top_10_properties)
