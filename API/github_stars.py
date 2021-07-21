import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}\n')

# Convert JSON to python dictionary and store API response in a variable
response_dicts = r.json()

# print(response_dicts['incomplete_results'])

# Process results.
# print(response_dict.keys())
# print(response_dict['items'][0]['html_url'])
repo_dirs = response_dicts['items']

print(repo_dirs[1]['html_url'])


