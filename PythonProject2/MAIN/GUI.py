import tkinter as tk
from tkinter import messagebox, ttk
from DAO.PROJECTREPOSITORYIMPL import ProjectRepositoryImpl
from ENTITY.EMPLOYEE import Employee
from ENTITY.PROJECT import Project
from ENTITY.TASK import Task
from EXCEPTIONS.EMPLOYEENOTFOUND import EmployeeNotFoundException
from EXCEPTIONS.PROJECTNOTFOUND import ProjectNotFoundException

class ProjectManagementGUI:
    def __init__(self, root):
        self.repo = ProjectRepositoryImpl()
        self.root = root
        self.root.title("Project Management System")
        self.root.geometry("700x500")

        self.welcome_frame = tk.Frame(root)
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)

        self.option_frame = tk.Frame(root)
        self.form_frame = tk.Frame(root)

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame.columnconfigure(0, weight=1)
        self.welcome_frame.rowconfigure([0, 1, 2], weight=1)

        tk.Label(
            self.welcome_frame,
            text="Welcome to the Project Management System",
            font=("Arial", 16)
        ).grid(row=0, column=0, pady=20)


        tk.Button(
            self.welcome_frame,
            text="Click Here",
            font=("Arial", 12),
            width=20,
            command=self.show_main_screen
        ).grid(row=2, column=0, pady=10)

    def show_main_screen(self):
        self.welcome_frame.destroy()
        self.option_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.create_option_buttons()

    def create_option_buttons(self):
        options = [
            ("Add Employee", self.add_employee),
            ("Add Project", self.add_project),
            ("Add Task", self.add_task),
            ("Assign Project", self.assign_project),
            ("Assign Task", self.assign_task),
            ("Delete Employee", self.delete_employee),
            ("Delete Project", self.delete_project),
            ("List Tasks", self.list_tasks),
            ("Exit", self.root.quit)
        ]
        for text, command in options:
            tk.Button(self.option_frame, text=text, width=20, command=command).pack(pady=5)

    def clear_form(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()

    def create_input(self, label_text):
        label = tk.Label(self.form_frame, text=label_text)
        label.pack()
        entry = tk.Entry(self.form_frame, width=30)
        entry.pack()
        return entry

    def display_table(self, columns, data, headings):
        self.clear_form()
        tree = ttk.Treeview(self.form_frame, columns=columns, show="headings", height=10)
        for col, heading in zip(columns, headings):
            tree.heading(col, text=heading)
            tree.column(col, width=100, anchor='center')
        for row in data:
            tree.insert("", "end", values=row)
        tree.pack(fill=tk.BOTH, expand=True)

    def add_employee(self):
        self.clear_form()
        eid = self.create_input("Employee ID")
        name = self.create_input("Name")
        desg = self.create_input("Designation")
        gender = self.create_input("Gender")
        salary = self.create_input("Salary")
        pid = self.create_input("Project ID (0 if none)")

        def submit():
            try:
                emp = Employee(
                    int(eid.get()), name.get(), desg.get(),
                    gender.get(), float(salary.get()),
                    None if pid.get() == "0" else int(pid.get())
                )
                if self.repo.create_employee(emp):
                    messagebox.showinfo("Success", "Employee added.")
                else:
                    messagebox.showerror("Failed", "Could not add employee.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Submit", command=submit).pack(pady=10)

    def add_project(self):
        self.clear_form()
        pid = self.create_input("Project ID")
        name = self.create_input("Project Name")
        desc = self.create_input("Description")
        date = self.create_input("Start Date (YYYY-MM-DD)")
        status = self.create_input("Status")

        def submit():
            try:
                proj = Project(int(pid.get()), name.get(), desc.get(), date.get(), status.get())
                if self.repo.create_project(proj):
                    messagebox.showinfo("Success", "Project added.")
                else:
                    messagebox.showerror("Failed", "Could not add project.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Submit", command=submit).pack(pady=10)

    def add_task(self):
        self.clear_form()
        tid = self.create_input("Task ID")
        name = self.create_input("Task Name")
        pid = self.create_input("Project ID")
        eid = self.create_input("Employee ID (0 if not assigned)")
        status = self.create_input("Task Status")

        def submit():
            try:
                task = Task(
                    int(tid.get()), name.get(), int(pid.get()),
                    None if eid.get() == "0" else int(eid.get()), status.get()
                )
                if self.repo.create_task(task):
                    messagebox.showinfo("Success", "Task added.")
                else:
                    messagebox.showerror("Failed", "Could not add task.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Submit", command=submit).pack(pady=10)

    def assign_project(self):
        self.clear_form()
        pid = self.create_input("Project ID")
        eid = self.create_input("Employee ID")

        def submit():
            try:
                if self.repo.assign_project_to_employee(int(pid.get()), int(eid.get())):
                    messagebox.showinfo("Success", "Project assigned.")
                else:
                    messagebox.showerror("Failed", "Could not assign project.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Assign", command=submit).pack(pady=10)

    def assign_task(self):
        self.clear_form()
        tid = self.create_input("Task ID")
        pid = self.create_input("Project ID")
        eid = self.create_input("Employee ID")

        def submit():
            try:
                if self.repo.assign_task_to_employee_in_project(int(tid.get()), int(pid.get()), int(eid.get())):
                    messagebox.showinfo("Success", "Task assigned.")
                else:
                    messagebox.showerror("Failed", "Could not assign task.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Assign", command=submit).pack(pady=10)

    def delete_employee(self):
        self.clear_form()
        eid = self.create_input("Employee ID to Delete")

        def submit():
            try:
                if self.repo.delete_employee(int(eid.get())):
                    messagebox.showinfo("Success", "Employee deleted.")
                else:
                    messagebox.showerror("Failed", "Could not delete employee.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Delete", command=submit).pack(pady=10)

    def delete_project(self):
        self.clear_form()
        pid = self.create_input("Project ID to Delete")

        def submit():
            try:
                if self.repo.delete_project(int(pid.get())):
                    messagebox.showinfo("Success", "Project deleted.")
                else:
                    messagebox.showerror("Failed", "Could not delete project.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="Delete", command=submit).pack(pady=10)

    def list_tasks(self):
        self.clear_form()
        eid = self.create_input("Employee ID")
        pid = self.create_input("Project ID")

        def submit():
            try:
                tasks = self.repo.get_all_tasks_for_employee_in_project(int(eid.get()), int(pid.get()))
                if tasks:
                    tk.Label(self.form_frame, text="\nAssigned Tasks:", font=("Arial", 10, "bold")).pack()
                    for task in tasks:
                        task_info = f"ID: {task.get_task_id()} | Name: {task.get_task_name()} | Status: {task.get_status()}"
                        tk.Label(self.form_frame, text=task_info).pack()
                else:
                    messagebox.showinfo("Info", "No tasks found.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.form_frame, text="List Tasks", command=submit).pack(pady=10)





# Start the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectManagementGUI(root)
    root.mainloop()