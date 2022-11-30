import json


person_string = '{"name":"Ali", "languages":["python","C#"]}'
person_dict = {"name": "Ali","languages": ["Python","C#"]}
# **JSON string to Dict***
# result = json.loads(person_string) # dictionary ye çevirir
# result = result["name"]
# result = result["languages"]



""" json ı dict yapısına çevirdi"""
# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])



""" dict yapıyı json a çevirdi"""
# result = json.dumps(person_dict)


"""json dosyasına  yazma işlemi"""
# with open("person.json","w") as f:
#     json.dump(person_dict,f)


# person_dict = json.loads(person_string)
# result = json.dumps(person_dict,indent = 4)
# print(person_dict)
# print(result)