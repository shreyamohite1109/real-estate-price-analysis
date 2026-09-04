import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

# DATA CLEANING

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

# Numerical columns cleaning

df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

# Categorical Column Cleaning

df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera": True, "not approved by rera": False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()

df = df.drop_duplicates()

# print(df)
# print(df.info())

# Question1 : Which is the costliest flat?

costliest_flat = df.loc[df["price"].idxmax()]
print(f"\nThe costliest flat is a {costliest_flat['flat_type']} located in {costliest_flat['locality']}, built by {costliest_flat['builder_name']}. The flat has a BHK count of {costliest_flat['bhk_count']}. The society name is {costliest_flat['society']} and the company name is {costliest_flat['company_name']}.The cost of the flat is {costliest_flat['price']/10000000} Crores.\n")

# Question 2: Which locality has the highest average price?

locality_avg_price = df.groupby("locality")["price"].mean()
print(f"\nThe locality with the highest average price is {locality_avg_price.idxmax()} with an average price of {locality_avg_price.max()} Crores.\n")

# Question 3: Which locality has the highest rate per square foot?

locality_avg_rate = df.groupby("locality")["rate_per_sqft"].mean()
print(f"\nThe locality with the highest average rate per square foot is {locality_avg_rate.idxmax()} with an average rate of {locality_avg_rate.max()} per sqft.\n")


# Question 4: Ready-to-move vs Under-construction pricing

ready_to_move_avg_price = df[df["status"] == "ready to move"]["price"].mean()
under_construction_avg_price = df[df["status"] == "under construction"]["price"].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print(f"\nReady to move property cost more than under-construction properties.")
else:
    print(f"\nUnder-construction properties cost more than ready-to-move properties.\n")    


# Question 5: Does RERA approval affect pricing?

rera_approved_avg_price = df[df["rera_approval"] == True]["price"].mean()
rera_not_approved_avg_price = df[df["rera_approval"] == False]["price"].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print(f"\nRERA-approved properties cost more than non-RERA-approved properties.")
else:
    print(f"\nNon-RERA-approved properties cost more than RERA-approved properties.\n")    


# Question 6: How does area (sqft) impact property price?

sns.scatterplot(data=df, x="area", y="price")
plt.title("Area vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.show()



# Question 7: Which BHK configuration is the most expensive on average?

most_expensive_bhk = df.groupby("bhk_count")["rate_per_sqft"].mean().idxmax()
print(f"\nThe most expensive BHK configuration is {most_expensive_bhk}BHK.\n")

# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?

property_type_price = df.groupby("flat_type")["rate_per_sqft"].mean()
print(f"\nThe costliest property type is {property_type_price.idxmax()} with an average price of {property_type_price.max()} Crores.\n")


# Question 9: Are larger homes always more expensive per square foot?

sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.title("Area vs Rate per Square Foot")
plt.xlabel("Area (sqft)")
plt.ylabel("Rate per Square Foot")
plt.show()
