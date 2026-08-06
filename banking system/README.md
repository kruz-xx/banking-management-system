#  Banking Management System

A console-based Banking Management System developed in **Python** using **Object-Oriented Programming (OOP)** principles. The project demonstrates data processing, modular architecture, and basic banking operations using CSV files as the data source.

---

##  Features

- View Customers
- View Accounts
- Search Account
- Deposit Money
- Withdraw Money
- Transfer Money
- View Transaction History
- Input Validation
- Modular OOP Architecture

---

##  Technologies Used

- Python 3.x
- Pandas
- OpenPyXL
- Object-Oriented Programming (OOP)

---

##  Project Structure

```
BMS/
│
├── app/
│   ├── database/
│   │   ├── __init__.py
│   │   └── csv_repo.py
│   │
│   ├── models/
│   │   ├── customer.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── services/
│   │   ├── customer_service.py
│   │   ├── account_service.py
│   │   └── transaction_service.py
│   │
│   ├── ui/
│   │   └── menu.py
│   │
│   └── main.py
│
├── data/
│   ├── raw/
│   │   └── raw_data.xlsx
│   │
│   └── processed/
│       ├── customers.csv
│       ├── accounts.csv
│       └── transactions.csv
│
├── scripts/
│   ├── dataset_importer.py
│   └── dataset_splitter.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Banking-Management-System.git
```

Move into the project directory:

```bash
cd Banking-Management-System
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Run the application:

```bash
python app/main.py
```

---

##  Menu

```
==================================================
        BANKING MANAGEMENT SYSTEM
==================================================

1. View Customers
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. View Transactions
8. Exit

==================================================
```

---

##  Architecture

The project follows a modular architecture.

```
User
   │
   ▼
Menu (UI)
   │
   ▼
Services
   │
   ▼
Models
   │
   ▼
CSV Repository
   │
   ▼
CSV Files
```

### Models

- Customer
- Account
- Transaction

### Services

- CustomerService
- AccountService
- TransactionService

### Repository

Responsible for loading data from CSV files and converting them into Python objects.

---

##  Dataset

The project uses a banking dataset containing:

- Customer Information
- Account Information
- Transaction Information
- Branch Details
- Currency
- Account Balance

The raw Excel dataset is processed into three normalized CSV files:

- customers.csv
- accounts.csv
- transactions.csv

---

##  Input Validation

The application validates:

- Invalid menu choices
- Invalid numeric input
- Negative deposits
- Negative withdrawals
- Negative transfers
- Insufficient account balance
- Invalid account IDs


---

##  Future Improvements

- Save updated balances back to CSV
- Database integration (SQLite/MySQL)
- Authentication system
- GUI/Desktop version
- REST API
- Unit testing

---

##  Author

**Krupa Sodagar**

B.Tech AI & Data Science Student

Python Intern at York IE

---

##  License

This project is created for educational purposes.