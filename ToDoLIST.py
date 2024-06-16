class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, deadline, priority):
        self.tasks.append({"task": task, "deadline": deadline, "priority": priority})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task['task']} - Deadline: {task['deadline']}, Priority: {task['priority']}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["task"] += " (Completed)"
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ")
            todo_list.add_task(task, deadline, priority)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
