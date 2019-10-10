import asyncio
import socket
import json


class Client():
    def __init__(self, host='localhost', port=15555):
        self._reader = None
        self._writer = None
        self.host = host
        self.port = port

    async def connect(self):
        self._reader, self._writer = await asyncio.open_connection(self.host, self.port)

    async def close(self):
        self._writer.close()
        await self._writer.wait_closed()

    async def _recvall(self):
        buffer = b''
        size = -1

        while True:
            data = await self._reader.read(1024)
            try:
                if len(data.split(b':', 1)) == 2:
                    size, data = data.split(b':', 1)
                    size = int(size)

                else:
                    buffer += data
                    data = b''

            except Exception as e:
                print('Erro: ' + e)
            
            if size > 0 and len(data) >= size:
                return data

    def _out(self, data):

	message_json = json.dumps({'op': 'out', 'sender': data[0], 'topic': data[1], 'msg': data[2]})
   	message = f'{len(message_json)}:{message_json}'
        self._writer.write(message.encode('utf-8'))
   
    async def _rd(self, data):
	
	message_json = json.dumps({'op': 'rd', 'sender': data[0], 'topic': data[1]})
   	message = f'{len(message_json)}:{message_json}'
        self._writer.write(message.encode('utf-8'))
        
        response = await self._recvall()
	
	json = {'op': "", 'sender': "", 'topic': "", 'msg': ""}
    	try:
        	json = json.loads(response)
    	except Exception as e:
        	print("Error: ", e)

        return self._cast(data[2], json)

    async def _in(self, data):

	message_json = json.dumps({'op': 'in', 'sender': data[0], 'topic': data[1]})
    	message = f'{len(message_json)}:{message_json}'

        self._writer.write(message.encode('utf-8'))
        
	json = {'op': "", 'sender': "", 'topic': "", 'msg': ""}
   	try:
        	json = json.loads(await self._recvall())
    	except Exception as e:
        	print("Erro: ", e)
    	return 

        return self._cast(data[2], json)

    def _cast(self, cast, msg):
        if type(cast) is type:
            return cast(msg)
        else:
            return msg

