from behave import *
from todo_list import ToDoList  # importa tu clase real

to_do_list =[] 

@given('a new to-do list')
def step_impl(context):
    context.todo = ToDoList()

@when('I add a task with title "{title}" and description "{desc}", priority "{priority}" and due date "{due}"')
def step_impl(context, title, desc, priority, due):
    context.todo.add_task(title, desc, priority, due)

@then('the task list should contain {count:d} task')
@then('the task list should contain {count:d} tasks')

def step_impl(context, count):
    assert len(context.todo.tasks) == count


    

# Scenario : Add a new task
@given('')