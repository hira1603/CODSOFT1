def _init_(self, title, description, status='Pending'):
        self.title, self.description, self.status = title, description, status

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.title} - {task.description} - {task.status}")

    def update_task_status(self, task_index, new_status):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].status = new_status
            print(f"Task {task_index} status updated to {new_status}")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Update Task Status\n4. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            title, description = input("Enter task title: "), input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            print("Task added successfully.")

        elif choice == 2:
            print("\n--- To-Do List ---")
            todo_list.show_tasks()

        elif choice == 3:
            todo_list.show_tasks()
            try:
                task_index, new_status = int(input("Enter task index to update status: ")), input("Enter new status: ")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
            todo_list.update_task_status(task_index, new_status)

        elif choice == 4:
            print("Exiting To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()

