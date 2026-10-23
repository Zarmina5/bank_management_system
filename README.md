#  Bank Management System (BMS)

A Bank Management System developed using **Python and MySQL** to manage customer information, bank accounts, credentials, and financial transactions. This project uses object-oriented programming, database connectivity, input validation, and CRUD operations to organize banking data.

##  Features

- **Customer Management:** Register and manage customer information.
- **Account Management:** Create and manage bank accounts.
- **Transaction Management:** Handle financial transactions and maintain transaction records.
- **Credential Management:** Manage customer credentials.
- **Unique ID Generation:** Generate unique IDs for customers, accounts, and transactions.
- **Data Validation:** Validate user input before storing information in the database.
- **MySQL Database Integration:** Insert, retrieve, update, and delete data using MySQL.

##  Technologies Used

- **Python** — Application logic and functionality.
- **MySQL** — Database management and data storage.
- **mysql-connector-python** — Connects Python to MySQL.
- **python-dotenv** — Loads database configuration from environment variables.
- **VS Code** — Development environment.

## 📂 Project Structure

```text
bank_account_managment/
│
├── .env.example
├── .gitignore
├── README.md
├── main.py
│
├── database/
│   └── db_connection.py
│
├── models/
│   ├── customer.py
│   ├── account.py
│   ├── credential.py
│   └── transaction.py
│
├── services/
│   ├── customer_service.py
│   ├── account_service.py
│   ├── transaction_service.py
│   └── credential.py
│
└── utils/
    ├── id_generator.py
    ├── acccount_validator.py
    ├── credential_validator.py
    ├── customer_validator.py
    └── transaction_validator.py


##  Requirements
- Python 3.x
- MySQL Server
- pip (Python package installer)

##  Installation and Setup

### 1. Clone the Repository


```bash
git clone https://github.com/Zarmina5/bank_management_system.git
cd bank_account_managment
```

### 2. Install Dependencies

Run the following command in your terminal:

```bash
pip install mysql-connector-python python-dotenv
```

### 3. Create the Database

Open MySQL and execute:

```sql
CREATE DATABASE bank_management;
```

Create the required tables for customers, accounts, and transactions using the SQL queries in your project.

### 4. Configure Environment Variables


### Database Configuration

1. Install MySQL Server.
2. Create a database named `bank_management`.
3. Create a `.env` file in the project's root directory.
4. Add your own MySQL connection settings to the `.env` file.
5. Run the application using `python main.py`.

**Note:** The `.env` file is excluded from version control to protect database credentials.


### 5. Run the Application

From the project's root directory, execute:

```bash
python main.py
```

##  Database

The application uses MySQL to store and manage banking data, including:

- Customer details
- Bank account information
- Customer credentials
- Transaction records

Python connects to MySQL to execute queries and perform database operations.

##  Concepts Practiced

- Python functions and modules
- Object-oriented programming (OOP)
- CRUD operations (Create, Read, Update, Delete)
- MySQL queries and database connectivity
- Environment variables and configuration management
- Input validation
- Unique ID generation
- Modular project organization

##  Project Goal

The goal of this project is to apply Python programming and database concepts to a practical banking application while improving programming logic, code organization, and database management skills.

## 👩 Author

**Zarmina Rehman**

Computer Science Student — 5th Semester

- **GitHub:** [Zarmina5](https://github.com/Zarmina5)



