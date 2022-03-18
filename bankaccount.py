class BankAccount:

    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def print_balance(self):
        print("Your current balance is:")
        print(self.balance)

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("please enter a valid amount")
        return self.balance

    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("you dont have enough funds to make this withdrawal")
        return self.balance

class SavingsBankAccount(BankAccount):
    INTEREST_RATE = 0.035

    def __init__(self, owner, balance, currency):
        BankAccount.__init__(self, owner, balance, currency)
        self.interest_rate = SavingsBankAccount.INTEREST_RATE

    def deposit_interest_earned(self):
        interest_earned = self.balance * SavingsBankAccount.INTEREST_RATE
        self.balance += interest_earned



class CheckingBankAccount(BankAccount):

    def __init__(self, owner, balance, currency, debit_card=None, credit_card=None):
        BankAccount.__init__(self, owner, balance, currency)
        self.debit_card = debit_card
        self.credit_card = credit_card


daniel_savings_account = SavingsBankAccount("Daniel", 34000, 'Naira')

daniel_savings_account.print_balance()
deposit = daniel_savings_account.make_deposit(2000)
withdrawl = daniel_savings_account.make_withdrawal(1900000)
print(deposit)
print(withdrawl)
daniel_savings_account = CheckingBankAccount("Daniel", 45000, 'Naira')

daniel_savings_account.make_deposit(4900)
