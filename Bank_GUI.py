# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 02:07:15 2025

@author: USER
"""
import tkinter as tk
from tkinter import messagebox
from bank_system import BankSystem  # Assumes your class code is in bank_system.py

class BankSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Bank System")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")
        self.bank = BankSystem()
        self.admin = None
        self.main_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Vrippy Bank", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=40)
        tk.Button(self.root, text="Admin Login", font=("Arial", 14), width=20, command=self.login_screen).pack(pady=20)
        tk.Button(self.root, text="Exit", font=("Arial", 14), width=20, command=self.root.quit).pack(pady=10)

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Login", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

        tk.Label(self.root, text="Username:", bg="#f0f0f0").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#f0f0f0").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack(pady=5)

        def login():
            username = username_entry.get()
            password = password_entry.get()
            msg, admin = self.bank.admin_login(username, password)
            messagebox.showinfo("Login", msg)
            if admin:
                self.admin = admin
                self.dashboard_screen()

        tk.Button(self.root, text="Login", font=("Arial", 12), command=login).pack(pady=15)
        tk.Button(self.root, text="Back", command=self.main_screen).pack()

    def dashboard_screen(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome {self.admin.get_first_name()} {self.admin.get_last_name()}", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)

        tk.Button(self.root, text="Transfer Money", width=30, command=self.transfer_money).pack(pady=5)
        tk.Button(self.root, text="Customer Account Operations", width=30, command=self.customer_operations).pack(pady=5)
        tk.Button(self.root, text="Delete Customer", width=30, command=self.delete_customer).pack(pady=5)
        tk.Button(self.root, text="Show All Customers", width=30, command=self.show_all_customers).pack(pady=5)
        tk.Button(self.root, text="Management Report", width=30, command=self.show_report).pack(pady=5)
        tk.Button(self.root, text="Sign Out", width=30, command=self.main_screen).pack(pady=20)

    def transfer_money(self):
        self.clear_screen()
        tk.Label(self.root, text="Transfer Money", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

        sender_entry = tk.Entry(self.root)
        receiver_entry = tk.Entry(self.root)
        receiver_acc_entry = tk.Entry(self.root)
        amount_entry = tk.Entry(self.root)

        for label, entry in zip(["Sender Last Name:", "Receiver Last Name:", "Receiver Account No:", "Amount to Transfer:"], [sender_entry, receiver_entry, receiver_acc_entry, amount_entry]):
            tk.Label(self.root, text=label, bg="#f0f0f0").pack()
            entry.pack(pady=2)

        def do_transfer():
            try:
                amount = float(amount_entry.get())
                self.bank.transferMoney(sender_entry.get(), receiver_entry.get(), receiver_acc_entry.get(), amount)
                self.bank.save_bank_data()
                messagebox.showinfo("Success", "Transfer successful!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Transfer", command=do_transfer).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack()

    def customer_operations(self):
        self.clear_screen()
        tk.Label(self.root, text="Customer Account Operations", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

        tk.Label(self.root, text="Enter Last Name of Customer:", bg="#f0f0f0").pack()
        lname_entry = tk.Entry(self.root)
        lname_entry.pack(pady=5)

        def search_customer():
            lname = lname_entry.get()
            customers = self.bank.search_customers_by_name(lname)
            if customers:
                for idx, cust in enumerate(customers):
                    tk.Button(self.root, text=f"{cust.get_first_name()} {cust.get_last_name()} - {cust.get_account_no()}", command=lambda c=cust: self.account_menu(c)).pack(pady=2)
            else:
                messagebox.showerror("Not Found", "No customer with that last name.")

        tk.Button(self.root, text="Search", command=search_customer).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack()

    def account_menu(self, customer):
        self.clear_screen()
        tk.Label(self.root, text="Customer Menu", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

        def deposit():
            amount = simple_input("Enter deposit amount:")
            if amount:
                customer.deposit(float(amount))
                self.bank.save_bank_data()
                messagebox.showinfo("Success", "Deposit complete.")

        def withdraw():
            amount = simple_input("Enter withdraw amount:")
            if amount:
                customer.withdraw(float(amount))
                self.bank.save_bank_data()

        def update_name():
            fname = simple_input("Enter new first name:")
            lname = simple_input("Enter new last name:")
            if fname: customer.update_first_name(fname)
            if lname: customer.update_last_name(lname)
            self.bank.save_bank_data()

        def update_address():
            address = simple_input("Enter new address (comma separated):")
            if address:
                customer.update_address(address.split(","))
                self.bank.save_bank_data()

        def show_details():
            messagebox.showinfo("Customer Details", f"Name: {customer.get_first_name()} {customer.get_last_name()}\nAddress: {', '.join(customer.get_address())}\nAccount No: {customer.get_account_no()}\nBalance: £{customer.get_balance():.2f}")

        def simple_input(prompt):
            top = tk.Toplevel(self.root)
            top.title(prompt)
            tk.Label(top, text=prompt).pack()
            entry = tk.Entry(top)
            entry.pack()
            val = []
            def submit():
                val.append(entry.get())
                top.destroy()
            tk.Button(top, text="OK", command=submit).pack()
            self.root.wait_window(top)
            return val[0] if val else None

        tk.Button(self.root, text="Deposit", command=deposit).pack(pady=2)
        tk.Button(self.root, text="Withdraw", command=withdraw).pack(pady=2)
        tk.Button(self.root, text="Update Name", command=update_name).pack(pady=2)
        tk.Button(self.root, text="Update Address", command=update_address).pack(pady=2)
        tk.Button(self.root, text="Show Details", command=show_details).pack(pady=2)
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack(pady=10)

    def delete_customer(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Customer", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
        tk.Label(self.root, text="Enter Last Name of Customer:", bg="#f0f0f0").pack()
        lname_entry = tk.Entry(self.root)
        lname_entry.pack(pady=5)

        def search_customer():
            lname = lname_entry.get()
            customers = self.bank.search_customers_by_name(lname)
            if customers:
                for idx, cust in enumerate(customers):
                    def delete(c=cust):
                        self.bank.accounts_list.remove(c)
                        self.bank.save_bank_data()
                        messagebox.showinfo("Deleted", "Customer deleted successfully.")
                        self.dashboard_screen()
                    tk.Button(self.root, text=f"Delete {cust.get_first_name()} {cust.get_last_name()} - {cust.get_account_no()}", command=delete).pack(pady=2)
            else:
                messagebox.showerror("Not Found", "No customer with that last name.")

        tk.Button(self.root, text="Search", command=search_customer).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack()

    def show_all_customers(self):
        self.clear_screen()
        tk.Label(self.root, text="All Customers", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
        for cust in self.bank.accounts_list:
            tk.Label(self.root, text=f"{cust.get_first_name()} {cust.get_last_name()} - {cust.get_account_no()} - £{cust.get_balance():.2f}", bg="#f0f0f0").pack()
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack(pady=20)

    def show_report(self):
        total_customers = len(self.bank.accounts_list)
        total_balance = sum(c.get_balance() for c in self.bank.accounts_list)
        total_interest = sum(c.get_interest() for c in self.bank.accounts_list)
        total_overdraft = sum(c.get_overdraft() for c in self.bank.accounts_list)
        report = (f"Total Customers: {total_customers}\n"
                  f"Total Balance: £{total_balance:.2f}\n"
                  f"Total Interest (1 Year): £{total_interest:.2f}\n"
                  f"Total Overdrafts in Use: £{total_overdraft:.2f}")
        messagebox.showinfo("Management Report", report)


if __name__ == "__main__":
    root = tk.Tk()
    app = BankSystemGUI(root)
    root.mainloop()

