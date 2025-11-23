def add_employee(name,salary):
    with open("employees.txt", "a") as file:
        file.write(name+ "," +str(salary)+"\n")
    print("Employee",name,"added successfully.")
def view_employees():
    print("Employee List:")
    with open("employees.txt", "r") as file:
        for line in file:
            pair = line.strip().split(",")
            name = pair[0]
            salary= pair[1]
            print("Name:", name, ", Salary:", salary)
def update_salary(name,salary):
    employees = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            pair = line.strip().split(",")
            employee_name = pair[0]
            employee_salary = pair[1]
            if employee_name == name:
                employees.append(name + "," + str(salary) + "\n")
                found = True
            else:
                employees.append(line)
    if found==True:
        with open("employees.txt", "w") as file:
            file.writelines(employees)
        print("Salary updated for", name)
    else:
        print("Employee", name, "not found.")
def give_bonus(name, bonus_amount):
    employees = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            pair = line.strip().split(",")
            employee_name = pair[0]
            employee_salary = float(pair[1])
            if employee_name == name:
                new_salary = employee_salary + bonus_amount
                employees.append(name + "," + str(new_salary) + "\n")
                found = True
            else:
                employees.append(line)
    if found==True:
        with open("employees.txt", "w") as file:
            file.writelines(employees)
        print("Bonus given to", name)
    else:
        print("Employee", name, "not found.")
def payroll_report():
    total_payroll = 0.0
    print("Payroll Report:")
    with open("employees.txt", "r") as file:
        for line in file:
            pair = line.strip().split(",")
            name = pair[0]
            salary = float(pair[1])
            total_payroll += salary
            print("Name:", name, ", Salary:", salary)
    print("Total Payroll Amount:", total_payroll)
def delete_employee(name):
    employees = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            pair = line.strip().split(",")
            employee_name = pair[0]
            if employee_name == name:
                found = True
            else:
                employees.append(line)
    if found==True:
        with open("employees.txt", "w") as file:
            file.writelines(employees)
        print("Employee", name, "deleted successfully.")
    else:
        print("Employee", name, "not found.")
def search_employee(name):
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            pair = line.strip().split(",")
            employee_name = pair[0]
            employee_salary = pair[1]
            if employee_name == name:
                print("Employee found - Name:", employee_name, ", Salary:", employee_salary)
                found = True
    if found==False:
        print("Employee", name, "not found.")
    return found
def count_employees():
    count = 0
    with open("employees.txt", "r") as file:
        for line in file:
            if line.strip() != "":
                count = count + 1
    return count
def get_average_salary():
    total = 0.0
    count = 0
    with open("employees.txt", "r") as file:
        for line in file:
            if line.strip() != "":
                pair = line.strip().split(",")
                salary = float(pair[1])
                total = total + salary
                count = count + 1
    if count > 0:
        average = total / count
        return average
    else:
        return 0.0
def get_highest_paid():
    highest_salary = 0.0
    highest_name = ""
    with open("employees.txt", "r") as file:
        for line in file:
            if line.strip() != "":
                pair = line.strip().split(",")
                name = pair[0]
                salary = float(pair[1])
                if salary > highest_salary:
                    highest_salary = salary
                    highest_name = name
    return highest_name
def get_lowest_paid():
    lowest_salary = 999999999.0
    lowest_name = ""
    first = True
    with open("employees.txt", "r") as file:
        for line in file:
            if line.strip() != "":
                pair = line.strip().split(",")
                name = pair[0]
                salary = float(pair[1])
                if first==True:
                    lowest_salary = salary
                    lowest_name = name
                    first = False
                else:
                    if salary < lowest_salary:
                        lowest_salary = salary
                        lowest_name = name
    return lowest_name
def get_total_payroll():
    total = 0.0
    with open("employees.txt", "r") as file:
        for line in file:
            if line.strip() != "":
                pair = line.strip().split(",")
                salary = float(pair[1])
                total = total + salary
    return total
    
def main():
    print("Welcome to the Employee Management System!")
    print()
    print("Please select an option:")
    print("1-View Employees\n2-Add Employee\n3-Update Salary\n4-Give Bonus\n5-Payroll Report\n6-Delete Employee\n7-Search Employee\n8-Statistics\n9-Exit")
    choice = int(input("Enter your choice (1-9): "))
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
        name = input("Enter employee name to delete: ")
        delete_employee(name)
    elif choice == 7:
        name = input("Enter employee name to search: ")
        search_employee(name)
    elif choice == 8:
        print("Statistics:")
        print("Total Employees:", count_employees())
        print("Average Salary:", get_average_salary())
        print("Total Payroll:", get_total_payroll())
        print("Highest Paid Employee:", get_highest_paid())
        print("Lowest Paid Employee:", get_lowest_paid())
    elif choice == 9:
        print("Exiting the system")
    else:
        print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()