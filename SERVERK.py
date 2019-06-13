from OpenSSL import SSL
import socket
info = 0
def startServer():
    HOST = (socket.gethostbyname(socket.gethostname()),50001)
    print("Server ip: " + HOST[0])
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.use_certificate_file('certificate.crt')
    context.use_privatekey_file('privateKey.key')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    connection = SSL.Connection(context,s)
    connection.bind(HOST)
    connection.listen(2)
    print("Esperando conexiones...")
    while True:
        conn, addr = connection.accept()
        print("Cliente: "+ str(addr[0]) + " conectado")      
        data = conn.recv(4096)
        saveFilebyAdress(addr[0],data.decode('utf-8'))
        conn.shutdown()

def saveFilebyAdress(addr,message):
    global info
    fileName = addr + 'info.txt'
    f= open(fileName,"w+")
    f.write(message)
    print("Info added " + str(info) + " times")
    info = info + 1
    f.close()

def main():
    startServer()



if __name__ == "__main__":
    main()