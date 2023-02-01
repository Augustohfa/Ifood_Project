import requests

# Define the endpoint for retrieving orders
endpoint = "https://merchant-api.ifood.com.br/shipping/v1.0/merchants/507fb019-2d3f-424d-9959-8f08eed42936/orders"

# Define the API Key for authentication
api_key = "1eb25468-6841-45ac-ad57-5e97aeaf3c83"

# Make the GET request to the endpoint
response = requests.get(endpoint, headers={'Authorization': api_key})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    orders = response.json()
    
    # Print the list of orders
    print(orders)
else:
    # Handle error cases
    print("Error retrieving orders:", response.text)
