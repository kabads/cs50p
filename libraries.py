import json

import requests
import statistics
import sys

print(statistics.mean([2, 5, 5, 1, 6, 9]))


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

print(json.dumps(response.json(), indent=2))
# print(response.json()['results'][0]['trackName'])

o = response.json()

for response in o['results']:
    print(response['trackName'])
