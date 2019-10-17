import requests
import json

#t1 = requests.delete("http://localhost:5000/blog?publisher='Bob'&topic='distsys'&message='I am studying chap 2'")
t2 = requests.delete("http://localhost:5000/blog?publisher='Alice'&topic='gtcn'&message='This graph theory stuff is not easy???'")

print("Deleting from blog\n")

print("Deleting message "+t2.json()['response'][0]+" sent by "+t2.json()['response'][1]+" on topic "+t2.json()['response'][2])

# for resp2 in t2.json()['response']:
#     print("Deleting message "+resp2[2]+" sent by "+resp2[0]+" on topic "+resp2[1])

