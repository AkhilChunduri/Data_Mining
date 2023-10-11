import requests

# Replace these with your actual credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Step 2: Generate an Access Token
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
token_payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

response = requests.post(token_url, data=token_payload)
access_token = response.json().get('access_token')

# Step 3: Make API Requests
if access_token:
    api_url = 'https://api.linkedin.com/v2/me'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        linkedin_data = response.json()
        print(linkedin_data)
    else:
        print(f"Error accessing LinkedIn API: {response.status_code}")
else:
    print("Failed to obtain access token")
