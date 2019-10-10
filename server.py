import json
import asyncio
import socket


from sys import exit
from collections import deque

tuples = {}


class Server(asyncio.Protocol):
    def connection(self, trans):
        self._trans = trans
        self._buffer = bytes()
        self._expec_size = -1

    def lostConnection(self, exec):
        if not exec:
            print('A conexão foi encerrada')
        else:
            print('Erro: ' + repr(exec))

    def received(self, data):
        while len(data) > 0:
            if self._expec_size < 0:
                if len(data.split(b':', 1)) == 2:
                    size, data = data.split(b':', 1)
                    try:
                        self._expec_size = int(size)
                    except ValueError:
                        self._trans.close()
            self._buffer = data[:self._expec_size]
            if self._expec_size > 0 and len(data) >= self._expec_size:
                data = data[self._expec_size:]
                self._expec_size = -1

		message_json = {'op': "", 'sender': "", 'topic': "", 'msg': ""}
		try:
		   message_json = json.loads(self._buffer.decode('utf-8'))
		   except Exception as e:
			print("Erro: ", e)
		  

                self._call(message_json)
                self._buffer = bytes()

    def _call(self, message):
        if message['op'] == 'out':
            self._op_out(message)
        elif message['op'] == 'rd':
            self._op_rd(message)
        elif message['op'] == 'in':
            self._op_in(message)

    def _op_out(self, message):
        sender = message['sender']
        subject = message['subject']
        content = message['msg']

        subject_tuple = self._getSubject(sender, subject)
        subject_tuple['messages'].append(content)
        self._waitIteration(subject_tuple)

    def _op_rd(self, message):
        sender = message['sender']
        subject = message['subject']

        subject_tuple = self._getSubject(sender, subject)
        self._regConnection(subject_tuple, message)
        self._waitIteration(subject_tuple)

    def _op_in(self, message):
        sender = message['sender']
        subject = message['subject']
        subject_tuple = self._getSubject(sender, subject)
        self._regConnection(subject_tuple, message)
        self._waitIteration(subject_tuple)

    def _getSubject(self, sender, subject):

        global tuples
        sender_tuple = tuples.get(sender)
        
        if not sender_tuple:
            sender_tuple = tuples[sender] = {}

        subject_tuple = sender_tuple.get(subject)
        if not subject_tuple:
            subject_tuple = sender_tuple[subject] = {'messages': deque(), 'subscribers': deque()}

        return subject_tuple

    def _regConnection(self, subject_tuple, message):
        subject_tuple['subscribers'].append((message, self._trans))

    def _waitIteration(self, subject_tuple):
        messages = subject_tuple['messages']
        subscribers = subject_tuple['subscribers']

        while len(messages) > 0 and len(subscribers) > 0:
            message, conn = subscribers.popleft()
            message['msg'] = messages[0]
	    
            message_json = json.dumps(message)
            message_final = f'{len(message_json)}:{message_json}'
            conn.write(message_final.encode('utf-8'))

            if message['op'] == 'in':
                messages.popleft()


async def createServer(host=localhost,port=15555):
    try:
        loop = asyncio.get_running_loop()
        print(f'Iniciando servidor socket no host:{host} e porta:{port}')
        server = await loop.createServer(lambda: Server(), host, port)
    
        async with server:
            await server.serve_forever()
    
    except RuntimeError as error:
        print('Erro: ' + error)
