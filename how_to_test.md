I used pytest to validate all the program’s functions. If you don’t already have pytest installed, you can add it using pip. To run the automated tests, open a terminal in the project folder and run pytest.

All tests are located in test_employee.py, and they cover adding employees, updating records, applying bonuses, deleting entries, searching, and performing calculations like averages and totals. I also included tests for edge cases such as empty files, zero salaries, and negative bonuses to make sure the program doesn’t crash.

For manual testing, you can run the main program and try each menu option individually. I also created a short manual test plan in manual_test_plan.md that outlines the steps to follow.

If pytest shows green, all automated tests passed; if it shows red, check the error message to see what went wrong.
