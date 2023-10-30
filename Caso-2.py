import pandas as pd

df_roberto = df_airbnb[df_airbnb['id'] == 97503]
df_clara = df_airbnb[df_airbnb['id'] == 90387]

df_combined = pd.concat([df_roberto, df_clara])

# Guardar el dataframe
df_combined.to_excel('roberto.xls', index=False)
