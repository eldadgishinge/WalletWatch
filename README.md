# WalletWatch - Expense Tracking Web App

WalletWatch is a web application designed to help you track your expenses and manage your budgets efficiently. It provides a user-friendly interface for tracking transactions, categorizing expenses, setting budget limits, and generating financial reports.

## Features

- **Transaction Tracking**: Easily add incoming and outgoing transactions from various accounts (e.g., bank accounts, mobile money, cash). Associate transactions with specific categories and subcategories for better organization.

- **Budget Management**: Set budget limits for different spending categories. The application calculates and compares total expenses to the set budget, sending notifications when expenses exceed the budget.

- **Category Management**: Create and manage categories and subcategories to classify expenses effectively.

- **Expense Categorization**: Categorize expenses with ease, providing a clear overview of where your money is going.

- **Report Generation**: Generate detailed financial reports by specifying a start and end date. The application displays transactions within the selected date range and calculates total expenses for that period.

## Getting Started

1. **Installation**: Ensure you have Python 3.x and Django installed.

2. **Clone the Repository**: `git clone https://github.com/yourusername/WalletWatch.git`

3. **Set Up Virtual Environment** (optional but recommended): Create and activate a virtual environment.

4. **Install Dependencies**: Run `pip install -r requirements.txt`.

5. **Database Setup**: Migrate the database and create a superuser account for admin access.

6. **Run the Development Server**: Execute `python manage.py runserver`.

7. **Access the Application**: Open your web browser and go to `http://localhost:8000/` to start using WalletWatch.

## Usage

- **Adding Transactions**: Log in to your account and navigate to "Add Transaction" to start tracking your expenses.

- **Setting Budgets**: Go to "Set Budget" to set budget limits for different categories. The application will notify you when expenses exceed your budget.

- **Generating Reports**: Use the "Transaction List" to generate reports on your financial activities.
