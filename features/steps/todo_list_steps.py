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



@given('the to-do list contains tasks')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'], "Default", "Low", "Anytime")

@then('the to-do list should contain')
def step_impl(context):
    expected_titles = [row['Task'] for row in context.table]
    actual_titles = [task.title for task in context.todo.tasks]
    assert actual_titles == expected_titles, f"Expected {expected_titles}, but got {actual_titles}"



@when('the user lists all tasks')
def step_impl(context):
    context.listed_titles = [task.title for task in context.todo.tasks]

@then('the output should contain')
def step_impl(context):
    expected = [row['Task'] for row in context.table]
    for title in expected:
        assert title in context.listed_titles, f'Task "{title}" not found in output'



@given('the to-do list contains tasks with status:')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        title = row['Task']
        context.todo.add_task(title, "Desc", "Medium", "Tomorrow")

@when('the user marks task "{task_title}" as completed')
def step_impl(context, task_title):
    for i, task in enumerate(context.todo.tasks):
        if task.title == task_title:
            context.todo.mark_completed(i)
            break

@then('the to-do list should show task "{task_title}" as completed')
def step_impl(context, task_title):
    for task in context.todo.tasks:
        if task.title == task_title:
            assert task.completed is True, f'Task "{task_title}" is not marked as completed'
            return
    assert False, f'Task "{task_title}" not found'





@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo.tasks) == 0



@given('the to-do list contains a task titled "{title}" with due date "{due_date}"')
def step_impl(context, title, due_date):
    context.todo = ToDoList()
    context.todo.add_task(title, "desc", "High", due_date)

@when('the user updates the due date of task {index:d} to "{new_date}"')
def step_impl(context, index, new_date):
    context.todo.update_dueDate(index, new_date)

@then('the task "{title}" should have due date "{new_date}"')
def step_impl(context, title, new_date):
    for task in context.todo.tasks:
        if task.title == title:
            assert task.due_date == new_date, f"Expected {new_date}, found {task.due_date}"
            return
    assert False, f"Task '{title}' not found"


@when('the user removes task at index {index:d}')
def step_impl(context, index):
    context.todo.remove_task(index)

