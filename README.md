# pythonKeyLogger
Simple implementarion for remote keyloggging in python :)

## Getting Started

For testing you have to provide certificate and private key for TLS(Transfer layer security) in the same folder of server code named 'certificate.crt' and 'privateKey.key' , the program adds automatically to startup in windows(not detected so far) and send information every 200 keys pressed, server side save's the info in a text file.


### Prerequisites
```sh
$ pip install pynput

$ pip install pyopenssl

$ pip install pyinstaller
```

### Running the tests
```sh

$ pyinstaller --onefile client.py

$ pyinstaller --onefile server.py

```

### Built With
* pynput

* OpenSSL

### Authors
Sebastian Mahuzier.
