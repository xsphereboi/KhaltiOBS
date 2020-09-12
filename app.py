from flask import Flask,render_template
import threading
from flask_socketio import SocketIO, send,emit
import khalti
import time
app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins='*')


# @socketio.on('message')
# def handleMessage(msg):
#     while True:
#         try:
#             time.sleep(10)
#             with open('recent_donators.txt','r')as f:
#                 prev = f.readline()
#             data = esewacookies.get_recent_donation()
#             if prev == data:
#                 print('No New Donators')
#             else:
#                 send(data, broadcast=True)
#                 with open('recent_donators.txt','w')as f:
#                     f.write(data)
#         except Exception:
#             send('Failed to grab recent donators', broadcast=True)
# @socketio.on('message')
# def handleMessage(msg):
#     while True:
#         try:
#             time.sleep(10)
#             with open('recent_donators.txt','r')as f:
#                 prev = f.readline()
#             data = khalti.very_latest_transaction()
#             if data['sender'] in prev:
#                 print('No New Donators')
#             else:
#                 send(data, broadcast=True)
#                 with open('recent_donators.txt','w')as f:
#                     st = f"{data['amount']}#|{data['sender']}#|{data['remarks']}"
#                     f.write(st)
#         except Exception as e:
#             print(e)
@socketio.on('message')
def handleMessage(msg):
    while True:
        
        time.sleep(30)
        with open('recent_donators.txt','r')as f:
            prev = f.readline()
        data = khalti.very_latest_transaction()
        print(data)
        if data['remarks'] in prev:
            print('No New Donators')
        else:
            send(data, broadcast=True)
            with open('recent_donators.txt','w')as f:
                st = f"{data['amount']}#|{data['sender']}#|{data['remarks']}"
                f.write(st)
        
if __name__ == "__main__":
    print('Server Started : ')
    socketio.run(app)