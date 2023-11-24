import requests,json 

def postdata(dataM):
    url = "http://localhost:5000"
    data = {"key":f"{dataM}"}
    json_data = json.dumps(data)
    headers = {"Content-Type":"application/json"}
    response = requests.post(url,data=json_data,headers=headers)
    print(response.text)
    
