'''
json 형식
{User:[{},{},{}]}
'''
import json
import csv

with open("local_users.json", "r", encoding="utf8") as f:
    contents = f.read()  # string 타입
    json_data = json.loads(contents)

Name = list(Name["Name"] for Name in json_data["Users"])
list.sort(Name)
Name2 = []
for i in Name:
    Name2.append([i])
print(Name)
print(Name2)

with open('Name.csv', 'w', newline='\n') as f:
    write = csv.writer(f)
    write.writerows(Name2)
  