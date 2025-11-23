I wrote a comprehensive set of tests to cover all major parts of my program. I used pytest, and all tests are located in test_employee.py.

The tests cover adding employees with normal, zero, and very large salaries, as well as handling duplicate names. For updating, I tested standard updates, updating a salary to zero, and attempting to update a name that doesn’t exist. For bonuses, I tested regular bonuses, zero bonuses, and negative bonuses. Deleting is tested with both existing and non-existing names. I also tested searching and all the math-related functions, including count, average, highest-paid, lowest-paid, and total payroll. Each of these was tested with multiple employees and with an empty file to ensure the program doesn’t crash.

For manual testing, I walked through the program’s interface and followed the manual test plan to verify each menu option and confirm that data persists correctly in the file.

Overall, the automated tests cover nearly all program logic, while the manual plan ensures the user interface behaves as expected.
