'''
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows
tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in
the 4th segment and sugarcane in the 5th segment.
He is converting his land from chemical-driven farming to chemical-free farming. Mahesh starts with
the conversion of vegetables into chemical-free produce. He spends the first 6 months doing the same.
He then converts the sunflower land bank into chemical-free farming. This takes him another 4
months. Finally, he converts sugarcane into chemical-free farming over the next 4 months.
He gets a yield of the following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre.
The remaining 70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato
is Rs. 7 per Kg.
The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20.
The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24.
The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200.
The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000.
All the crops are sowed at the same time. Mahesh gets the above yield at the above-mentioned rate
in one crop cycle across his entire land of 80 acres.
What is
a. The overall sales achieved by Mahesh from the 80 acres of land.
b. Sales realisation from chemical-free farming at the end of 11 months?
'''
# Total land and segments
total_land = 80
segments = 5
land_per_crop = total_land / segments  # 16 acres per crop

# --- Tomatoes ---
# 30% at 10 tonnes/acre, 70% at 12 tonnes/acre
tomato_area = land_per_crop
tomato_price = 7  # per kg

tomato_area_30 = 0.3 * tomato_area
tomato_area_70 = 0.7 * tomato_area

tomato_yield_30 = tomato_area_30 * 10 * 1000  # in kg
tomato_yield_70 = tomato_area_70 * 12 * 1000  # in kg

tomato_total_yield = tomato_yield_30 + tomato_yield_70
tomato_sales = tomato_total_yield * tomato_price

# --- Potatoes ---
potato_yield_per_acre = 10  # tonnes
potato_price = 20  # per kg
potato_yield = land_per_crop * potato_yield_per_acre * 1000  # in kg
potato_sales = potato_yield * potato_price

# --- Cabbage ---
cabbage_yield_per_acre = 14
cabbage_price = 24
cabbage_yield = land_per_crop * cabbage_yield_per_acre * 1000  # in kg
cabbage_sales = cabbage_yield * cabbage_price

# --- Sunflower ---
sunflower_yield_per_acre = 0.7
sunflower_price = 200
sunflower_yield = land_per_crop * sunflower_yield_per_acre * 1000  # in kg
sunflower_sales = sunflower_yield * sunflower_price

# --- Sugarcane ---
sugarcane_yield_per_acre = 45  # in tonnes
sugarcane_price = 4000  # per tonne
sugarcane_yield = land_per_crop * sugarcane_yield_per_acre  # in tonnes
sugarcane_sales = sugarcane_yield * sugarcane_price

# Total sales
total_sales = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales +
    sugarcane_sales
)

# Chemical-free sales after 11 months (excluding sugarcane)
chemical_free_sales = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales
)

# Print results
print("Total sales from 80 acres of land: Rs.", total_sales)
print("Sales from chemical-free farming after 11 months: Rs.", chemical_free_sales)
