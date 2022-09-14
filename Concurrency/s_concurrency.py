import requests
import json
import time

INPUT_FILE = 'values.json'
ADDRESS = 'http://localhost:8080/'

values = []
data = []
output = {}
with open(INPUT_FILE) as f:
    values = json.load(f)

start_time = time.time()

s = requests.Session()
for start, end in values:
    url = ADDRESS + '?start=%s&end=%s' % (start, end)
    resp = s.get(url)
    r = resp.json()
    data.append(r)
s.close()

output['time'] = time.time() - start_time
output['name'] = 'synchronous'
output['data'] = data


with open("output.json", "r") as f:
    if f.read():
        with open("output.json", "r") as f:
            data = json.load(f)
        data.append(output)
        with open("output.json", "w") as f:
            json.dump(data, f)
    else:
        with open("output.json", "w") as f:
            json.dump([output], f)