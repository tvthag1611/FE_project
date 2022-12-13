import requests
 
r = requests.post('http://127.0.0.1:8000/v2/api/staff/', 
data = {
    "username": "linhnt",
    "password": "123",
    "name": "Linh",
    "age": 18,
    "phone": "0333855577",
    "email": "linhnt.ptit@gmail.com",
    "department": "Mobile",
    "role": "Dev",
    "face_registered": False,
    "face_embed": None
}
)
print(r)
print(r.content)