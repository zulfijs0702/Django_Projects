import requests as req
url="https://dog.ceo/api/breeds/image/random"
res=req.get(url) 
if res.status_code==200:
    breed=res.json()
    print("Available breeds: ", breed['message'])
else:
    print("Error in fetching data")