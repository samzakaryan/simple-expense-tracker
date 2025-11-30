categories = []
expenses = []
account = 0

with open('categories.txt', 'r') as file:
    categories = [line.strip() for line in file]
with open('expenses.txt', 'r') as file:
    expenses = [line.strip() for line in file]
try:
    with open('account.txt', 'r') as file:
        account = int(file.read().strip())
except (FileNotFoundError, ValueError):
    account = 0

def add_categories():
    print("\n" + "=" * 50)
    print("  ADD NEW CATEGORY")
    print("=" * 50)
    new_category = input("Name of the category: ")
    while new_category in categories:
        print("Category already exists")
        new_category = input("Name of the category: ")
    categories.append(new_category)
    print(f"\nCategory '{new_category}' added successfully!")

def remove_category(): 
    print("\n" + "=" * 50)
    print("  REMOVE CATEGORY")
    print("=" * 50)
    if not categories:
        print("No categories to remove")
        return
    
    print("\nAvailable categories:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")
    print("-" * 50)
    
    try:
        user_input = int(input("Choose a category to remove (0 to cancel): "))
        if user_input == 0:
            print("Cancelled")
            return
        while user_input < 1 or user_input > len(categories):
            user_input = int(input("No category found. Try again: "))
        removed = categories.pop(user_input - 1)
        print(f"\nCategory '{removed}' removed successfully!")
    except ValueError:
        print("Wrong input")
        return

def view_categories():
    print("\n" + "=" * 50)
    print("  ALL CATEGORIES")
    print("=" * 50)
    if not categories:
        print("No categories to view")
        return
    
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")
    print("-" * 50)
    
def add_expense():
    global account
    print("\n" + "=" * 50)
    print("  ADD EXPENSE")
    print("=" * 50)
    
    if not categories:
        print("No categories yet. Add categories first!")
        return
    
    print("\nSelect category:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")
    print("-" * 50)
    
    try:
        user_input = int(input("Choose a category: "))
        while user_input < 1 or user_input > len(categories):
            user_input = int(input("No category found. Try again: "))
        expense_category = categories[user_input - 1]
    except ValueError:
        print("Wrong input")
        return
    
    try:
        user_expense = int(input("Enter expense amount: $"))
        while user_expense < 1:
            user_expense = int(input("Invalid amount. Try again: $"))
    except ValueError:
        print("Wrong input")
        return
    
    expenses.append(f"{-1 * user_expense}:{expense_category}")
    account -= user_expense
    print(f"\nExpense of ${user_expense} added to '{expense_category}'")
    print(f"New balance: ${account}")

def add_income():
    global account
    print("\n" + "=" * 50)
    print("  ADD INCOME")
    print("=" * 50)
    
    if not categories:
        print("No categories yet. Add categories first!")
        return
    
    print("\nSelect category:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")
    print("-" * 50)
    
    try:
        user_input = int(input("Choose a category: "))
        while user_input < 1 or user_input > len(categories):
            user_input = int(input("No category found. Try again: "))
        income_category = categories[user_input - 1]
    except ValueError:
        print("Wrong input")
        return
    
    try:
        user_income = int(input("Enter income amount: $"))
        while user_income < 1:
            user_income = int(input("Invalid amount. Try again: $"))
    except ValueError:
        print("Wrong input")
        return
    
    expenses.append(f"{user_income}:{income_category}")
    account += user_income
    print(f"\nIncome of ${user_income} added to '{income_category}'")
    print(f"New balance: ${account}")

def save_data():
    with open('categories.txt', 'w') as file:
        file.write('\n'.join(categories))
    with open('expenses.txt', 'w') as file:
        file.write('\n'.join(expenses))
    with open('account.txt', 'w') as file:
        file.write(str(account))

def main_menu():
    print("\n" + "=" * 50)
    print("       EXPENSE TRACKER")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 50)
        print("  MAIN MENU")
        print("-" * 50)
        print("  1. Add Category")
        print("  2. Remove Category")
        print("  3. View Categories")
        print("  4. Add Expense")
        print("  5. Add Income")
        print("  6. Quit")
        print("-" * 50)
        print(f"  Current Balance: ${account}")
        print("-" * 50)
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            add_categories()
        elif choice == "2":
            remove_category()
        elif choice == "3":
            view_categories()
        elif choice == "4":
            add_expense()
        elif choice == "5":
            add_income()
        elif choice == "6":
            save_data()
            print("\n" + "=" * 50)
            print("Data saved successfully!")
            print("Exiting the programm...!")
            print("=" * 50)
            break
        else:
            print("\nInvalid option. Please try again.")

main_menu()