import requests
import json

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}\n')

# Convert JSON to python dictionary and store API response in a variable
source = r.text
data = json.loads(source)
print(json.dumps(data, indent=2))


