Feature: To-Do List Manager

  Scenario: Add a new task
    Given a new to-do list
    When I add a task with title "Buy milk" and description "Get 2 liters", priority "High" and due date "Tomorrow"
    Then the task list should contain 1 task

  Scenario: List tasks
    Given a new to-do list
    And I add 2 tasks
    When I list the tasks
    Then I should see 2 tasks

  Scenario: Mark a task as completed
    Given a to-do list with one task
    When I mark the first task as completed
    Then the task should be marked as completed

  Scenario: Clear the task list
    Given a to-do list with 3 tasks
    When I clear the task list
    Then the task list should be empty