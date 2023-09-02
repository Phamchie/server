import requests
import socket

class server:
  host = "https://www.tiktok.com/"

class pwd:
  password = "th1s1sclone07"

def listen():
  address = socket.gethostbyname(server.host)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((address, 443))
  while True:
    data_result = s.recv(1024)
    def log():
      data = {
        "username": data_result,
        "password": pwd.password
      }
      log = requests.post(server.host + data=data)
    log()
listen()
