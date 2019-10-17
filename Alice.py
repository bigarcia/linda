import requests

data1={
	'tuple':"'Alice','gtcn','This graph theory stuff is not easy???'"
	}
data2={
	'tuple':"'Alice','distsys','I like systems more than graphs'"
}

response1 = requests.post('http://localhost:5000/blog', data1)
response2= requests.post('http://localhost:5000/blog', data2)
print("Sending messages\n")
print(response1.json()['response']['publisher']+" Said: "+response1.json()['response']['message']+" on topic "+response1.json()['response']['topic'])
print(response2.json()['response']['publisher']+" Said: "+response2.json()['response']['message']+" on topic "+response2.json()['response']['topic'])
