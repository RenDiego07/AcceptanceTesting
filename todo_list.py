class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def set_dueDate(self, new_date):
        self.due_date = new_date

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} [{status}]\n  Description: {self.description}\n  Priority: {self.priority}\n  Due: {self.due_date}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, due_date):
        task = Task(title, description, priority, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.\n")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}\n")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.\n")
        else:
            print("Invalid index.\n")

    def update_dueDate(self, index, new_date):
        if 0 <= index < len(self.tasks):
            self.tasks[index].set_dueDate(new_date)
            print(f"New due date set to: {new_date}")
        else:
            print("Invalid index")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed")
        else:
            print("Invalid index")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.\n")


def main():
    todo = ToDoList()

    while True:
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority: ")
            due_date = input("Due date: ")
            todo.add_task(title, description, priority, due_date)

        elif choice == "2":
            todo.list_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter task number to mark as completed: "))
                todo.mark_completed(index)
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "4":
            todo.clear_tasks()

        elif choice == "5":
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
