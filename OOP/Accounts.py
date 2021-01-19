import pytz
import datetime

class Accounts:

    @staticmethod#To create static method
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Accounts._current_time(), balance)]
        print('Account created for ' + self._name)
        self.showbalance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Accounts._current_time(), amount))#Accounts is used because it is static

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Accounts._current_time(), -amount))

        else:
            print('The entered amount is greater than current balance')

    def showbalance(self):
        print('The current balance is ' + str(self.__balance))
        self.show_transaction()

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'Deposited'
            else:
                tran_type = 'Withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount, tran_type, date, date.astimezone()))
#help(Accounts)

if __name__ == '__main__':
    A = Accounts('A', 1000)
    A.deposit(1000)
    A.showbalance()
    A.withdraw(500)
    A.showbalance()
    #A.show_transaction()

    B = Accounts('B', 800)
    B.deposit(100)
    B.showbalance()
    B.withdraw(200)
    B.showbalance()
    B.__balance = 200#Name mangling done using two underscores before a class variable and if same variabel
    #is used cannot make changes
    B.showbalance()