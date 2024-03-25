'''TO-DO LIST

TASK 1

A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing

users to create, update, and track their to-do lists
'''

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do list is empty.")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List\n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Update Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            task_index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(task_index)
            print("Task removed successfully.")
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            task_index = int(input("Enter the task index to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
            print("Task updated successfully.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()