import datetime
import pytz


class Account:
    """Simple account class with balance"""

    # making a static method
    @staticmethod
    def _currently_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # Initial method
    def __init__(self, name: str="Default_Name", balance: int=0) -> None:
        self.name = name
        self._balance = balance
        # 
        self.transaction_list = [(Account._currently_time(), balance)] 
        print(f"Account Created for: {self.name}")
        self.show_balance()

    def deposit(self, amount: int=0) -> None:
        if amount > 0:
            self._balance += amount
            self.show_balance()
            #
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self.transaction_list.append((Account._currently_time(), amount))

    def withdraw(self, amount: int=0) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transaction_list.append((Account._currently_time(), -amount)) #-amount
        else: 
            print("Amount must be greater than 0 and no more than account balance")
            self.show_balance()

    def show_balance(self) -> None:
        print(f"{self.name}'s balance is ${self._balance}")
    
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"\t{amount} on {tran_type} (local time was {date.astimezone()})")
            # print("{:6} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))

def main():
    print()


    tim = Account("Tim", 0)

    tim.deposit(1000)
    tim.withdraw(500)

    tim.withdraw(2000)

    tim.show_transactions()

    # print(tim._currently_time())
     

#__________________________________________________


    # default_name = Account()

    # default_name.show_balance()

#__________________________________________________

    Steph = Account("Steph", 800)

    Steph.deposit(100)
    Steph.withdraw(200)

    Steph.show_transactions()

    # Steph._balance = 1000
    # print(Steph._balance)

    print(Steph.__dict__)

    Steph._Account__balance = 40
    Steph.show_balance()


if __name__ == "__main__":
    main()