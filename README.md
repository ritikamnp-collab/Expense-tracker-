# Expense Tracker

A Python-based command-line Expense Tracker designed to help users efficiently manage their daily expenses. The application allows users to record, view, delete, and analyze expenses through a simple menu-driven interface. All expense data is stored persistently using CSV files, ensuring that records remain available across sessions.

---

## Overview

Managing personal finances is an essential skill, and this project provides a lightweight solution for tracking expenses without the need for complex software or databases. The Expense Tracker enables users to maintain organized financial records and generate monthly spending reports with category-wise analysis.

---

## Features

### Add Expense
- Record a new expense with category, description, and amount.
- Automatically assigns a unique expense ID.
- Captures the current date automatically.

### View Expenses
- Display all recorded expenses in a structured tabular format.
- View expense details including date, category, description, and amount.

### Delete Expense
- Remove an expense record using its unique ID.
- Ensures accurate expense management and data maintenance.

### Monthly Report
- Generate spending reports for a specific month.
- Calculate total monthly expenditure.
- Display category-wise expense distribution.

### Persistent Data Storage
- Stores all expense records in a CSV file.
- Automatically creates the file if it does not exist.

---
## Data Format

Expenses are stored in a CSV file with the following structure:

| Field | Description |
|---------|------------|
| ID | Unique Expense Identifier |
| Date | Expense Date |
| Category | Expense Category |
| Description | Expense Details |
| Amount | Expense Amount |

Example:

```csv
ID,Date,Category,Description,Amount
1,2026-06-25,Food,Lunch,150
2,2026-06-25,Transport,Bus Ticket,50
```

---

## How to Run

### Prerequisites

- Python 3.x installed on your system

### Steps

1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

2. Navigate to the project directory

```bash
cd expense-tracker
```

3. Run the application

```bash
python expense_tracker.py
```

---

## Application Menu

```text
====== EXPENSE TRACKER ======

1. Add Expense
2. View Expenses
3. Delete Expense
4. Monthly Report
5. Exit
```

---

## Sample Output

### Adding an Expense

```text
Enter Category: Food
Enter Description: Lunch
Enter Amount: 150

Expense Added Successfully
```

### Viewing Expenses

```text
ID   Date         Category       Description              Amount
---------------------------------------------------------------
1    2026-06-25   Food           Lunch                    150
```

### Monthly Report

```text
===== MONTHLY REPORT =====

Month: 2026-06
Total Spending: Rs 150.00

Food: Rs 150.00
```

---

## Key Concepts Demonstrated

- File Handling in Python
- CSV Data Management
- CRUD Operations
- Modular Programming
- Dictionary-Based Data Aggregation
- Data Analysis Fundamentals
- Menu-Driven Application Development

---

## Future Enhancements

- Edit Existing Expenses
- Budget Tracking and Alerts
- Expense Filtering by Category
- Data Visualization using Matplotlib
- SQLite Database Integration
- PDF Report Generation
- Streamlit-Based Web Dashboard
- User Authentication System

---

## Learning Outcomes

This project helped strengthen practical knowledge of:

- Python Programming
- Data Persistence Techniques
- File and CSV Operations
- Structured Program Design
- Report Generation
- Financial Data Management

---

## Author

**Ritika Nitin Pathak**

Computer Engineering Student  
MKSSS Cummins College of Engineering for Women, Nagpur

---

If you found this project useful, consider giving the repository a ⭐.
