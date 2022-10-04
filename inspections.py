import pandas as pd
import matplotlib.pyplot as plt
# from secret_values import api_key, signature
# import gmaps
# import gmaps.datasets
# import requests

# gmaps.configure(api_key=api_key)
# locations = earthquake_df[['latitude', 'longitude']]
# weights = earthquake_df['magnitude']
# fig = gmaps.figure()
# fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
# fig

violations = pd.read_csv("Louisville_Metro_KY_-_Inspection_Violations_of_Failed_Restaurants.csv")
violations.InspectionDate = pd.to_datetime(violations.InspectionDate, format="%Y/%m/%d")
violations.plot(x="InspectionDate", y="score", kind="line")
violations["full_address"] = violations.premise_adr1_num + " " + violations.premise_adr1_street


points = pd.read_csv("Jefferson_County_KY_Address_Points.csv")
points.rename(columns={"FULL_ADDRESS": "full_address"}, inplace=True)

violations_geocoded = violations.merge(points, on=["full_address"])
# wind = violations.rolling(window=2, on="InspectionDate")
# wind.mean().plot(kind="line", x="InspectionDate", y="score", use_index=False)
# markers =
# url = f"https://maps.googleapis.com/maps/api/staticmap?center=LOUISVILLE,KY&format=png32&zoom=12&size=800x800&maptype=roadmap&key={api_key}&signature={signature}"
# data = requests.get(url)
# with open("map.png", "wb+") as f:
#     f.write(data.content)
