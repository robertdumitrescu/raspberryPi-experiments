import requests

# Create a dictionary to be sent.
json_data = {'lightElectricalQuantity': 333}

# Send the data.
response = requests.post(url='http://46.101.225.81:5555/api/measurements', json=json_data)
print("Server responded with %s" % response.text)