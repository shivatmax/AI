
import requests
import json

# Authorization token that must have been created previously. 
# See : https://developer.spotify.com/documentation/web-api/concepts/authorization
token = 'BQCR0jNfwhOyZsG39ypRYNn_3-2kp_hJ5hR48XTCxzSOYMFF4ncUKpFxplQEl77wzrKbY68VHAD-SEv1NkWR97tRrBgRqBOWnEoI7ikQDxdlHDzrNWg'

def request_spotify_api(endpoint, method, body=None):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://api.spotify.com/{endpoint}'
    
    if method == 'GET':
        resp = requests.get(url, headers=headers)
    elif method == 'POST':
        resp = requests.post(url, headers=headers, data=json.dumps(body))
    else:
        raise ValueError(f'HTTP method {method} not supported')
    
    return resp.json()

def get_top_tracks():
    # Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    api_resp = request_spotify_api(
        'v1/me/top/tracks?time_range=short_term&limit=5', 'GET'
    )
    return api_resp['items']

top_tracks = get_top_tracks()

for track in top_tracks:
    print(f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
