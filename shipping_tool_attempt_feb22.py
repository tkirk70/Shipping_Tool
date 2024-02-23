import pandas as pd
import streamlit as st

ground_zones = pd.read_excel('TCG zone chart.xlsx', sheet_name='ground_zones', dtype=str)

ground_commercial = pd.read_csv("2023_UPS Ground Commercial.csv")
ground_residential = pd.read_csv("2023_UPS Ground Residential.csv")
ground_surepost = pd.read_csv("2023_UPS SurePost - 1lb or greater.csv")

ground_commercial.set_index('lbs', inplace=True)
ground_residential.set_index('lbs', inplace=True)
ground_surepost.set_index('lbs', inplace=True)

# create title, header and subheader
st.title('TCG Shipping Tool', divider='✨')
st.header('Check UPS Shipping Costs')
st.subheader('A TDS Application')

# take input for the zip code
zip_code = st.text_input("What is the zip?", "43123")
weight = st.number_input("What is the weight?", 1)

# zip_code = input(str('What is the zip?'))
# weight = int(input('What is the weight?'))
zip_code_clipped = zip_code[:3]
# Use boolean indexing to extract the names of customers who ordered product A
result = dict(zip(ground_zones['Dest. ZIP'], ground_zones['Ground']))
# result[zip_code_clipped]

c_price = ground_commercial.loc[weight, result[zip_code_clipped][-1]]
r_price = ground_residential.loc[weight, result[zip_code_clipped][-1]]
sure_price = ground_surepost.loc[weight, result[zip_code_clipped][-1]]

from uszipcode import SearchEngine

sr = SearchEngine()
z = sr.by_zipcode(zip_code)
print(z.major_city + ', ' + z.state + '  ' + z.zipcode + ' is in UPS Ground Zone ' + result[zip_code_clipped] + ' for TCG Continuum.')
print(f'A package with a weight of {weight}lbs using {ground_residential.columns[0]} will cost: ${r_price:.2f}.')
print(f'A package with a weight of {weight}lbs using {ground_commercial.columns[0]} will cost: ${c_price:.2f}.')
print(f'A package with a weight of {weight}lbs using {ground_surepost.columns[0]} will cost: ${sure_price:.2f}.')


# figure out how many different ship services to present.

# calculate the distance
import haversine as hs   
from haversine import Unit

loc1=(39.8815, -83.0930)
loc2=(z.bounds_north, z.bounds_east)

distance=hs.haversine(loc1,loc2,unit=Unit.MILES)
print(f'The distance from TCG is: {distance:,.0f} miles.')



# from copilot
# Display results
st.write(z.major_city + ', ' + z.state + '  ' + z.zipcode + ' is in UPS Ground Zone ' + result[zip_code_clipped] + ' for TCG Continuum.')
st.write(f'The distance from TCG is: {distance:,.0f} miles.')
st.write(f"A package with a weight of {weight} lbs using {ground_residential.columns[0]} will cost: ${r_price:.2f}.")
st.write(f"A package with a weight of {weight} lbs using {ground_commercial.columns[0]} will cost: ${c_price:.2f}.")
st.write(f"A package with a weight of {weight} lbs using {ground_surepost.columns[0]} will cost: ${sure_price:.2f}.")

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [39.8815, z.bounds_north],
    'longitude': [-83.0930, z.bounds_east]
})
 
## Create a map with the data
st.map(data, zoom=3)