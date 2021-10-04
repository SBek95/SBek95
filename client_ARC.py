import socket
import time
import random
comands = ["Сердцебиение в норме ",
           "Заряд аккумулятора ниже 75% ",
           "Приводы активны ",
           "Режим бега ",
           "Система охлаждения включена ",
           "Автономная подзарядка включена ",
           "ускорители включены ",
           "Достигнут предел грузоподъемности ",
           "Заряд аккумулятора ниже 50% ",
           "Подзарядка началась ",
           "Подключение к серверу стабильно ",
           "Оболочка брони не повреждена ",
           "HUD активирован ",
           "Каркас деформирован на 15% ",
           "Нейросинхронизация на 76% ",
           "Костюм отключается от сервера "]
sock = socket.socket()
sock.connect(('localhost', 9090))
com = random.choice(comands)
#messege = input("команды в базу=")
sock.send(com.encode())
#sock.send(messege,encode())

data = sock.recv(102300)
dat2 = data.decode("utf-8")
#//////////////////////////////
if dat2 == 'Next':
  com = random.choice(comands)
  sock.send(com.encode())
  print(dat2)
if not data:
  print("NO DATA")
sock.close()