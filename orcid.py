import requests

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

# Example usage
access_token = 'YOUR_ACCESS_TOKEN_HERE'
emails = ['laalnaji@uhb.edu.sa']
for email in emails:
    print(f"Email: {email}, ORCID: {get_orcid_by_email(email, access_token)}")
