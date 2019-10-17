import requests
import json

t1 = requests.get("http://localhost:5000/blog?publisher='Bob'&topic='distsys'")
t2 = requests.get("http://localhost:5000/blog?publisher='Alice'&topic='gtcn'")
t3 = requests.get("http://localhost:5000/blog?publisher='Bob'&topic='gtcn'")
print("Reading from blog\n")

print("Get all messages from Bob on topic distsys:")
for resp1 in t1.json()['response']:
    print("Reading message "+resp1[2]+" sent by "+resp1[0]+" on topic "+resp1[1])
print("Get all messages from Alice on topic gtcn:")
for resp2 in t2.json()['response']:
    print("Reading message "+resp2[2]+" sent by "+resp2[0]+" on topic "+resp2[1])
print("Get all messages from Bob on topic gtcn:")
for resp3 in t3.json()['response']:
    print("Reading message "+resp3[2]+" sent by "+resp3[0]+" on topic "+resp3[1])