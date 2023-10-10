import requests

url = "https://192.168.56.101/v1/projects"


payload={}
headers = {
  'Authorization': 'Bearer itwmjjgGMu8TU6yd5INgP1J1c2Y7YUi8vKcIsLSX1IdrP6AJUcrRpWja_0Zfp9X_nrQSLjWkhBgbjt9xYABXEJK0-z2jQFadInuTkXzIkcw47eulOerUNKZ0-puQhPPJvzo', 
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)