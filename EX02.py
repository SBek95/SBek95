import socket
import sqlite3

#Попытка подключения и создание базы данных для сохранения входящих сообщений.
try:
    conn = sqlite3.connect('EXO.sqlite')
    cursor = conn.cursor()
    print("Успешно открыта база данных")
except sqlite3.Error as err:
    print('Ошибка: ' + err.args[0])
finally:
    conn.close()
    print("Закрыта база данных")
# ФУНКЦИЯ ТАБЛИЫ БАЗЫ ДАННЫХ - "КОМАНДЫ"
def f1():
     conn = sqlite3.connect('EXO.sqlite')
     cursor = conn.cursor()
     cursor.execute('''  CREATE TABLE EXO_DATA(
                    COMAND           TEXT    NOT NULL);''')
     cursor.close()
# СОХРАНЕНИЕ БАЗЫ ДАННЫХ
def f2():
     conn = sqlite3.connect('EXO.sqlite')
     cursor = conn.cursor()
     comand = "'" + sms + "'"
     q = "INSERT INTO EXO_DATA (COMAND) VALUES (" + comand +")"
     print(q)
     cursor.execute(q)
     conn.commit()
     conn.close()
# ПОДКЛЮЧЕНИЕ К КЛИЕНТУ
class communication:
  def __init__(self):
    try:
      host = '127.0.0.1'
      self.Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.Server.bind((host,12347))
      self.Server.listen(1)
    finally:
      print("установка завершена")
  def recieve(self):
    (connection, client_address) = self.Server.accept()
    data = connection.recv(128)
    return data
  def close(self):
    self.server.close()
if __name__ == "__main__":
    exp = communication()
    while True:
        try:
            (connection,client_address) = exp.Server.accept()
            message = connection.recv(128)
            sms = message.decode('utf-8')
            f2()
        finally:
            print(sms)
        if message == 'Отключение от сервера ':
          exp.close()