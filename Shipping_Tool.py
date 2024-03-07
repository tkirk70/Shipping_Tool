import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
)

# st.balloons()

ground_zones = pd.read_excel('TCG zone chart.xlsx', sheet_name='ground_zones', dtype=str)

ground_commercial = pd.read_csv("2023_UPS Ground Commercial.csv")
ground_residential = pd.read_csv("2023_UPS Ground Residential.csv")
ground_surepost = pd.read_csv("2023_UPS SurePost - 1lb or greater.csv")

ground_commercial.set_index('lbs', inplace=True)
ground_residential.set_index('lbs', inplace=True)
ground_surepost.set_index('lbs', inplace=True)

# create title, header and subheader
st.title('TCG Shipping Tool')
# st.divider('✨')
st.divider()
st.header('Check UPS Shipping Costs')
# st.subheader('A TDS Application')

# take input for the zip code
col4, col5 = st.columns(2)
with col4:
    zip_code = st.text_input("What is the zip?", "43123")
    
with col5:
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


# calculate the distance
import haversine as hs   
from haversine import Unit

loc1=(39.8815, -83.0930)
loc2=(z.bounds_north, z.bounds_east)

distance=hs.haversine(loc1,loc2,unit=Unit.MILES)
print(f'The distance from TCG is: {distance:,.0f} miles.')


st.write(z.major_city + ', ' + z.state + '  ' + z.zipcode + ' is in UPS Ground Zone ' + result[zip_code_clipped] + ' for TCG Continuum.')
st.write(f'The distance from TCG is: {distance:,.0f} miles.')
        
col1, col2, col3 = st.columns(3)

with col1:
    length = st.number_input("Length", 1)
    
with col2:
    width = st.number_input("Width", 1)
    
with col3:
    height = st.number_input("Height", 1)
    
dim_weight = length * width * height / 139

if dim_weight > weight:
    st.write(f'The dimensional weight of your package is: {int(round(dim_weight, 0))}lbs.')
    st.write('**USE DIMENSIONAL WEIGHT**')
else:
    st.write(f'The dimensional weight of your package is: {int(round(dim_weight, 0))}lbs.')



# from uszipcode import SearchEngine

# sr = SearchEngine()
# z = sr.by_zipcode(zip_code)
# print(z.major_city + ', ' + z.state + '  ' + z.zipcode + ' is in UPS Ground Zone ' + result[zip_code_clipped] + ' for TCG Continuum.')
# print(f'A package with a weight of {weight}lbs using {ground_residential.columns[0]} will cost: ${r_price:.2f}.')
# print(f'A package with a weight of {weight}lbs using {ground_commercial.columns[0]} will cost: ${c_price:.2f}.')
# print(f'A package with a weight of {weight}lbs using {ground_surepost.columns[0]} will cost: ${sure_price:.2f}.')


# figure out how many different ship services to present.



# try adding buttons to sidebar
with st.sidebar:
    st.button("Cost", type="primary")
    if st.button('Upcharge', type="primary"):
        st.write("**:orange[20% Surcharge for Customer]**")
        multiplier = 1.2
    else:
        st.write("**:orange[TCG Cost]**")
        multiplier = 1


# # add multiplier button for TCG or Customer cost
# st.button("Cost", type="primary")
# if st.button('Upcharge', type="primary"):
#     st.write("**:orange[20% Surcharge for Customer]**")
#     multiplier = 1.2
# else:
#     st.write("**:orange[TCG Cost]**")
#     multiplier = 1

# from copilot
# Display results
# st.write(z.major_city + ', ' + z.state + '  ' + z.zipcode + ' is in UPS Ground Zone ' + result[zip_code_clipped] + ' for TCG Continuum.')
# st.write(f'The distance from TCG is: {distance:,.0f} miles.')
st.write(f"A package with a weight of {weight} lbs using {ground_residential.columns[0]} will cost: ${multiplier*r_price:.2f}.")
st.write(f"A package with a weight of {weight} lbs using {ground_commercial.columns[0]} will cost: ${multiplier*c_price:.2f}.")
st.write(f"A package with a weight of {weight} lbs using {ground_surepost.columns[0]} will cost: ${multiplier*sure_price:.2f}.")

st.divider()

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [39.8815, z.bounds_north],
    'longitude': [-83.0930, z.bounds_east]
})
 
## Create a map with the data
st.map(data, zoom=3)

# st.subheader('A TDS Application')
# st.markdown('<div style="text-align: right;">A TDS Application</div>', unsafe_allow_html=True)

# Custom CSS style for the text
custom_style = '<div style="text-align: right; font-size: 20px;">✨ A TDS Application ✨</div>'

# Render the styled text using st.markdown
st.markdown(custom_style, unsafe_allow_html=True)
