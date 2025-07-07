Feature: To-Do List Manager

    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user lists all tasks
        Then the output should contain:
            | Task          |
            | Buy groceries |
            | Pay bills     |
     

    Scenario: Mark a task as completed
        Given the to-do list contains tasks:
            | Task          | Status   |
            | Buy groceries | Pending  |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

        Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user clears the to-do list
        Then the to-do list should be empty


    Scenario: Update the due date of a task
        Given the to-do list contains a task titled "Finish report" with due date "Friday"
        When the user updates the due date of task 0 to "Monday"
        Then the task "Finish report" should have due date "Monday"

    Scenario: Remove a task from the to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user removes task at index 0
    Then the to-do list should contain:
        | Task      |
        | Pay bills |

