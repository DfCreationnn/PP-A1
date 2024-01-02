from random import randrange as r


class Variables:
    note = "note that when the programm has finished it wil say :'Process finished with exit code 0'"
    User_input = input("Hi there ! choose a number between 1 to 999 ")
    after = "The number you choosed is perfect"
    User_int = int(User_input)
    error = "Error please choose another number"
    start_signal = 0
    random_number_chooser = r(1, 1000000)
    random_number = r(1, random_number_chooser)
    load1 = 0
    load2 = 0
    load_p = 0
    load_p_adder = 5.546248245
    load_pstr = str(load_p)
    done1 = "Done!"
    counter = 0
    counter_str = str(counter)
    end1 = "The number you choosed mathced the number that the program choose in ..."
    end2 = "..." + counter_str + " tries"
    error404 = "Error 404 , number input did not found"
    error4040 = 0
    lucky = r(0, 20)
    lucky_sms = "You are lucky so you got - 1000 from the score !!!!!!"

