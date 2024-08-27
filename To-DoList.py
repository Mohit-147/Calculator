import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        # Define listbox to display tasks
        self.tasks = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.tasks.pack(pady=20)

        # Entry widget to enter new tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add Task button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Mark as Completed button
        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.pack(pady=5)

        # Delete Task button
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_completed(self):
        selected_task_index = self.tasks.curselection()
        if selected_task_index:
            task = self.tasks.get(selected_task_index)
            self.tasks.delete(selected_task_index)
            self.tasks.insert(tk.END, f"{task} [Completed]")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.tasks.curselection()
        if selected_task_index:
            self.tasks.delete(selected_task_index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

