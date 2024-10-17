import pandas as pd

import matplotlib.pyplot as plt





def visualize_expenses():

    df = pd.read_csv('expenses.csv')

    if df.empty:

        print("No expenses to visualize.")

        return





    category_data = df.groupby('Category')['Amount'].sum()





    category_data.plot(kind ='bar', color ='skyblue')

    plt.xlabel('Category')

    plt.ylabel('Total Amount')

    plt.title('Expenses by Category')

    plt.xticks(rotation=45)

    plt.tight_layout()





    plt.show()




EXPENSE_FILE = 'expenses.csv'




def add_expense(expense_name, amount, category):

    try:

        df = pd.read_csv(EXPENSE_FILE)

    except FileNotFoundError:

        df = pd.DataFrame(columns=['Expense Name', 'Amount', 'Category'])





    new_expense = {'Expense Name': expense_name, 'Amount': amount, 'Category': category}

    if df.empty:

        df = pd.DataFrame([new_expense])

    else:

        df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
        
 
    df.to_csv(EXPENSE_FILE, index=False)

    print(f"Added expense: {expense_name}, Amount: {amount}, Category: {category}")




def view_expenses():

    try:

        df = pd.read_csv(EXPENSE_FILE)

        print(df)

    except FileNotFoundError:

        print("No expenses recorded yet.")




def main():

    while True:

        print("\nExpense Tracker menu:")

        print("1. Add an expense")

        print("2. View all expenses")

        print("3. Visualize expenses")

        print("4. Exit")




        choice = input("Enter your choice: ")

        if choice == '1':

            expense_name = input("Enter expense name: ")

            amount = float(input("Enter amount: "))

            category = input("Enter category (e.g., Food, Transport, etc.): ")

            add_expense(expense_name, amount, category)

        elif choice == '2':

            view_expenses()

        elif choice == '3':

            visualize_expenses()

        elif choice == '4':

            break

        else:

            print("Invalid choice. Please try again.")





if __name__ == "__main__":

    main()
