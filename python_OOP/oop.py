class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price) -> None:
        self.make = make
        self.price = price
        self.on = False


    def switch_on(self)-> None:
        self.on = True


def main():
    print()


    # a = 12
    # b = 4
    # print(a + b)
    # print(a.__add__(b))

#______________________________________________


    kenwood = Kettle("Kenwood", 8.99)
    print(kenwood.make)
    print(kenwood.price)


    kenwood.price = 12.75
    print(kenwood.price)

    hamilton = Kettle("Hamilton", 14.55)

    print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

    print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

    # value is False
    print(hamilton.on)

    # setting the value to True
    hamilton.switch_on()
    print(hamilton.on)

    Kettle.switch_on(kenwood)
    print(kenwood.on)
    kenwood.switch_on()
    
#_______________________________________________________________

    print("*" * 80)

    # adding variables to the class 
    kenwood.power = 1.5
    print(kenwood.power)

    print("Switch to atomic power")
    Kettle.power_source = "atomic power"
    print(Kettle.power_source)

    kenwood.power_source="gas"
    print(kenwood.power_source)
    print(hamilton.power_source)

    print(Kettle.__dict__)
    print(kenwood.__dict__)
    print(hamilton.__dict__)





if __name__ == "__main__":
    main()