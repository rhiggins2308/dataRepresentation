# https://requests.kennethreitz.org/en/master/users/quickstart/
import requests

# ------ GET --------
url1 = 'https://www.gmit.ie'
response1 = requests.get(url1)
print(response1.status_code)
print(response1.text)
print(response1.headers)

# response1.json
# response1.content
# response1.data


# ------ PUT --------
url2 = 'http://127.0.0.1:5000/cars'
data = {
    'reg':'12 G 1234',
    'make':'Hyundai',
    'model':'i40',
    'price': 19000
}

response2 = requests.post(url2, json=data)
print(response2.status_code)
print(response2.json())