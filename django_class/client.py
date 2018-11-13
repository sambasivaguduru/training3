import requests
resp = requests.post("http://127.0.0.1:8000/service/", 
	data={"name": "test vol1","size":"20M","aggregate":"ag1"})
print resp.json(), resp.status_code
resp = requests.get("http://127.0.0.1:8000/service/")
print resp.json(), resp.status_code
resp = requests.put("http://127.0.0.1:8000/service/")
print resp.json(), resp.status_code
resp = requests.delete("http://127.0.0.1:8000/service/")
print resp.json(), resp.status_code