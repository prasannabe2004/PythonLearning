# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars)

# Print out drive_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])