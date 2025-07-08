from behave import *
from todo_list import ToDoList, Task


@given('the to-do list is empty')
def step_impl(context):
    context.todo = ToDoList()

@when('the user adds a task "{task_title}"')
def step_impl(context, task_title):
    context.todo.add_task(task_title, "Default description", "Medium", "Today")

@then('the to-do list should contain "{task_title}"')
def step_impl(context, task_title):
    titles = [task.title for task in context.todo.tasks]
    assert task_title in titles, f'Task "{task_title}" not found in to-do list'



@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        task_title = row['Task']
        context.todo.add_task(task_title, "description", "Medium", "2025-07-15")

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo.tasks) == 0




@given('the to-do list contains a task titled "{title}" with due date "{due_date}"')
def step_impl(context, title, due_date):
    context.todo = ToDoList()
    context.todo.add_task(title, "Complete the report for next week", "High", due_date)

@when('the user updates the due date of task {index:d} to "{new_due_date}"')
def step_impl(context, index, new_due_date):
    context.todo.update_due_date(index, new_due_date)

@then('the task "{title}" should have due date "{expected_due_date}"')
def step_impl(context, title, expected_due_date):
    for task in context.todo.tasks:
        if task.title == title:
            assert task.due_date == expected_due_date
            return
    assert False, f"Task '{title}' not found."


    

@when('the user removes task at index {index:d}')
def step_impl(context, index):
    context.todo.remove_task(index)

@then('the to-do list should contain:')
def step_impl(context):
    expected_titles = [row['Task'] for row in context.table]
    actual_titles = [task.title for task in context.todo.tasks]
    assert expected_titles == actual_titles
