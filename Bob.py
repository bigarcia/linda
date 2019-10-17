import requests

data1={
	'tuple':"'Bob','distsys','I am studying chap 2'"
	}
data2={
    'tuple':"'Bob','distsys','The linda example's pretty simple'"
}
data3={
    'tuple':"'Bob','gtcn','Cool book!'"
}


response1 = requests.post('http://localhost:5000/blog', data1)
response2= requests.post('http://localhost:5000/blog', data2)
response3 = requests.post('http://localhost:5000/blog', data3)
print("Sending messages\n")
print(response1.json()['response']['publisher']+" Said: "+response1.json()['response']['message']+" on topic "+response1.json()['response']['topic'])
print(response2.json()['response']['publisher']+" Said: "+response2.json()['response']['message']+" on topic "+response2.json()['response']['topic'])
print(response3.json()['response']['publisher']+" Said: "+response3.json()['response']['message']+" on topic "+response3.json()['response']['topic'])
