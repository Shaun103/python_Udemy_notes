class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeeeeeee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)
    
    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("Come on in, the water's lovely")
    
    def quack(self):
        print("Quack quack quack")

    # composition
    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, it's a bit chilly this far South")
    
    def quack(self):
        print("Are you 'avin' a larf? I'm a penquin")


def test_duck(object):
    object.walk()
    object.swim()
    object.quack()


def main():
    print()

    donald= Duck()
    test_duck(donald)

    print()

    # percy = Penguin()
    # test_duck(percy)

    # print()
#___________________________________________


    donald.fly()







if __name__ == "__main__":
    main()