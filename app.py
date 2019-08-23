import requests
import config
import pandas as pd
import numpy as np

url = "https://api.foursquare.com/v2/venues/search"
params = dict(
    client_id="FRVVP3N4MQV5HSDK0UOROBBSP0X305H0FTFNO2GRUOXG53DV",
    client_secret=config.secret_code,
    near='luxembourg',
    limit=100,
    v="20180323"  # version of the API
)
headers = {
    "Authorization": "Bearer " + params["client_secret"]
}

response = requests.get(url=url, params=params)
# print(response) gives the status

venues = response.json()["response"]["venues"]
# venues = response.json()["venues"]
# print(venues)
name = []
category = []
address = []
neighborhood = []
for venue in venues:
    name.append(venue["name"])
    if venue["categories"]:  # if not empty
        category.append(venue["categories"][0].get("shortName"))
    else:
        category.append(None)
    address.append(venue["location"].get("address"))
    neighborhood.append(venue["location"].get("neighborhood"))
result = {
    "name": name,
    "category": category,
    "address": address,
    "neighborhood": neighborhood
}

df = pd.DataFrame(result)
print(df)
