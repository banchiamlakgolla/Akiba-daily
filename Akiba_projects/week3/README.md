# Akiba Technologies — Week 3 Python Programming

**Topic:** Python Functions — Intermediate Practice  
**Assignment:** Individual (Banchiamlak Golla)  
**Difficulty:** Medium  
**Language:** Python 3

## About This Project

This repository contains my work for Week 3 of the Akiba Technologies Python Programming Bootcamp. In this assignment, I practise using functions to solve different problems and make my programs more organized.

While working through the tasks, I get to practise passing information to functions, returning results, using default parameters, checking user input, and working with lists and dictionaries. I am also learning how breaking a large problem into smaller functions makes code easier to understand, test, and improve.

The repository includes ten coding tasks, the Akiba Business Management Toolkit mini-project, and my answers to two theory questions.

## What I Practice in This Assignment

Through these tasks, I work on how to:

- Write functions that each have a clear purpose.
- Use parameters and return values to pass information between parts of a program.
- Reuse code instead of writing the same logic repeatedly.
- Work with conditions, loops, strings, lists, and dictionaries.
- Check input and handle invalid or boundary values.
- Test and debug programs and make the code easier to maintain.

## Project Structure

```text
akiba-week-3-python/
├── README.md
├── theory_answers.md
├── task_01_shopping_receipt.py
├── task_02_student_analyzer.py
├── task_03_number_analyzer.py
├── task_04_text_analyzer.py
├── task_05_bank_processor.py
├── task_06_inventory_controller.py
├── task_07_password_analyzer.py
├── task_08_electricity_calculator.py
├── task_09_quiz_engine.py
├── task_10_expense_analyzer.py
└── mini_project/
    ├── main.py
    ├── products.py
    ├── sales.py
    └── reports.py
```

The mini-project is organized into separate files for the main program, product management, sales, and reports. This helps keep related functions together and makes it easier to reuse them across the program.

## Coding Tasks

### Task 1 — Smart Shopping Receipt Generator

For this task, I build a program that calculates a shopping subtotal, applies a discount, calculates tax, and creates a receipt showing the final amount.

The main functions are:

- `calculate_subtotal(items)`
- `calculate_discount(subtotal)`
- `calculate_tax(amount, tax_rate)`
- `generate_receipt(items, tax_rate)`

The discount depends on the purchase amount:

- Below 1,000 Birr: no discount
- 1,000–2,999 Birr: 5% discount
- 3,000 Birr or more: 10% discount

I also need to check for invalid prices, quantities, and tax rates.

### Task 2 — Student Performance Analyzer

In this task, I analyse students' exam scores and create a class report. The program checks whether scores are valid, assigns grades, calculates the class average, finds the highest and lowest scores, and counts how many students passed or failed.

The grade ranges are:

- 90–100: A
- 80–89: B
- 70–79: C
- 60–69: D
- Below 60: F

A score of 50 is considered a pass. The challenge is to find students who scored above the class average without using `max()`, `min()`, or `sum()` for the main calculations.

### Task 3 — Advanced Number Analyzer

Here, I create reusable functions to analyse a number. The program checks whether the number is even or odd and whether it is prime. It also finds the number's positive divisors, calculates the sum of its digits, and reverses its digits.

I also need to decide how the program should handle zero and negative numbers.

### Task 4 — Text Statistics and Word Analyzer

This task is about analysing a paragraph. I write functions to count words, count characters without spaces, count vowels and consonants, and find the longest word. The program also counts how often each word appears and identifies repeated words.

The analysis should ignore letter case and remove basic punctuation before counting. As an extra challenge, I find the five most frequent words without using an external library.

### Task 5 — Bank Transaction Processor

For this task, I build a simple banking program that supports deposits, withdrawals, balance checks, and transaction history. It starts with an opening balance that can be configured and keeps a record of successful transactions.

The program must reject zero or negative transaction amounts and prevent withdrawals that are greater than the available balance. It also calculates the total amount deposited, the total withdrawn, and the final balance.

The extra challenge is to add a daily withdrawal limit.

### Task 6 — Inventory Stock Controller

In this task, I create a small inventory system. It allows a user to add and search for products, update prices, increase stock, and sell products. It also calculates the total value of the inventory and shows products with low stock.

Product names cannot be empty or duplicated. Prices and stock quantities cannot be negative, and a sale must not exceed the available stock. The low-stock threshold should be adjustable through a function parameter.

### Task 7 — Password Policy and Strength Analyzer

Here, I practise checking several password requirements, including minimum length, uppercase letters, lowercase letters, digits, and special characters.

The program reports whether each requirement passes or fails and explains which requirements are missing instead of stopping at the first failure. The minimum length can also be changed using a default parameter.

I use fictional passwords for testing because this is an educational exercise, not a complete password-security solution.

### Task 8 — Date-Free Electricity Bill Calculator

For this task, I calculate an electricity bill using the example tiered rates provided in the assignment.

| Consumption range | Rate per unit |
|---|---:|
| First 50 units | 0.50 Birr |
| Next 100 units | 0.75 Birr |
| Above 150 units | 1.20 Birr |

I write functions to validate the units consumed, calculate the charge for each tier, find the total bill, and display a billing summary. I also practise using a default parameter for an optional fixed service fee.

**Note:** These rates are fictional assignment rates, not official Ethiopian electricity tariffs.

### Task 9 — Reusable Quiz Engine

In this task, I build a command-line quiz. Each question contains the question text, a list of options, and the correct answer.

The program displays questions, checks answers, rejects invalid options, and updates the score. At the end, it shows the final score, percentage, and number of correct and incorrect answers. Answers should work regardless of whether the user types uppercase or lowercase letters.

The challenge is to assign a result category based on the final percentage and let the user play again without restarting Python.

### Task 10 — Function-Based Expense Analyzer

For the final coding task, I create an expense tracker. Each expense has a description, category, and amount.

The program can add expenses, calculate total spending, group spending by category, find the largest expense, and identify expenses above a chosen threshold. It also generates a spending report.

The extra challenge is to calculate the percentage of total spending for each category and identify the category with the highest total.

## Mini-Project — Akiba Business Management Toolkit

The mini-project brings together the function concepts I practise in the ten tasks. The goal is to build a menu-driven program that helps a small business manage its products, sales, and reports.

### Product Management

- Add a product.
- Search for a product.
- Update product information.
- Display all products.

### Sales Management

- Record a sale.
- Check that the quantity is valid.
- Reduce stock after a successful sale.
- Calculate the total cost of the sale.

### Reporting

- Calculate total revenue.
- Calculate the value of the remaining inventory.
- Display products with low stock.
- Show a summary of recorded sales.

I organize the program using separate functions, pass information through parameters, and return calculated results where appropriate. Lists and dictionaries store product and sales information. The program also needs to validate user input, handle missing products and insufficient stock, and keep showing the menu until the user chooses to exit.

**Bonus challenge:** Create a receipt for each sale that shows the product name, quantity, unit price, and total cost.

## Requirements

To run the programs, I need:

- Python 3
- A code editor or terminal
- Git and a GitHub account to manage and submit the project

The assignment does not specify any third-party Python packages.

## How to Run the Programs

1. Clone the repository or download the project files.
2. Open a terminal in the project folder.
3. Run the Python file for the task you want to try.

For example, to run the shopping receipt task:

```bash
python task_01_shopping_receipt.py
```

To run the expense analyzer:

```bash
python task_10_expense_analyzer.py
```

To run the mini-project:

```bash
python mini_project/main.py
```

Depending on the computer setup, I may need to use `python3` instead of `python`.

## Testing My Programs

I test the programs with normal inputs as well as boundary and invalid values. This helps me check how they behave in different situations.

Some examples I test include:

- Empty product names or descriptions.
- Negative prices, quantities, scores, or transaction amounts where they are not allowed.
- Electricity consumption at tier boundaries, such as 50 and 150 units.
- Valid and invalid quiz answers.
- Searching for a product that does not exist.
- Trying to sell more items than are available in stock.
- Empty lists or other cases where there may be no data to analyse.

Testing these cases helps me find mistakes and make the programs more reliable.

## Theory Questions

The file [`theory_answers.md`](theory_answers.md) contains my answers to the two theory questions:

1. **Function Design:** Why a very large function can be hard to maintain and how smaller functions can make code easier to reuse, test, and debug.
2. **Mutable Data and Function Side Effects:** Why changing a list inside a function can also change the original list, and how returning a new list can help avoid that.

## Assignment Checklist

I use this checklist to keep track of the work before submission. The checked items below reflect the current project status and should be updated if any task still needs to be completed or tested.

- [x] Complete Task 1: Shopping Receipt Generator
- [x] Complete Task 2: Student Performance Analyzer
- [x] Complete Task 3: Advanced Number Analyzer
- [x] Complete Task 4: Text Statistics and Word Analyzer
- [x] Complete Task 5: Bank Transaction Processor
- [x] Complete Task 6: Inventory Stock Controller
- [x] Complete Task 7: Password Policy and Strength Analyzer
- [x] Complete Task 8: Electricity Bill Calculator
- [x] Complete Task 9: Quiz Engine
- [x] Complete Task 10: Expense Analyzer
- [x] Complete the Akiba Business Management Toolkit
- [x] Add answers to `theory_answers.md`
- [x] Test normal, boundary, and invalid inputs
- [x] Review file names and project structure
- [x] Commit and push the work to GitHub

## GitHub Submission

My project is stored in the Akiba projects area of my GitHub repository:

[View my Akiba projects on GitHub](https://github.com/banchiamlakgolla/Akiba-daily/tree/main/Akiba_projects/)

After reviewing and testing the work, I can use these commands to commit and push my changes:

```bash
git add .
git commit -m "Complete Week 3 functions assignment"
git push
```

I will submit the repository link according to the bootcamp instructions.

## What I Learned

Working on this assignment helps me practice breaking problems into smaller functions instead of putting everything into one large block of code. I also get more experience using parameters and return values, validating input, working with lists and dictionaries, and thinking about how to test my programs.

As I work through the tasks and mini-project, I can use what I learn from one program in the next and keep improving the way I organize my code.

---

**Akiba Technologies — Learn • Build • Grow**
