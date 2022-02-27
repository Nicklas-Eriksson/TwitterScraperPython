import socket
import pickle
from dotenv import load_dotenv
import os

load_dotenv()
Host = os.getenv("Host")
Port = os.getenv("Port")

HEADERSIZE = 10

def StartClient(userSearch, selectSearch, numberOfTweets):
    s = socket.socket()
    s.connect((Host, int(Port)))
    msg = s.recv(1024)
    print(msg)

    inputTuple = (userSearch, selectSearch, numberOfTweets)
    compressedMsg = pickle.dumps(inputTuple)
    msg = bytes(f'{len(compressedMsg):<{HEADERSIZE}}' , "utf-8") + compressedMsg
    s.send(msg)
    s.close