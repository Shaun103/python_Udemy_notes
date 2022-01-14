import random


# base class what the rest are inheriting
class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"I took {damage} points damage and have {self._hit_points} left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life")
            else:
                print(f"{self._name} is dead")
                self._alive = False

    def __str__(self) -> str:
        return f"Name: {self._name}, Lives: {self._lives}, Hit points: {self._hit_points} "


class Troll(Enemy):
    
    def __init__(self, name) -> None:
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self._name}. {self._name} stomp you")


class Vampire(Enemy):

    def __init__(self, name) -> None:
        super().__init__(name=name, lives=3, hit_points=12)

    def voice_line(self) -> None:
        print(f"{self._name} wants to suck your blood!")

    def dodges(self):
        if random.randint(1, 3) == 3:
            print()
            print(f"****** {self._name} dodges attack *****")
            print()
            return True
        else:
            return False

    # overrideing method
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name) -> None:
        super().__init__(name=name)
        self._hit_points = 140
    
    # overriding method 
    def take_damage(self, damage) -> None:
        super().take_damage(damage=damage // 4)


