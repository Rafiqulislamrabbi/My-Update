import json, operator

s = '''\
[
  {"CarValue": "59", "ID": "100043"},
  {"CarValue": "59", "ID": "100013"}
]
'''

data = json.loads(s)
data.sort(key=operator.itemgetter('ID'))
print(json.dumps(data, indent=2))