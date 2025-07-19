from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []

import json
class BankSystem:
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()

    def save_bank_data(self):
        data = {
            'accounts': [
                {
                    'fname': acc.fname,
                    'lname': acc.lname,
                    'address': acc.address,
                    'account_no': acc.account_no,
                    'balance': acc.balance,
                    'account_type': acc.account_type,
                    'interest_rate': acc.interest_rate,
                    'overdraft_limit': acc.overdraft_limit
                } for acc in self.accounts_list
            ],
            'admins': [
                {
                    'fname': adm.fname,
                    'lname': adm.lname,
                    'address': adm.address,
                    'username': adm.username,
                    'password': adm.password,
                    'super_user': adm.super_user
                } for adm in self.admins_list
            ]
        }
        with open('bank_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def load_bank_data(self):
        try:
            with open('bank_data.json', 'r') as f:
                data = json.load(f)
                self.accounts_list = [CustomerAccount(**acc) for acc in data['accounts']]
                self.admins_list = [Admin(**adm) for adm in data['admins']]
        except FileNotFoundError:
            account_no = 1234
            self.accounts_list.append(CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, "Current", 0.02, 500))
            account_no += 1
            self.accounts_list.append(CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, "Savings", 0.04, 0))
            account_no += 1
            self.accounts_list.append(CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, "Savings", 0.04, 0))
            account_no += 1
            self.accounts_list.append(CustomerAccount("Ali", "Abdallah", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, "Current", 0.02, 200))

            self.admins_list.append(Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True))
            self.admins_list.append(Admin("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False))
            self.save_bank_data()

    def admin_login(self, username, password):
        for admin in self.admins_list:
            if admin.get_username() == username and admin.get_password() == password:
                return "Login successful!", admin
        return "Invalid username or password.", None

    def search_customers_by_name(self, customer_lname):
        return [cust for cust in self.accounts_list if cust.get_last_name().lower() == customer_lname.lower()]

    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        sender_list = self.search_customers_by_name(sender_lname)
        receiver_list = self.search_customers_by_name(receiver_lname)

        if not sender_list or not receiver_list:
            print("Sender or Receiver not found.")
            return

        sender = sender_list[0]
        receiver = next((cust for cust in receiver_list if str(cust.get_account_no()) == str(receiver_account_no)), None)

        if receiver is None:
            print("Receiver account number mismatch.")
            return

        if sender.get_balance() + sender.overdraft_limit < amount:
            print("Insufficient balance for transfer.")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)
        print("Transfer successful!")
        self.save_bank_data()

    def print_all_accounts_details(self):
        for idx, c in enumerate(self.accounts_list, 1):
            print(f"\n {idx}. ", end='')
            c.print_details()
            print("------------------------")

    def print_management_report(self):
        print("\n~~~~~ Bank Management Report ~~~~~")
        print(f"Total number of customers: {len(self.accounts_list)}")
        total_balance = sum(c.get_balance() for c in self.accounts_list)
        total_interest = sum(c.get_interest() for c in self.accounts_list)
        total_overdrafts = sum(c.get_overdraft() for c in self.accounts_list)
        print(f"Total funds in bank: £{total_balance:.2f}")
        print(f"Total interest payable (1 year): £{total_interest:.2f}")
        print(f"Total overdrafts in use: £{total_overdrafts:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def admin_menu(self, admin_obj):
        print("\nWelcome Admin %s %s : Available options are:" % (admin_obj.get_first_name(), admin_obj.get_last_name()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Customer account operations & profile settings")
        print("3) Delete customer")
        print("4) Print all customers detail")
        print("5) Management report")
        print("6) Sign out")
        return int(input("Choose your option: "))

    def run_admin_options(self, admin_obj):
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)
            elif choice == 2:
                lname = input("Enter customer last name: ")
                customers = self.search_customers_by_name(lname)
                if customers:
                    for idx, c in enumerate(customers):
                        print(f"{idx + 1}) {c.get_first_name()} {c.get_last_name()}, Acc No: {c.get_account_no()}")
                    selected = int(input("Select customer (number): ")) - 1
                    customers[selected].run_account_options()
                else:
                    print("Customer not found.")
            elif choice == 3:
                lname = input("Enter customer last name to delete: ")
                customers = self.search_customers_by_name(lname)
                if customers:
                    for idx, c in enumerate(customers):
                        print(f"{idx + 1}) {c.get_first_name()} {c.get_last_name()}, Acc No: {c.get_account_no()}")
                    selected = int(input("Select customer to delete (number): ")) - 1
                    self.accounts_list.remove(customers[selected])
                    self.save_bank_data()
                    print("Customer deleted successfully.")
                else:
                    print("Customer not found.")
            elif choice == 4:
                self.print_all_accounts_details()
            elif choice == 5:
                self.print_management_report()
            elif choice == 6:
                loop = 0
        print("\n Exit account operations")

    def main_menu(self):
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Python Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Admin login")
        print("2) Quit Python Bank System")
        return int(input("Choose your option: "))

    def run_main_options(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input("\n Please input admin username: ")
                password = input("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print("\n Thank-You for stopping by the bank!")


if __name__ == "__main__":
    app = BankSystem()
    app.run_main_options()
    