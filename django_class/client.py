import requests
# resp = requests.post("http://127.0.0.1:8000/clusters/",
#                      data={"name": "cluster12", "ip": "192.168.0.1",
#                            "username": "ag1", "password": "pwd1"})
# print resp.json(), resp.status_code
# resp = requests.get("http://127.0.0.1:8000/clusters/")
# print resp.json(), resp.status_code

# print "*"*20
# resp = requests.get("http://127.0.0.1:8000/clusters/12")
# print resp.json(), resp.status_code

# resp = requests.put("http://127.0.0.1:8000/service/")
# print resp.json(), resp.status_code
# resp = requests.delete("http://127.0.0.1:8000/service/")
# print resp.json(), resp.status_code
resp = requests.delete("http://127.0.0.1:8000/clusters/12")
print resp.json(), resp.status_code