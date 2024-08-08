

from random import randint
from passlib.hash import pbkdf2_sha256 as crypt


class Car:
    status_car = False

    @staticmethod
    def serial():
        return 'XRRR02'

    def __init__(self, marc, model, color):
        self.marc = marc
        self.model = model
        self.color = color
        self.__ligado = False
        self.passwd = randint(0, 9999)
        print(f'New car {self.marc} {self.model} {self.color}\nYor key to turn on the Car is : {self.passwd}')

    def check_passwd(self):
        temp = int(input("Enter your password: "))
        if temp == self.passwd:
            return print('Lest Go')
        else:
            return print('Incorrect Password')


while True:
    usr_mar = input('Whats the marca of the car:')
    usr_model = input('Whats the model of the car:')
    usr_color = input('Whats the color of the car:')
    car = Car(usr_mar, usr_model, usr_color)
    temp = int(input('Enter 1 to turn-on the car, 2 for continue or 0 for exit: '))
    if temp == 1:
        car.check_passwd()








