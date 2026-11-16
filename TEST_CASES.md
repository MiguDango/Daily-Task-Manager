# Test Cases – Daily Task Manager

> These are simulated results from running the updated program in an isolated Python test environment. Run the same tests in PyCharm and update the actual results if your instructor requires personal test evidence.

| Test ID | Type | Input / Action | Expected Result | Simulated Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Add `Study Python`, description `Review loops`, due date `2026-11-20`, then view tasks | Task is added and displayed as Pending | Task was added and displayed as Pending | PASS |
| TC02 | Boundary | Add one task, then try to complete task number `0` | Program rejects the number and displays the valid range | Displayed `Choose a number from 1 to 1.` | PASS |
| TC03 | Invalid Input | Enter `hello` at the main menu | Program displays an invalid-choice message without crashing | Displayed `Invalid choice. Select a number from 1 to 5.` | PASS |
| TC04 | Invalid Date | Enter `20-11-2026` as the due date | Program rejects the date and does not add the task | Displayed `Invalid date. Use YYYY-MM-DD.` | PASS |
| TC05 | File Handling | Add a task, exit, restart the program, and view tasks | Previously saved task appears after restart | `Read chapter` appeared after restarting | PASS |

## Verification Notes

The cases above were executed with prepared inputs in an isolated test environment. They are simulated results, not a claim that the student personally ran the tests in PyCharm. Re-run them in PyCharm if required and replace the simulated results with the observations from that run.
