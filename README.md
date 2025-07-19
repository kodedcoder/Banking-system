# 🏦 Python Banking System

A fully functional banking system built using **Python** and **Tkinter**, supporting core banking operations such as customer management, money transfers, interest calculation, and admin functionality. This project includes a graphical user interface, data persistence via JSON, and is structured using object-oriented principles.

## 🚀 Features

### ✅ Admin Functionality
- Secure login with username and password
- View all customer account details
- Search for customers by last name
- Transfer money between accounts
- Delete customer accounts
- Generate management reports (total funds, interest, overdrafts)

### ✅ Customer Account Features
- Deposit and withdraw money
- Update personal information (name, address)
- View account balance and details
- Calculate interest and overdraft usage

### ✅ GUI (Graphical User Interface)
- Built with Tkinter
- Admin dashboard
- Customer account operations interface
- User-friendly layout with organized views
- Real-time feedback and validation

### ✅ Data Persistence
- All customer and admin data is saved and loaded from a local `bank_data.json` file.
- Changes (like deposits, transfers, updates) are persisted between sessions.



## 💻 Requirements

- Python 3.8 or higher
- Tkinter (included by default in most Python installations)

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-banking-system.git
   cd python-banking-system
Run the GUI Application:

bash
Copy
Edit
python gui.py
First-time launch: If bank_data.json doesn't exist, sample data will be auto-generated.
