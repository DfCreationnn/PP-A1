from random import randrange as r

class Variables:
    def __init__(self):
        self.note = "Note that when the program has finished, it will say: 'Process finished with exit code 0'"
        self.User_input = 0
        self.after = "The number you chose is perfect"
        self.User_int = 0
        self.error = "Error, please choose another number"
        self.start_signal = 0
        self.random_number_chooser = r(1, 1000000)
        self.random_number = r(1, self.random_number_chooser)
        self.load1 = 0
        self.load2 = 0
        self.load_p = 0
        self.load_p_adder = 5.546248245
        self.load_pstr = str(self.load_p)
        self.done1 = "Done!"
        self.counter = 0
        self.counter_str = str(self.counter)
        self.end1 = f"The number you chose matched the number that the program chose in {self.counter_str} tries"
        self.error404 = "Error 404, number input not found"
        self.error4040 = 0
        self.lucky = 0
        self.lucky_sms = "You are lucky, so you got -1000 from the score!!!!!!"

    def get_user_input(self):
        while True:
            try:
                self.User_input = int(input("Hi there! Choose a number between 1 to 999: "))
                if 0 < self.User_input < 1000:
                    break
                else:
                    print("Error: Please choose a number between 1 and 999.")
            except ValueError:
                print("Error: Please enter a valid integer.")

    def generate_lucky_number(self):
        self.lucky = r(0, 20)


# Main program
def start():
    print(variables_instance.note)
    print("Loading...")
    variables_instance.get_user_input()
    print(variables_instance.after)
    variables_instance.start_signal = 1
    variables_instance.error4040 = 1

def choose():
    if variables_instance.start_signal == 1:
        print(f"Choosing a random number between 1 and {variables_instance.random_number_chooser}...")
        while variables_instance.start_signal == 1:
            variables_instance.random_number = r(1, variables_instance.random_number_chooser)
            variables_instance.counter += 1
            variables_instance.counter_str = str(variables_instance.counter)
            if variables_instance.User_int == variables_instance.random_number:
                if variables_instance.load1 == 0:
                    print("Loading...")
                    variables_instance.load1 = 1
                    variables_instance.load2 = 1

                if variables_instance.load2 == 1:
                    variables_instance.load_p = variables_instance.load_p + variables_instance.load_p_adder
                    variables_instance.load_pstr = str(variables_instance.load_p)
                    print("%" + " " + variables_instance.load_pstr)

                    if variables_instance.load_p > 100:
                        print(variables_instance.done1)
                        variables_instance.start_signal = 0

def end():
    if variables_instance.error4040 == 1:
        print(variables_instance.end1)
        print("..." + variables_instance.counter_str + " tries")
    else:
        print(variables_instance.error404)

def lucky():
    print(variables_instance.counter)
    if variables_instance.lucky == 11:
        print(variables_instance.lucky_sms)
        print("So the score is...")
        print(variables_instance.counter - 1000)

# Example usage:
if __name__ == "__main__":
    variables_instance = Variables()
    start()
    choose()
    end()
    lucky()
