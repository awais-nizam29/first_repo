class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit (self):
        a = float(input("Enter the amount which you want to deposit: "))
        if a <= 0:
            raise ValueError(("Deposit amount must be positive"))
        self.__balance = self.__balance + a
        print(f"{a} has been deposited to your account.")

    def check_balance(self):
        print("Your balance is", self.__balance)
    
    def with_draw(self):
        b = float(input("Enter the amount which you want to withdraw: "))
        if b <= 0:
            raise ValueError("Withdraw amount must be positive")
        elif b > self.__balance:
            raise ValueError("Insufficient Balance")
        self.__balance = self.__balance - b
        print(f"{b} has been withdraw from your account")

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.__maintain_balance = 200
        self.interest_rate = 100
    
    def with_draw(self):
        b = float(input("Enter the amount which you want to With_draw: "))
        if b <= 0:
            raise ValueError("Withdraw amount must be positive.")

        elif b > self._BankAccount__balance:
            raise ValueError("Insufficient Balance") 
        elif self._BankAccount__balance - b < self.__maintain_balance:
            raise ValueError(f"Minimum balance of {self.__maintain_balance} must be in your account.")
        self._BankAccount__balance = self._BankAccount__balance - b
        print(f"{b} is deduted from your account")

    def add_interst_rate(self):
        self._BankAccount__balance = self._BankAccount__balance + self.interest_rate
        print(f"interest {self.interest_rate} is added into your account")

class BankApp:
    def __init__(self):
        self.account = SavingsAccount()
    
    def Bank_account(self):
        while True:
            print("Welcome to the Bank")
            print("Press 1 for Deposit")
            print("Press 2 to Check Balance")
            print("Press 3 to Withdraw")
            print("Press 4 to Add Interest")
            print("Press 5 to Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.account.deposit()
            elif choice == "2":
                self.account.check_balance()
            elif choice == "3":
                self.account.with_draw()
            elif choice == "4":
                self.account.add_interst_rate()
            elif choice == "5":
                print("Thanks for visiting")
                break
            else:
                print("Invalid Input")

app = BankApp()
app.Bank_account()
