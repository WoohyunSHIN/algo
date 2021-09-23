import json

user = {
    "id" : "gildong",
    "password" :  "123456",
    "age" : 30,
    "hobby" : ["football","programming"]
}

# json 인코딩
json_data = json.dumps(user, indent = 4)
print(json_data)

# json 디코딩
decoding_data = json.loads(json_data)
print(decoding_data)

# 파일 생성
with open("user.json","w",encoding="utf-8") as file:
    json.dump(user, file, indent=4)