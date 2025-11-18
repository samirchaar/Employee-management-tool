def main():
    print("Welcome to the Employee Management System!")
    print()
    print("Please select an option:")
    print("1-View Employees\n2-Add Employee\n3-Update Salary\n4-Give Bonus\n5-Payroll report\n6-Exit")
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        view_employees()
    elif choice == 2:
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        add_employee(name, salary)
    elif choice == 3:
        name = input("Enter employee name to update salary: ")
        salary = float(input("Enter new salary: "))
        update_salary(name,salary)
    elif choice == 4:
        name = input("Enter employee name to give bonus: ")
        bonus_amount = float(input("Enter bonus amount: "))
        give_bonus(name, bonus_amount)
    elif choice == 5:
        payroll_report()
    elif choice == 6:
        print("Exiting the system")
    else:
        print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()