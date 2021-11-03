from ping3 import ping
import socket

def pingar(ip):
    ms = int(ping(ip, unit="ms"))
    return ms

def minecraft():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      s.connect(('127.0.0.1', 25565))
      s.shutdown(1)
      s.close()
      return True
    except:
      s.close()
      return False

def terraria():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      s.connect(('127.0.0.1', 7777))
      s.shutdown(1)
      s.close()
      return True
    except:
      s.close()
      return False

def minecraftmods():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      s.connect(('127.0.0.1', 25465))
      s.shutdown(1)
      s.close()
      return True
    except:
      s.close()
      return False
