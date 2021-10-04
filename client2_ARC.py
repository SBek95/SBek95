import socket
import time
from time import sleep

host = '127.0.0.1'
class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self):
        self.sock.connect((host,12347))
    def send(self,message):
            self.sock.sendall(message)
    def close(self):
        self.sock.close()
if __name__ == "__main__":
    message1 = "Связь к серверу успешна"
    message2 = "Уровень заряда батареи ниже 75%"
    message3 = "Приводы активны"
    message4 = "Оболочка брони не повреждена "
    message5 = "Дополненная реальность автивирована"
    message6 = "Связь не стабильна "
    message7 = "температура комфортная "
    message8 = "Влажность воздуха ниже 50%"
    message9 = "голосовое управление стабильно работает"
    message10 = "Нейросвязь стабильна "
    message11 = "Заряд батареи 50% "
    message12 = "Один привод барахлит "
    message13 = "Увеличение физической силы на 40% "
    message14 = "Переход на режим бега "
    message15 = "Обычный режим "
    message16 = "требуется подзарядка "
    message17 = "Сигнал с сервером сильный "
    message18 = "Амортизаторы разблокированы "
    message19 = "Вес пилота 78 кг "
    message20 = "Отключение от сервера "
    #exp = Client()
    #exp.connect()
    for i in range(0,20):
        try:
            exp = Client()
            exp.connect()
            if i == 0:
                txt = message1
                sleep(3)
                print("Задержка")
            elif i == 1:
                txt = message2
                sleep(4)
                print("Задержка2")
            elif i == 2:
                txt = message3
                sleep(3)
                print("Задержка3")
            elif i == 3:
                txt = message4
                sleep(2)
                print("Задержка4")
            elif i == 4:
                txt = message5
                sleep(3)
                print("Задержка5")
            elif i == 5:
                txt = message6
                sleep(5)
                print("Задержка6")
            elif i == 6:
                txt = message7
                sleep(3)
                print("Задержка7")
            elif i == 7:
                txt = message8
                sleep(4)
                print("Задержка8")
            elif i == 8:
                txt = message9
                sleep(2)
                print("Задержка9")
            elif i == 9:
                txt = message10
                sleep(3)
                print("Задержка10")
            elif i == 10:
                txt = message11
                sleep(3)
                print("Задержка11")
            elif i == 11:
                txt = message12
                sleep(3)
                print("Задержка12")
            elif i == 12:
                txt = message13
                sleep(4)
                print("Задержка13")
            elif i == 13:
                txt = message14
                sleep(5)
                print("Задержка14")
            elif i == 14:
                txt = message15
                sleep(4)
                print("Задержка15")
            elif i == 15:
                txt = message16
                sleep(3)
                print("Задержка16")
            elif i == 16:
                txt = message17
                sleep(4)
                print("Задержка17")
            elif i == 17:
                txt = message18
                sleep(5)
                print("Задержка18")
            elif i == 18:
                txt = message19
                sleep(3)
                print("Задержка19")
            elif i == 19:
                txt = message20
                sleep(6)
                print("Задержка20")
                exp.send(txt)
                exp.close()
            print(i)
            exp.send(txt.encode())
        except:
            pass