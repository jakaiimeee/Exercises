import json
def convert(dict):
    data=json.dumps(dict)
    return data
My_dict = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
               {"firstName": "Mervin", "lastName": "Friedland"},
               {"firstName": "Aron ", "lastName": "Wilkins"}],
"teachers":[{"firstName": "Amberly", "lastName": "Calico"},
         {"firstName": "Regine", "lastName": "Agtarap"}]}

result = convert(My_dict)
print(result)
print(type(result))

