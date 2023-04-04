import pandas as pd

df = pd.read_csv('C:/Users/palaa/OneDrive/Desktop/whitehat/python/c130/pro/total_stars.csv')
del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']

df.to_csv('cleaned_file.csv')