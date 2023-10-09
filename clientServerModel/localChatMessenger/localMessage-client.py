import socket
import sys

sock = socket.socket(socket.AF_UNIX , socket.SOCK_STREAM)
address= '/local_talk_file'

print('connecting {}'.format(address))

try:
    sock.connect(address)
except socket.err() as err:
    print(err)
    sys.exit(1)
    
try:
    message = input('Please enter "job", "name" or "address"') 
    sock.sendall(message.encode('utf-8'))
    
    sock.settimeout(3)
    
    try:
        while True:
            result = sock.recv(32).decode('utf-8')
            if result:
                print('server response : ' + result)
            else:
                break
    except(TimeoutError):
        print('time out')

finally:
    print('socket close')
sock.close()            
