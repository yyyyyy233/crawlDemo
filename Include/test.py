import json
dictstr = '{"a":"b"}'
d = json.loads(dictstr)
print(d['a'])