from random import randrange as rn
import random as rm
from time import sleep as sl
import time as tm

class Var:
    rnctp = rn(1, 1000000)
    p1 = "Welcome to the number guessing game"
    p2 = "How to play?"
    p3 = "First the program will choose a number between 1 and 1000000 and you have to guess what is the number."
    ip1 = "Choose your number"
    si1 = 0
    p4 = "You guessed the number !!!"
    p5 = "The number you choosed was wrong retry :/"
    t = 0
    p6 = "It took you "
    p7 = " tries to guess the number"


def introduction():
    print(Var.p1)
    sl(2.5)
    print(Var.p2)
    sl(2.5)
    print(Var.p3)
    Var.si1 = 1


def cheking():
    PI = input(Var.ip1)
    pi_i = int(PI)
    while Var.si1 == 1:
        if pi_i == Var.rnctp:
            print(Var.p4)
            Var.si1 = 0
            ts = str(Var.t)
            print(Var.p6 + ts + Var.p7)

        else:
            print(Var.p5)
            Var.t = Var.t + 1


def everythingtoghether():
    introduction()
    cheking()

ETT = everythingtoghether()

ETT