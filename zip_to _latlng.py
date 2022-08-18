"""
My first ever commercial use of python. I needed to convert a large number of zip codes into geographic coordinates for my current job and used an API provided by Google for this.
"""

import json
import requests


api_key = [YOUR GOOGLE API KEY]
file_zip = open('zip.txt', 'r') # txt file with zip codes to change (one zip code per line)
file_lat_lng = open('latLng.txt', 'w') # txt file for saving geographic coordinates
zip_list_clean =[]
country = 'pl' # all my zip codes were in Poland (that's why 'pl'), but here you can specify the country that will be provided in the API request

zip_list = file_zip.readlines()

for zip_code in zip_list:
  zip_list_clean.append(zip_code.strip())

for zip_code in zip_list_clean:
  response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:{}|country:{}&key={}".format(zip_code, country, api_key))
  
  json_dictionary = json.loads(response.content)

  if json_dictionary['status'] != 'ZERO_RESULTS':
    
    # getting lat and lng from json from results -> gemoetry -> location

    lat = json_dictionary['results'][0]['geometry']['location']['lat']
    lng = json_dictionary['results'][0]['geometry']['location']['lng']

    file_lat_lng.write('{}, {}\n'.format(lat, lng))

file_zip.close()
file_lat_lng.close()