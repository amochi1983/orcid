import requests


def get_orcid_access_token(client_id, client_secret):
    """Get an ORCID access token using client credentials."""
    url = 'https://orcid.org/oauth/token'
    headers = {'Accept': 'application/json'}
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
        'scope': '/read-public'
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None

# Usage
client_id = 'APP-F2JUGND5DSO48ISW'
client_secret = '237b6430-23a2-4bcc-9515-611f4c10a3e4'
token = get_orcid_access_token(client_id, client_secret)
print("Access Token:", token)

def get_orcid_by_email(email, access_token):
    """Search for an ORCID iD by email."""
    url = f"https://pub.orcid.org/v3.0/search?q=email:{email}"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['result']:
            return data['result'][0]['orcid-identifier']['path']
        else:
            return "No ORCID found"
    else:
        return "Failed to retrieve data"

def get_orcid_by_name(name, access_token):
    """Search for an ORCID iD by name."""
    url = f"https://pub.orcid.org/v3.0/search?q={name}"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['num-found'] > 0:
            # Returning the first match's ORCID iD
            return data['result'][0]['orcid-identifier']['path']
        else:
            return "No ORCID found"
    else:
        return "Failed to retrieve data"


# Example usage
access_token = token
emails = ['amochi@uhb.edu.sa']
for email in emails:
    print(f"Email: {email}, ORCID: {get_orcid_by_email(email, access_token)}")

# Use the function by replacing 'name' with the actual name of the person
namea="Aymen Ochi"
orcid_id = get_orcid_by_name(namea, token)
print(f"Name: {namea}, ORCID: {orcid_id}")