import requests

url = "https://images.unsplash.com/photo-1510337550647-e84f83e341ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1031&q=80"

response = requests.get(url)
with open("perritos.jpg","wb") as f:
    f.write(response.content)
    pass