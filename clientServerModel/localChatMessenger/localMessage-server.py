from faker import Faker
import os
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

address = '/local_talk_file'

try:
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)
sock.listen(1)

print('start chat bot')

while True:
    connection  = sock.accept()
    try:
        print('connect from {}'.format(address))
        fake = Faker('ja-JP')
        while True:
            answer = connection[0].recv(32)
            answer_str = answer.decode('utf-8')
            print('client message is {}'.format(answer_str))
            if answer:
                if answer_str == 'job':
                    result = str(fake.job())
                    connection[0].sendall(result.encode())
                elif answer_str == 'name':
                    result = str(fake.name())
                    connection[0].sendall(result.encode())
                elif answer_str == 'address':
                    result = str(fake.address())
                    connection[0].sendall(result.encode())
            else:
                print('no data from {}'.format(connection[0].getsockname()))
                break
    finally:    
        print('connection close : {}'.format(connection[0].getsockname()))
        connection[0].close()
