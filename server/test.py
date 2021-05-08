import requests

query = {
    'oauth_token': '356875925d370ab7a4dc5512f04b10ba',
    'oauth_verifier': 'b4508bbfbddeb275d6c111bd00b4ece4',
    
}

response = requests.post(
    url = 'http://84.252.140.135:9090',
    data = query
)

print(response)