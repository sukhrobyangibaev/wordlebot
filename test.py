import requests

response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/asshole')
res_json = response.json()
print(res_json)
if type(res_json) is list:
    word = res_json[0]['word']
    meanings = res_json[0]['meanings']
    definitions = []
    for meaning in meanings:
        for definition in meaning['definitions']:
            definitions.append(definition['definition'])
    print(definitions)
    # definitions.append(meaning['definitions'])
    # definitions = res_json[0]['meanings'][0]['definitions']
    # for definition in definitions:
    #     print(definition['definition'])
