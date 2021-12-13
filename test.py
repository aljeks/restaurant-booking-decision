
import requests

url = "http://localhost:9696/predict"

rest = {'restaurant_name': 'via_delhi',
 'country_code': 214,
 'city': 'abu_dhabi',
 'longitude': 54.374273233100006,
 'latitude': 24.4910933909,
 'cuisines': 'indian,north_indian,chinese',
 'average_cost_for_two': 100,
 'currency': 'emirati_diram(aed)',
 'has_table_booking': 0,
 'has_online_delivery': 1,
 'is_delivering_now': 1,
 'price_range': 3,
 'votes': 1148}
 
respose = requests.post(url, json=rest).json()
print("AWS recommendation to book this restaurant or not (1-yes, 0-no): ")
print(respose)

