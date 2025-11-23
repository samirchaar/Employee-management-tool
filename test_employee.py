import pytest
import employee_system as es

def test_add_employee():
    es.add_employee("test_employee", 2000.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    assert lines[-1].strip() == "test_employee,2000.0"

def test_add_employee_with_zero_salary():
    es.add_employee("zero_salary", 0.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("zero_salary"):
            assert line.strip() == "zero_salary,0.0"
            found = True
    assert found

def test_add_employee_with_high_salary():
    es.add_employee("high_salary", 100000.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("high_salary"):
            assert line.strip() == "high_salary,100000.0"
            found = True
    assert found

def test_update_salary():
    es.add_employee("update_test", 1500.0)
    es.update_salary("update_test", 1800.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("update_test"):
            assert line.strip() == "update_test,1800.0"
            found = True
    assert found, "Employee not found after update"

def test_update_salary_employee_not_found():
    es.update_salary("nonexistent_employee", 5000.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("nonexistent_employee"):
            found = True
    assert not found

def test_update_salary_to_zero():
    es.add_employee("zero_update", 3000.0)
    es.update_salary("zero_update", 0.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("zero_update"):
            assert line.strip() == "zero_update,0.0"
            found = True
    assert found

def test_give_bonus():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("bonus_test", 1200.0)
    es.give_bonus("bonus_test", 300.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("bonus_test"):
            assert line.strip() == "bonus_test,1500.0"
            found = True
    assert found, "Employee not found after bonus"

def test_give_bonus_employee_not_found():
    es.give_bonus("nonexistent_bonus", 500.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("nonexistent_bonus"):
            found = True
    assert not found

def test_give_bonus_zero_amount():
    es.add_employee("zero_bonus", 2000.0)
    es.give_bonus("zero_bonus", 0.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("zero_bonus"):
            assert line.strip() == "zero_bonus,2000.0"
            found = True
    assert found

def test_give_bonus_negative_amount():
    es.add_employee("negative_bonus", 3000.0)
    es.give_bonus("negative_bonus", -500.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("negative_bonus"):
            assert line.strip() == "negative_bonus,2500.0"
            found = True
    assert found

def test_delete_employee():
    es.add_employee("delete_test", 2500.0)
    es.delete_employee("delete_test")
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("delete_test"):
            found = True
    assert not found

def test_delete_employee_not_found():
    es.delete_employee("nonexistent_delete")
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith("nonexistent_delete"):
            found = True
    assert not found

def test_search_employee_found():
    es.add_employee("search_test", 4000.0)
    result = es.search_employee("search_test")
    assert result == True

def test_search_employee_not_found():
    result = es.search_employee("nonexistent_search")
    assert result == False

def test_count_employees():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("count1", 1000.0)
    es.add_employee("count2", 2000.0)
    es.add_employee("count3", 3000.0)
    count = es.count_employees()
    assert count == 3

def test_count_employees_empty_file():
    with open("employees.txt", "w") as file:
        file.write("")
    count = es.count_employees()
    assert count == 0

def test_get_average_salary():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("avg1", 1000.0)
    es.add_employee("avg2", 2000.0)
    es.add_employee("avg3", 3000.0)
    average = es.get_average_salary()
    assert average == 2000.0

def test_get_average_salary_empty_file():
    with open("employees.txt", "w") as file:
        file.write("")
    average = es.get_average_salary()
    assert average == 0.0

def test_get_highest_paid():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("low_emp", 1000.0)
    es.add_employee("high_emp", 5000.0)
    es.add_employee("mid_emp", 3000.0)
    highest = es.get_highest_paid()
    assert highest == "high_emp"

def test_get_highest_paid_single_employee():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("only_emp", 2500.0)
    highest = es.get_highest_paid()
    assert highest == "only_emp"

def test_get_lowest_paid():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("low_emp", 1000.0)
    es.add_employee("high_emp", 5000.0)
    es.add_employee("mid_emp", 3000.0)
    lowest = es.get_lowest_paid()
    assert lowest == "low_emp"

def test_get_lowest_paid_single_employee():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("only_emp", 2500.0)
    lowest = es.get_lowest_paid()
    assert lowest == "only_emp"

def test_get_total_payroll():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("payroll1", 1000.0)
    es.add_employee("payroll2", 2000.0)
    es.add_employee("payroll3", 3000.0)
    total = es.get_total_payroll()
    assert total == 6000.0

def test_get_total_payroll_empty_file():
    with open("employees.txt", "w") as file:
        file.write("")
    total = es.get_total_payroll()
    assert total == 0.0

def test_add_multiple_employees_same_name():
    es.add_employee("duplicate", 1000.0)
    es.add_employee("duplicate", 2000.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        if line.startswith("duplicate"):
            count = count + 1
    assert count == 2

def test_update_salary_first_duplicate():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("dup", 1000.0)
    es.add_employee("dup", 2000.0)
    es.update_salary("dup", 1500.0)
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        if line.startswith("dup"):
            assert line.strip() == "dup,1500.0"
            count = count + 1
    assert count == 2

def test_delete_first_duplicate():
    with open("employees.txt", "w") as file:
        file.write("")
    es.add_employee("del_dup", 1000.0)
    es.add_employee("del_dup", 2000.0)
    es.delete_employee("del_dup")
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        if line.startswith("del_dup"):
            count = count + 1
    assert count == 0











