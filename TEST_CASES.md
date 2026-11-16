
# Test Cases – Daily Task Manager

The following test cases will be used to check the program.

| Test | Type | Input / Action | Expected Result | Actual Result |
|---|---|---|---|---|
| 1 | Normal | Add a task titled Study Python with description Review loops and due date 2026-11-20 | Task is added and displayed as Pending | To be tested |
| 2 | Boundary | Try to complete task number 0 | Program rejects the number and displays the valid range | To be tested |
| 3 | Invalid Input | Enter hello at the main menu | Program displays an invalid choice message without crashing | To be tested |
| 4 | Invalid Date | Enter 20-11-2026 as the due date | Program rejects the date and explains the correct format | To be tested |
| 5 | File Handling | Add a task, exit, and reopen the program | Previously saved task is displayed | To be tested |

## Testing Notes

Run each test in PyCharm and record the actual result.

Do not mark a test as successful until you have verified its output.
