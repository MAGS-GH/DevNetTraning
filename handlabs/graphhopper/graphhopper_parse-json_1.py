import requests 
import urllib.parse 

geocode_url = "https://graphhopper.com/api/1/geocode?" 
route_url = "https://graphhopper.com/api/1/route?" 
loc1 = "Roma, Italia" 
loc2 = "Baltimore, Maryland" 
key = "724a46f5-7fa8-4dfc-9264-1d1ac6ad53b4"

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key}) 

replydata = requests.get(url) 
json_data = replydata.json() 
json_status = replydata.status_code 
print(json_data) 