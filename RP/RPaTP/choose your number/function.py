from variables import Variables as v
from time import sleep as s
from random import randrange as r


def start():
    print(v.note)
    s(3)
    print(v.User_input)

    if 1000 > v.User_int > 0:
        s(1)
        print(v.after)
        v.start_signal = 1
        v.error4040 = 1

    else:
        print(v.error)


def choose():
    if v.start_signal == 1:
        print(v.random_number_chooser)

        while v.start_signal == 1:
            v.random_number = r(1, v.random_number_chooser)
            v.counter = v.counter + 1
            v.counter_str = str(v.counter)
            if v.User_int == v.random_number:
                if v.load1 == 0:
                    print("Loading")
                    v.load1 = 1
                    v.load2 = 1

                if v.load2 == 1:
                    v.load_p = v.load_p + v.load_p_adder
                    v.load_pstr = str(v.load_p)
                    s(0.2)
                    print("%" + " " + v.load_pstr)

                    if v.load_p > 100:
                        print(v.done1)
                        v.start_signal = 0


def end():
    if v.error4040 == 1:
        s(3)
        print(v.end1)
        s(4)
        print("..." + v.counter_str + " tries")

    else:
        print(v.error404)


def lucky():
    print(v.counter)
    if v.lucky == 11:
        print(v.lucky_sms)
        print("so the score is ..")
        print(v.counter - 1000)




def the_program():
    start()
    s(1)
    choose()
    s(1)
    end()
    s(2)
    lucky()
