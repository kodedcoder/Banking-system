class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type, interest_rate, overdraft_limit):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = float(interest_rate)
        self.overdraft_limit = float(overdraft_limit)

    def update_first_name(self, fname):
        self.fname = fname

    def update_last_name(self, lname):
        self.lname = lname

    def get_first_name(self):
        return self.fname

    def get_last_name(self):
        return self.lname

    def update_address(self, addr):
        self.address = addr

    def get_address(self):
        return self.address

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("\n Withdrawal successful!")
        else:
            print("\n Insufficient funds including overdraft limit.")

    def print_balance(self):
        print("\n The account balance is %.2f" % self.balance)

    def get_balance(self):
        return self.balance

    def get_account_no(self):
        return self.account_no

    def get_interest(self):
        return self.balance * self.interest_rate

    def get_overdraft(self):
        return abs(self.balance) if self.balance < 0 else 0

    def account_menu(self):
        print("\n Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Check balance")
        print("4) Update customer name")
        print("5) Update customer address")
        print("6) Show customer details")
        print("7) Back")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def print_details(self):
        print(f"Customer: {self.fname} {self.lname}, Address: {', '.join(self.address)}, Account No: {self.account_no}, Type: {self.account_type}, Balance: £{self.balance:.2f}")

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                amount = float(input("\n Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == 2:
                amount = float(input("\n Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                fname = input("\n Enter new first name: ")
                lname = input("\n Enter new last name: ")
                self.update_first_name(fname)
                self.update_last_name(lname)
            elif choice == 5:
                addr = input("\n Enter new address (comma separated): ").split(',')
                self.update_address(addr)
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print("\n Exit account operations")
