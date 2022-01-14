

class Duck(object):
    
    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("Come on in, the water's lovely")
    
    def quack(self):
        print("Quack quack quack")


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

    percy = Penguin()
    test_duck(percy)

    print()



if __name__ == "__main__":
    main()