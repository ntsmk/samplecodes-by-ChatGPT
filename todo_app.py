class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Added task: "{task}"')

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{i}. {task['task']} - {status}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Marked task {task_number} as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f'Deleted task: "{deleted_task["task"]}"')
        else:
            print("Invalid task number.")

    def show_menu(self):
        print("\nTo-Do App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                task_number = int(input("Enter task number to complete: "))
                self.complete_task(task_number)
            elif choice == '4':
                task_number = int(input("Enter task number to delete: "))
                self.delete_task(task_number)
            elif choice == '5':
                print("Exiting To-Do App. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
