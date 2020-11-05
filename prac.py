import json

example = {
    'KJB' : 'king',
    'Kang' : 'slave'
}

print(type(example))
ex = json.JSONEncoder(example)
print(type(ex))