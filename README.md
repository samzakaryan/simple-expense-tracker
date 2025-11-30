# Expense Tracker

A lightweight command-line application for tracking personal finances. Manage your income, expenses, and categories with automatic data persistence.

## Features

- Add and remove expense/income categories
- Track expenses and income with categorization
- Real-time balance tracking
- Persistent data storage (saves automatically on exit)
- Clean, intuitive terminal interface
- Input validation and error handling

## How to Use

1. Clone the repository
2. Run `tracker.py` (or whatever your main file is named)
3. Use the menu to manage your finances:
   - Add categories (e.g., Food, Transport, Salary)
   - Record expenses and income
   - View your current balance
   - All data saves automatically only when you quit

## Data Storage

The application stores data in three text files:
- `categories.txt` - Your expense/income categories
- `expenses.txt` - Transaction history
- `account.txt` - Current balance

## Requirements

- Python 3.x
- No external dependencies required

## Future Improvements

- Add date/time stamps to all transactions
- Search and filter expenses by date range or category
- Support for multiple currencies
- Undo last transaction feature
