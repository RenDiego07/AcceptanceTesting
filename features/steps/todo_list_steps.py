from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        title = row['Task']
        context.todo_list.add_task(title, "desc", "normal", "Friday")  # valores por defecto

@given('the to-do list contains a task titled "{title}" with due date "{due_date}"')
def step_impl(context, title, due_date):
    context.todo_list = ToDoList()
    context.todo_list.add_task(title, "desc", "normal", due_date)

@when('the user adds a task "{title}"')
def step_impl(context, title):
    context.todo_list.add_task(title, "desc", "normal", "Friday")  # valores por defecto

@when('the user lists all tasks')
def step_impl(context):
    context.list_output = [task.title for task in context.todo_list.tasks]

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    for i, task in enumerate(context.todo_list.tasks):
        if task.title == title:
            context.todo_list.mark_completed(i)
            break

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()

@when('the user updates the due date of task {index:d} to "{new_due_date}"')
def step_impl(context, index, new_due_date):
    context.todo_list.update_dueDate(index, new_due_date)

@when('the user removes task at index {index:d}')
def step_impl(context, index):
    context.todo_list.remove_task(index)

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.todo_list.tasks]
    assert title in titles, f"'{title}' not in {titles}"

@then('the to-do list should contain')
def step_impl(context):
    expected_titles = [row['Task'] for row in context.table]
    actual_titles = [task.title for task in context.todo_list.tasks]
    assert expected_titles == actual_titles, f"Expected {expected_titles}, but got {actual_titles}"

@then('the output should contain')
def step_impl(context):
    expected_titles = [row['Task'] for row in context.table]
    assert context.list_output == expected_titles, f"Expected {expected_titles}, but got {context.list_output}"

@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    for task in context.todo_list.tasks:
        if task.title == title:
            assert task.completed is True, f"Task '{title}' is not marked as completed"
            return
    assert False, f"Task '{title}' not found"

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0

@then('the task "{title}" should have due date "{due_date}"')
def step_impl(context, title, due_date):
    for task in context.todo_list.tasks:
        if task.title == title:
            assert task.due_date == due_date, f"Expected '{due_date}' but got '{task.due_date}'"
            return
    assert False, f"Task '{title}' not found"
