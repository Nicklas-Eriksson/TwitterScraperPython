import socket 
import pickle
from itsdangerous import TimedJSONWebSignatureSerializer
import twitterScraper as scrapeData
import tweetResults

HEADERSIZE = 10 # Used for prepare that reciving system on the size of the file transfer.

#Starts the server, it will allways listen for connections.
def StartServer():
    serverSocket = socket.socket()
    print("Socket created")
    host = socket.gethostname()
    print("Host name:", host)
    port = 1234
    serverSocket.bind((host,port))

    while True:
        print("Listening for connection...")
        serverSocket.listen(10) #queue size 10

        clientSocket, address = serverSocket.accept()
        print("Connection recived from", address)

        msg = clientSocket.recv(1024)
        print("Message recived!")

        print("Decoding message...")
        decodedCompressedMsg = pickle.loads(msg)

        if decodedCompressedMsg != None:
            orders = decodedCompressedMsg[0]
        print("Message decoded!")
        
        print("Booting bot...")
        if orders == 'BirdBot2022':
            Tweet(clientSocket, decodedCompressedMsg)
        else:
            Scrape(clientSocket, decodedCompressedMsg)

def Scrape(clientSocket, decodedCompressedMsg):
    print("Scraping initiated...")
    data = scrapeData.Run(decodedCompressedMsg[0], decodedCompressedMsg[1], decodedCompressedMsg[2])
    print("Twitter data collected!")
    # CompressAndSend(clientSocket, data)
    print("Compressing inputs...")
    compressedMsg = pickle.dumps(data)
    print("Compression done!")

    msg = bytes(f'{len(compressedMsg):<{HEADERSIZE}}', "utf-8") + compressedMsg

    print("Sending data...")
    clientSocket.send(msg)
    print("Data transmitted!")

    print("Terminating connection to client...")
    clientSocket.close()
    print("Connection terminated!")

def Tweet(clientSocket, decodedCompressedMsg):
    res = tweetResults.Run(decodedCompressedMsg[1])
    print(res)
    # CompressAndSend(clientSocket, res)
    print("Compressing inputs...")
    compressedMsg = pickle.dumps(res)
    print("Compression done!")

    msg = bytes(f'{len(compressedMsg):<{HEADERSIZE}}', "utf-8") + compressedMsg

    print("Sending data...")
    clientSocket.send(msg)
    print("Data transmitted!")

    print("Terminating connection to client...")
    clientSocket.close()
    print("Connection terminated!")

def CompressAndSend(clientSocket, data):
    print("Compressing inputs...")
    compressedMsg = pickle.dumps(data)
    print("Compression done!")

    msg = bytes(f'{len(compressedMsg):<{HEADERSIZE}}', "utf-8") + compressedMsg

    print("Sending data...")
    clientSocket.send(msg)
    print("Data transmitted!")

    print("Terminating connection to client...")
    clientSocket.close()
    print("Connection terminated!")