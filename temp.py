import urllib.request
from json import loads

# domain = 'robynveitch.com'
domain = 'www.google.com'

with urllib.request.urlopen(f'https://www.ionos.com/api/ssl-checker?domain={domain}') as response:
	assert response.status == 200
	json_res = loads(response.read().decode('utf-8'))
	